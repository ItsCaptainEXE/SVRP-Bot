import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv
import threading
import http.server
import socketserver

# Load environment variables
load_dotenv()

# --- Health Check Server ---
class HealthCheckHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is healthy")

    def log_message(self, format, *args):
        return # Suppress logs to keep output clean

def run_health_check_server():
    port = int(os.environ.get("PORT", 8080))
    with socketserver.TCPServer(("", port), HealthCheckHandler) as httpd:
        print(f"Health check server running on port {port}")
        httpd.serve_forever()

# Bot Setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="$", intents=intents)

# Load Cogs
async def load_extensions():
    # Use the directory where main.py resides to find the 'cogs' folder
    cogs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cogs')
    for filename in os.listdir(cogs_dir):
        if filename.endswith('.py'):
            # Load the extension using the module path
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')
    await load_extensions()

# Command to manually sync slash commands
@bot.command()
async def sync(ctx):
    await bot.tree.sync()
    await ctx.send("Commands synced!")

# Global Error Handler
@bot.event
async def on_command_error(ctx, error):
    # Log to LOG_CHANNEL_ERRORS and send user message
    print(f"Error: {error}")
    await ctx.send("An unexpected error occurred.")

# Run Bot
if __name__ == "__main__":
    # Start health check server in a separate thread
    health_thread = threading.Thread(target=run_health_check_server, daemon=True)
    health_thread.start()
    bot.run(os.getenv('DISCORD_TOKEN'))
