import discord
from discord.ext import commands, tasks
import time
import json
import platform
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('bau!'), intents=discord.Intents().all())

        self.cogslist = ["cogs.bau", "cogs.jpnbau", "cogs.info", "cogs.jpninfo", "cogs.yuri", "cogs.ping"]

    async def setup_hook(self):
        for ext in self.cogslist:
            try:
                await self.load_extension(ext)
                print(f"Loaded extension: {ext}")
            except Exception as e:
                print(f"Failed to load extension {ext}: {e}")
     
    async def on_ready(self):
        prfx = (time.strftime("%H:%M:%S UTC", time.gmtime()))
        print(prfx + " Logged in as " + self.user.name)
        print(prfx + " Bot ID " + str(self.user.id))
        print(prfx + " Discord Version " + discord.__version__)
        print(prfx + " Python Version " + str(platform.python_version()))
        synced = await self.tree.sync()
        print(prfx + " " + str(len(synced)) + " Commands Synced")
        member_count = len(self.guilds[0].members)
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"bau bau"))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, discord.Forbidden):
            await ctx.send("I can't send direct messages to this user. Please open your dms on this server")
            return

client = Client()

@client.command()
async def bau(ctx):
    await ctx.send("https://tenor.com/view/fuwamoco-baubau-gif-2478836885696344855")

@client.command()
async def ping(ctx):
    bot_latency = round(client.latency * 1000)
    api_latency = round(client.ws.latency * 1000)
    await ctx.send(f'baubau! <a:fuwabau:1363129865632616448><a:mocobau:1363129818484445235>\n\nbaupp latency: {bot_latency}ms\nBAUPI latency: {api_latency}ms', ephemeral=True)

@client.command()
async def jpn(ctx):
    await ctx.send("バウバウ!")

@client.event
async def on_message(message):
    if 'bau bau' in message.content.lower():
        await message.add_reaction('<:bau:1361315398418698251>')
    if 'fuwawa' in message.content.lower():
        await message.add_reaction('<a:fuwabau:1363129865632616448>')
    if 'mococo' in message.content.lower():
        await message.add_reaction('<a:mocobau:1363129818484445235>')
    if 'pero' in message.content.lower():
        await message.add_reaction('<:perocozy:1363130851595915395>')

    await client.process_commands(message)

client.run(os.getenv("TOKEN"))