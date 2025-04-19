import discord
from discord.ext import commands, tasks
import random
from discord import app_commands

class jpnbau(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="jpn-bau", description="bau bau bau")
    async def jpnbau(self, interaction: discord.Interaction):
        await interaction.response.send_message(content="バウバウ！")
        print(f"{interaction.user.display_name} バウエド")

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            await self.client.add_cog(jpnbau(self.client))
            return
        except Exception as e:
            return

async def setup(client):
    try:
        await client.add_cog(jpnbau(client))
        return
    except Exception as e:
        return