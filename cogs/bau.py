import discord
from discord.ext import commands, tasks
import random
from discord import app_commands

class bau(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="bau", description="bau bau bau")
    async def bau(self, interaction: discord.Interaction):
        await interaction.response.send_message(content="bau")
        print(f"{interaction.user.display_name} baued")

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            await self.client.add_cog(bau(self.client))
            return
        except Exception as e:
            return

async def setup(client):
    try:
        await client.add_cog(bau(client))
        return
    except Exception as e:
        return


