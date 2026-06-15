import discord
from discord import app_commands
from discord.ext import commands
from bot.config_manager import update_config_key, load_config
from bot.utils import create_embed

class SetupCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    setup_group = app_commands.Group(name="setup", description="Setup bot channels")
    post_group = app_commands.Group(name="post", description="Post embeds")

    @setup_group.command(name="channel", description="Set channel for a specific purpose")
    @app_commands.describe(purpose="rules, info, faq, or server_info", channel="The channel to set")
    @app_commands.choices(purpose=[
        app_commands.Choice(name="Rules", value="rules_channel_id"),
        app_commands.Choice(name="Info", value="info_channel_id"),
        app_commands.Choice(name="FAQ", value="faq_channel_id"),
        app_commands.Choice(name="Server Info", value="server_info_channel_id"),
    ])
    async def set_channel(self, interaction: discord.Interaction, purpose: app_commands.Choice[str], channel: discord.TextChannel):
        update_config_key(purpose.value, channel.id)
        await interaction.response.send_message(f"Set {purpose.name} channel to {channel.mention}")

    @post_group.command(name="embed", description="Post an embed to a configured channel")
    @app_commands.describe(purpose="rules, info, faq, or server_info")
    @app_commands.choices(purpose=[
        app_commands.Choice(name="Rules", value="rules_channel_id"),
        app_commands.Choice(name="Info", value="info_channel_id"),
        app_commands.Choice(name="FAQ", value="faq_channel_id"),
        app_commands.Choice(name="Server Info", value="server_info_channel_id"),
    ])
    async def post_embed(self, interaction: discord.Interaction, purpose: app_commands.Choice[str]):
        config = load_config()
        channel_id = config.get(purpose.value)
        
        if not channel_id:
            await interaction.response.send_message(f"Channel for {purpose.name} not set. Use /setup channel first.", ephemeral=True)
            return
            
        channel = self.bot.get_channel(channel_id)
        if not channel:
            await interaction.response.send_message("Channel not found. It might have been deleted.", ephemeral=True)
            return
            
        embed = create_embed(title=purpose.name, description=f"Content for {purpose.name} goes here.")
        await channel.send(embed=embed)
        await interaction.response.send_message(f"Posted {purpose.name} embed to {channel.mention}")

async def setup(bot):
    await bot.add_cog(SetupCommands(bot))
