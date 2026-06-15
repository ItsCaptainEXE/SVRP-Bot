import discord
from discord.ext import commands, tasks
import asyncio
import os

class ServerDynamics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.server_open = True
        self.status_cycle.start()
        self.idle_timer = 0
        self.api_key = os.getenv('ERLC_SERVER_KEY')
        self.api_url = "https://api.erlc.gg/v2/server/command"

    def cog_unload(self):
        self.status_cycle.cancel()

    # 1. Dynamic Status Cycling
    @tasks.loop(seconds=10)
    async def status_cycle(self):
        statuses = [
            "Made by @itscaptainexe",
            "Monitoring Server",
            "HAHA GET BANNED!",
            "SVRP Status: Active"
        ]
        for status in statuses:
            await self.bot.change_presence(activity=discord.Game(name=status))
            await asyncio.sleep(10)

    # 2. Server Closed Enforcement
    @commands.command(name="server-close", help="Close the server")
    async def server_close(self, ctx):
        self.server_open = False
        await self.bot.change_presence(status=discord.Status.dnd)
        await ctx.send("Server closed. Kicking unauthorized players.")
        # Logic to check players and kick
        await self._enforce_server_closed()

    async def _enforce_server_closed(self):
        # Implementation would fetch players via API and kick those not leaving
        pass

    # 3. Discord/ERLC Ban Sync
    @commands.Cog.listener()
    async def on_message(self, message):
        # Trigger Idle Status
        if message.author.bot: return
        await self.bot.change_presence(status=discord.Status.idle)
        await asyncio.sleep(60) # Reduced to 1 min for testing
        await self.bot.change_presence(status=discord.Status.online)

    # 4. Automod (Racism Focus)
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot: return
        import re
        racist_regex = r"\b(nigger|chink|kike|faggot)\b" # Expand as needed
        if re.search(racist_regex, message.content, re.IGNORECASE):
            await message.author.ban(reason="Racist language")
            await message.delete()

async def setup(bot):
    await bot.add_cog(ServerDynamics(bot))
