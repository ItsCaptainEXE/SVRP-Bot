import discord
from discord.ext import commands
import re

class Automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Framework to hold 100+ rules
        self.rules = {
            "bad_words": ["badword1", "badword2", "spammy"],
            "spam_threshold": 3
        }

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # 1. Word Filtering (Example of multiple rules)
        for word in self.rules["bad_words"]:
            if word in message.content.lower():
                await message.delete()
                await message.channel.send(f"Automod: {message.author.mention}, that word is forbidden.")
                return


        # TODO: Implement remaining 98+ rules here
        # Suggestion: Use a database or JSON file to load rules dynamically.

async def setup(bot):
    await bot.add_cog(Automod(bot))
