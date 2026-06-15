import discord

def create_embed(title, description, color=discord.Color.blue()):
    embed = discord.Embed(title=title, description=description, color=color)
    embed.set_footer(text="Bot developed by @itscaptainexe | SVRP | Assistant")
    return embed
