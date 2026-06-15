import discord
from discord import app_commands
from discord.ext import commands
from bot.svrp_api import send_api_request

class ManagementCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="server-lock", description="Lock ERLC server")
    async def server_lock(self, interaction: discord.Interaction):
        # Implementation: Assuming an endpoint exists
        data = send_api_request("POST", "server/lock")
        if data:
            await interaction.response.send_message("Locked ERLC server successfully.")
        else:
            await interaction.response.send_message("Failed to lock server.")

    @app_commands.command(name="server-unlock", description="Unlock ERLC server")
    async def server_unlock(self, interaction: discord.Interaction):
        # Implementation: Assuming an endpoint exists
        data = send_api_request("POST", "server/unlock")
        if data:
            await interaction.response.send_message("Unlocked ERLC server successfully.")
        else:
            await interaction.response.send_message("Failed to unlock server.")

    @app_commands.command(name="set-map", description="Set ERLC map")
    async def set_map(self, interaction: discord.Interaction, map_name: str):
        # Implementation: Assuming an endpoint exists
        data = send_api_request("POST", f"server/map/{map_name}")
        if data:
            await interaction.response.send_message(f"Map set to {map_name}")
        else:
            await interaction.response.send_message("Failed to set map.")

    @app_commands.command(name="set-weather", description="Set ERLC weather")
    async def set_weather(self, interaction: discord.Interaction, weather: str):
        # Implementation: Assuming an endpoint exists
        data = send_api_request("POST", f"server/weather/{weather}")
        if data:
            await interaction.response.send_message(f"Weather set to {weather}")
        else:
            await interaction.response.send_message("Failed to set weather.")

    @app_commands.command(name="announcement", description="Send server announcement")
    async def announcement(self, interaction: discord.Interaction, message: str):
        # Discord server announcement logic
        await interaction.channel.send(f"@everyone Announcement: {message}")
        await interaction.response.send_message("Announcement sent.", ephemeral=True)

    @app_commands.command(name="role-add", description="Add role to user")
    async def role_add(self, interaction: discord.Interaction, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await interaction.response.send_message(f"Added {role.name} to {member.name}")

    @app_commands.command(name="role-remove", description="Remove role from user")
    async def role_remove(self, interaction: discord.Interaction, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)
        await interaction.response.send_message(f"Removed {role.name} from {member.name}")

    @app_commands.command(name="create-role", description="Create a new role")
    async def create_role(self, interaction: discord.Interaction, name: str):
        await interaction.guild.create_role(name=name)
        await interaction.response.send_message(f"Created role {name}")

    @app_commands.command(name="delete-role", description="Delete a role")
    async def delete_role(self, interaction: discord.Interaction, role: discord.Role):
        await role.delete()
        await interaction.response.send_message(f"Deleted role {role.name}")

    @app_commands.command(name="set-nick", description="Set nickname")
    async def set_nick(self, interaction: discord.Interaction, member: discord.Member, nick: str):
        await member.edit(nick=nick)
        await interaction.response.send_message(f"Nickname set")

async def setup(bot):
    await bot.add_cog(ManagementCommands(bot))
