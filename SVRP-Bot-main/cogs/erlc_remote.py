import discord
from discord import app_commands
from discord.ext import commands, tasks
import os
import requests

class ERLCRemote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_url = "https://api.erlc.gg/v2/server/command"
        self.server_key = os.getenv('ERLC_SERVER_KEY')
        self.recur_message = "Join our server! SVRP - State of Victor Roleplay"
        self.recur_task.start()

    def cog_unload(self):
        self.recur_task.cancel()

    @tasks.loop(minutes=5)
    async def recur_task(self):
        # Sends to ERLC server via API
        self._execute_command(f":h {self.recur_message}")

    def _execute_command(self, cmd_string):
        if not self.server_key:
            return False, "Server key not configured."
        payload = {"command": cmd_string}
        headers = {"server-key": self.server_key, "Content-Type": "application/json"}
        try:
            response = requests.post(self.api_url, json=payload, headers=headers)
            return response.status_code == 200, response.text
        except Exception as e:
            return False, str(e)

    # --- Moderation & Utility ---
    @app_commands.command(name="erlc-kill", description="Kill a player")
    async def kill(self, interaction: discord.Interaction, player: str):
        success, msg = self._execute_command(f":kill {player}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-killlogs", description="View kill logs")
    async def killlogs(self, interaction: discord.Interaction):
        success, msg = self._execute_command(":killlogs")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-hint", description="Temporary hint (:h)")
    async def hint(self, interaction: discord.Interaction, text: str):
        success, msg = self._execute_command(f":h {text}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-broadcast", description="Broadcast message (:m)")
    async def broadcast(self, interaction: discord.Interaction, text: str):
        success, msg = self._execute_command(f":m {text}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-tp", description="TP player to player")
    async def tp(self, interaction: discord.Interaction, p1: str, p2: str):
        success, msg = self._execute_command(f":tp {p1} {p2}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-refresh", description="Refresh player")
    async def refresh(self, interaction: discord.Interaction, player: str):
        success, msg = self._execute_command(f":refresh {player}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-heal", description="Heal player")
    async def heal(self, interaction: discord.Interaction, player: str):
        success, msg = self._execute_command(f":heal {player}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-fire", description="Start fire (House/Brush/Building)")
    async def fire(self, interaction: discord.Interaction, type: str):
        success, msg = self._execute_command(f":startfire {type}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-unwanted", description="Clear wanted status")
    async def unwanted(self, interaction: discord.Interaction, player: str):
        success, msg = self._execute_command(f":unwanted {player}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-prty", description="Priority cooldown timer")
    async def prty(self, interaction: discord.Interaction, seconds: int):
        success, msg = self._execute_command(f":prty {seconds}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-wanted", description="Set wanted status")
    async def wanted(self, interaction: discord.Interaction, player: str):
        success, msg = self._execute_command(f":wanted {player}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-time", description="Set time of day (0-24)")
    async def time(self, interaction: discord.Interaction, hour: int):
        success, msg = self._execute_command(f":time {hour}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-stopfire", description="Stop all fires")
    async def stopfire(self, interaction: discord.Interaction):
        success, msg = self._execute_command(":stopfire")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-bans", description="View banned players")
    async def bans(self, interaction: discord.Interaction):
        success, msg = self._execute_command(":bans")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-logs", description="View executed commands")
    async def logs(self, interaction: discord.Interaction):
        success, msg = self._execute_command(":logs")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-jail", description="Jail player")
    async def jail(self, interaction: discord.Interaction, player: str):
        success, msg = self._execute_command(f":jail {player}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-pt", description="Prohibit PVP timer")
    async def pt(self, interaction: discord.Interaction, seconds: int):
        success, msg = self._execute_command(f":pt {seconds}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-respawn", description="Respawn player")
    async def respawn(self, interaction: discord.Interaction, player: str):
        success, msg = self._execute_command(f":respawn {player}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-kick", description="Kick player")
    async def kick(self, interaction: discord.Interaction, player: str, reason: str):
        success, msg = self._execute_command(f":kick {player} {reason}")
        await interaction.response.send_message(msg)

    # --- Administration ---
    @app_commands.command(name="erlc-weather", description="Change weather")
    async def weather(self, interaction: discord.Interaction, type: str):
        success, msg = self._execute_command(f":weather {type}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-unmod", description="Revoke mod")
    async def unmod(self, interaction: discord.Interaction, player: str):
        success, msg = self._execute_command(f":unmod {player}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-unban", description="Unban player")
    async def unban(self, interaction: discord.Interaction, player: str):
        success, msg = self._execute_command(f":unban {player}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-mod", description="Grant mod")
    async def mod(self, interaction: discord.Interaction, player: str):
        success, msg = self._execute_command(f":mod {player}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-ban", description="Ban player")
    async def ban(self, interaction: discord.Interaction, player: str):
        success, msg = self._execute_command(f":ban {player}")
        await interaction.response.send_message(msg)

    # --- Owner ---
    @app_commands.command(name="erlc-admin", description="Grant admin")
    async def admin(self, interaction: discord.Interaction, player: str):
        success, msg = self._execute_command(f":admin {player}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-unadmin", description="Revoke admin")
    async def unadmin(self, interaction: discord.Interaction, player: str):
        success, msg = self._execute_command(f":unadmin {player}")
        await interaction.response.send_message(msg)

    @app_commands.command(name="erlc-shutdown", description="Shutdown server")
    async def shutdown(self, interaction: discord.Interaction):
        success, msg = self._execute_command(":shutdown")
        await interaction.response.send_message(msg)

    @app_commands.command(name="set-recur-message", description="Set recurring hint message")
    async def set_recur(self, interaction: discord.Interaction, message: str):
        self.recur_message = message
        await interaction.response.send_message(f"Recurring ERLC hint updated to: {message}")

async def setup(bot):
    await bot.add_cog(ERLCRemote(bot))
