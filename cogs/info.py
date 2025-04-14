import discord
from discord.ext import commands, tasks
import random
from discord import app_commands

class info(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="info", description="information about baubot")
    async def info(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="baubot v1.1",
            description=(''
            'baubot is a discord application written in python using discord.py inspired by the hololive duo fuwamoco created by @zaynedrift. the application is hosted locally from Zaynes localhost.'
            '\nclick [here](https://github.com/Zaynedrift/baubot) for the github repository.'
            '\n(sorry if latency is high, this application is hosted locally from australia.)')
        )
        await interaction.response.send_message(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            await self.client.add_cog(info(self.client))
            return
        except Exception as e:
            return

async def setup(client):
    try:
        await client.add_cog(info(client))
        return
    except Exception as e:
        return