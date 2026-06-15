import discord
from discord import app_commands
from discord.ext import commands
import time

class UtilityCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    @app_commands.command(name="ping", description="Check bot latency")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms")

    @app_commands.command(name="uptime", description="Check bot uptime")
    async def uptime(self, interaction: discord.Interaction):
        uptime = time.time() - self.start_time
        await interaction.response.send_message(f"Bot has been online for {round(uptime)} seconds.")

    @app_commands.command(name="userinfo", description="Get info about a user")
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(title=f"User Info - {member.name}", color=discord.Color.green())
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Joined", value=member.joined_at.strftime("%Y-%m-%d"))
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="serverinfo", description="Get info about the server")
    async def serverinfo(self, interaction: discord.Interaction):
        guild = interaction.guild
        embed = discord.Embed(title=f"Server Info - {guild.name}", color=discord.Color.blue())
        embed.add_field(name="Members", value=guild.member_count)
        embed.add_field(name="Owner", value=guild.owner)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="echo", description="Echo a message")
    async def echo(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(message)

    @app_commands.command(name="avatar", description="Get a user's avatar")
    async def avatar(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.response.send_message(member.avatar.url)

    @app_commands.command(name="util_time", description="Get time")
    async def util_time(self, interaction: discord.Interaction): await interaction.response.send_message("Time.")
    @app_commands.command(name="util_date", description="Get date")
    async def util_date(self, interaction: discord.Interaction): await interaction.response.send_message("Date.")
    @app_commands.command(name="util_calc", description="Calc")
    async def util_calc(self, interaction: discord.Interaction): await interaction.response.send_message("Calc.")
    @app_commands.command(name="util_shorten", description="Shorten URL")
    async def util_shorten(self, interaction: discord.Interaction): await interaction.response.send_message("Shortened.")
    @app_commands.command(name="util_weather", description="Weather")
    async def util_weather(self, interaction: discord.Interaction): await interaction.response.send_message("Weather.")

async def setup(bot):
    await bot.add_cog(UtilityCommands(bot))
