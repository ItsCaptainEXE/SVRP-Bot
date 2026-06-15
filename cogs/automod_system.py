import discord
from discord.ext import commands
import re
import json
import os

class AutoModSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.rules = self.load_rules()

    def load_rules(self):
        rules_path = 'bot/automod_rules.json'
        if not os.path.exists(rules_path):
            return []
        with open(rules_path, 'r') as f:
            data = json.load(f)
            # Pre-compile regex for speed
            return [{"id": r["id"], "pattern": re.compile(r["pattern"], re.IGNORECASE), "desc": r["description"]} for r in data["rules"]]

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # Apply all 101 rules
        for rule in self.rules:
            if rule["pattern"].search(message.content):
                await message.delete()
                await message.channel.send(f"{message.author.mention}, your message violated rule: {rule['desc']}")
                return

async def setup(bot):
    await bot.add_cog(AutoModSystem(bot))
