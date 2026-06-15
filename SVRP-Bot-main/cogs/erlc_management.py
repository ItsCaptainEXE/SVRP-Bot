import discord
from discord import app_commands
from discord.ext import commands, tasks
from bot.svrp_api import send_api_request
import json
import os

class ERLCManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.recur_channel_id = None
        self.recur_message = "Join our server! SVRP - State of Victor Roleplay"
        self.recur_task.start()

    def cog_unload(self):
        self.recur_task.cancel()

    @tasks.loop(minutes=5)
    async def recur_task(self):
        if self.recur_channel_id:
            channel = self.bot.get_channel(self.recur_channel_id)
            if channel:
                await channel.send(self.recur_message)

    @app_commands.command(name="set-recur", description="Set the recurring hint channel and message")
    async def set_recur(self, interaction: discord.Interaction, channel: discord.TextChannel, message: str):
        self.recur_channel_id = channel.id
        self.recur_message = message
        await interaction.response.send_message(f"Recurring hint set to channel {channel.mention} with message: {message}")

    @app_commands.command(name="server-info", description="Fetch current ERLC server information")
    async def server_info(self, interaction: discord.Interaction):
        # Based on provided schema: GET /server
        data = send_api_request("GET", "server")
        if data:
            embed = discord.Embed(title=f"Server: {data.get('Name')}", color=discord.Color.blue())
            embed.add_field(name="Players", value=f"{data.get('CurrentPlayers')}/{data.get('MaxPlayers')}")
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Failed to fetch server information.")

    @app_commands.command(name="staff-list", description="List current server staff")
    async def staff_list(self, interaction: discord.Interaction):
        data = send_api_request("GET", "server")
        if data and 'Staff' in data:
            staff = data['Staff']
            embed = discord.Embed(title="Server Staff", color=discord.Color.gold())
            for role, members in staff.items():
                member_list = "\n".join(members.values())
                embed.add_field(name=role, value=member_list or "None")
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Failed to fetch staff list.")

async def setup(bot):
    await bot.add_cog(ERLCManagement(bot))
