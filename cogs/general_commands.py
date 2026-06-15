import discord
from discord.ext import commands

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="cmds", help="List all commands you can run")
    async def list_cmds(self, ctx):
        commands_list = []
        # List prefix commands
        for command in self.bot.commands:
            commands_list.append(f"${command.name} - {command.help}")
        
        # List slash commands
        for command in self.bot.tree.get_commands():
            commands_list.append(f"/{command.name} - {command.description}")
        
        output = "\n".join(commands_list)
        if len(output) > 2000:
            output = output[:1997] + "..."
            
        embed = discord.Embed(title="Available Commands", description=output, color=discord.Color.blue())
        await ctx.send(embed=embed)
    
    @commands.command(name="ping", help="Ping")
    async def ping(self, ctx):
        await ctx.send("Pong!")
    
    @commands.command(name="userinfo", help="User info")
    async def userinfo(self, ctx, member: discord.Member):
        await ctx.send(f"{member.name} info")
        
    @commands.command(name="serverinfo", help="Server info")
    async def serverinfo(self, ctx):
        await ctx.send("Server info")
        
    @commands.command(name="avatar", help="Avatar")
    async def avatar(self, ctx, member: discord.Member):
        await ctx.send(f"{member.name}'s avatar")

    @commands.command(name="membercount", help="Member count")
    async def membercount(self, ctx):
        await ctx.send("Members: 100")

async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))
