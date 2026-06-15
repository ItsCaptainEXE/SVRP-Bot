import discord
from discord import app_commands
from discord.ext import commands, tasks
from bot.svrp_api import send_api_request

class ERLCCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.recur_message = "Join our server! SVRP - State of Victor Roleplay"
        self.recur_task.start()

    def cog_unload(self):
        self.recur_task.cancel()

    @tasks.loop(minutes=5)
    async def recur_task(self):
        pass

    @app_commands.command(name="server-status", description="Get ERLC server status")
    async def server_status(self, interaction: discord.Interaction):
        data = send_api_request("GET", "server")
        if data: await interaction.response.send_message(f"Server Status: {data}")
        else: await interaction.response.send_message("Failed to fetch server status.")

    @app_commands.command(name="player_list", description="List players")
    async def player_list(self, interaction: discord.Interaction): await interaction.response.send_message("Players.")
    @app_commands.command(name="player_info", description="Get player info")
    async def player_info(self, interaction: discord.Interaction): await interaction.response.send_message("Player info.")
    @app_commands.command(name="player_kick", description="Kick player")
    async def player_kick(self, interaction: discord.Interaction): await interaction.response.send_message("Player kicked.")
    @app_commands.command(name="player_ban", description="Ban player")
    async def player_ban(self, interaction: discord.Interaction): await interaction.response.send_message("Player banned.")
    @app_commands.command(name="player_warn", description="Warn player")
    async def player_warn(self, interaction: discord.Interaction): await interaction.response.send_message("Player warned.")
    @app_commands.command(name="mgmt_setup", description="Setup management")
    async def mgmt_setup(self, interaction: discord.Interaction): await interaction.response.send_message("Setup.")
    @app_commands.command(name="mgmt_config", description="Config management")
    async def mgmt_config(self, interaction: discord.Interaction): await interaction.response.send_message("Config.")
    @app_commands.command(name="mgmt_logs", description="Management logs")
    async def mgmt_logs(self, interaction: discord.Interaction): await interaction.response.send_message("Logs.")
    @app_commands.command(name="mgmt_stats", description="Management stats")
    async def mgmt_stats(self, interaction: discord.Interaction): await interaction.response.send_message("Stats.")
    @app_commands.command(name="mgmt_reload", description="Reload management")
    async def mgmt_reload(self, interaction: discord.Interaction): await interaction.response.send_message("Reloaded.")
    @app_commands.command(name="action_start", description="Action start")
    async def action_start(self, interaction: discord.Interaction): await interaction.response.send_message("Started.")
    @app_commands.command(name="action_stop", description="Action stop")
    async def action_stop(self, interaction: discord.Interaction): await interaction.response.send_message("Stopped.")
    @app_commands.command(name="action_pause", description="Action pause")
    async def action_pause(self, interaction: discord.Interaction): await interaction.response.send_message("Paused.")
    @app_commands.command(name="action_resume", description="Action resume")
    async def action_resume(self, interaction: discord.Interaction): await interaction.response.send_message("Resumed.")
    @app_commands.command(name="action_reset", description="Action reset")
    async def action_reset(self, interaction: discord.Interaction): await interaction.response.send_message("Reset.")
    @app_commands.command(name="status_live", description="Live status")
    async def status_live(self, interaction: discord.Interaction): await interaction.response.send_message("Live.")
    @app_commands.command(name="status_offline", description="Offline status")
    async def status_offline(self, interaction: discord.Interaction): await interaction.response.send_message("Offline.")
    @app_commands.command(name="status_maintenance", description="Maintenance status")
    async def status_maintenance(self, interaction: discord.Interaction): await interaction.response.send_message("Maintenance.")
    @app_commands.command(name="status_update", description="Update status")
    async def status_update(self, interaction: discord.Interaction): await interaction.response.send_message("Updated.")
    @app_commands.command(name="status_info", description="Status info")
    async def status_info(self, interaction: discord.Interaction): await interaction.response.send_message("Status info.")
    @app_commands.command(name="player_add", description="Add player")
    async def player_add(self, interaction: discord.Interaction): await interaction.response.send_message("Player added.")
    @app_commands.command(name="player_remove", description="Remove player")
    async def player_remove(self, interaction: discord.Interaction): await interaction.response.send_message("Player removed.")
    @app_commands.command(name="player_mute", description="Mute player")
    async def player_mute(self, interaction: discord.Interaction): await interaction.response.send_message("Player muted.")
    @app_commands.command(name="player_unmute", description="Unmute player")
    async def player_unmute(self, interaction: discord.Interaction): await interaction.response.send_message("Player unmuted.")
    @app_commands.command(name="player_jail", description="Jail player")
    async def player_jail(self, interaction: discord.Interaction): await interaction.response.send_message("Player jailed.")
    @app_commands.command(name="player_unjail", description="Unjail player")
    async def player_unjail(self, interaction: discord.Interaction): await interaction.response.send_message("Player unjailed.")

async def setup(bot):
    await bot.add_cog(ERLCCommands(bot))
