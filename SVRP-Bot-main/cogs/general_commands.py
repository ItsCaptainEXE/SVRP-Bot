import discord
from discord import app_commands
from discord.ext import commands

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="General help")
    async def help(self, interaction: discord.Interaction):
        await interaction.response.send_message("General help content.")

    @app_commands.command(name="cmds", description="List all commands you can run")
    async def list_cmds(self, interaction: discord.Interaction):
        commands_list = []
        for command in self.bot.tree.get_commands():
            commands_list.append(f"/{command.name} - {command.description}")
        
        # Paginate if needed, for now just join
        output = "\n".join(commands_list)
        if len(output) > 2000:
            output = output[:1997] + "..."
            
        embed = discord.Embed(title="Available Commands", description=output, color=discord.Color.blue())
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @app_commands.command(name="ping", description="Ping")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")
    
    @app_commands.command(name="userinfo", description="User info")
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.response.send_message(f"{member.name} info")
        
    @app_commands.command(name="serverinfo", description="Server info")
    async def serverinfo(self, interaction: discord.Interaction):
        await interaction.response.send_message("Server info")
        
    @app_commands.command(name="avatar", description="Avatar")
    async def avatar(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.response.send_message(f"{member.name}'s avatar")

    @app_commands.command(name="membercount", description="Member count")
    async def membercount(self, interaction: discord.Interaction):
        await interaction.response.send_message("Members: 100")

async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))
