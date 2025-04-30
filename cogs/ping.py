import discord
from discord.ext import commands
import asyncio
from discord import app_commands

class ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="ping", description="Check the bot and API latency.")
    async def ping(self, interaction: discord.Interaction):
        bot_latency = round(self.client.latency * 1000)
        api_latency = round(self.client.ws.latency * 1000)
        await interaction.response.send_message(content=f'baubau! <a:fuwabau:1363129865632616448><a:mocobau:1363129818484445235>\n\nbaupp latency: {bot_latency}ms\nBAUPI latency: {api_latency}ms', ephemeral=True)
        print(f"App latency: {bot_latency}ms\nAPI latency: {api_latency}ms")
    
    @commands.Cog.listener()
    async def on_ready(self):
        try:
            await self.client.add_cog(ping(self.client))
            return
        except Exception as e:
            return

async def setup(client):
    try:
        await client.add_cog(ping(client))
        return
    except Exception as e:
        return

