import discord
from discord.ext import commands, tasks
import random
from discord import app_commands

class jpninfo(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="jpn-info", description="バウボットに関する情報")
    async def jpninfo(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="バウボット v1.1.2",
            description=(''
            '私はバウボット！ :3'
            '\n[リポジトリ](https://github.com/Zaynedrift/baubot)')
        )
        await interaction.response.send_message(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            await self.client.add_cog(jpninfo(self.client))
            return
        except Exception as e:
            return

async def setup(client):
    try:
        await client.add_cog(jpninfo(client))
        return
    except Exception as e:
        return