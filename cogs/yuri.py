import discord
from discord.ext import commands, tasks
import random
from discord import app_commands
import requests
import xml.etree.ElementTree as ET

class yuri(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    
    def search_safebooru(self, tags, limit=1, randomize=True):
        try:
            url = "https://safebooru.org/index.php"
            params = {
                "page": "dapi",
                "s": "post",
                "q": "index",
                "tags": "+".join(tags),
                "limit": 100
            }

            response = requests.get(url, params=params)
            response.raise_for_status()

            root = ET.fromstring(response.content)
            posts = root.findall("post")

            if not posts:
                return []

            if randomize:
                post = random.choice(posts)
                return [post]
            else:
                return posts[:limit]

        except requests.exceptions.RequestException as e:
            print(f"[Safebooru Request Error] {e}")
            return []
        except ET.ParseError as e:
            print(f"[Safebooru XML Parse Error] {e}")
            return []

    @app_commands.command(name="yuri", description="use command for yuri :3")
    async def yuri(self, interaction: discord.Interaction):
        await interaction.response.defer()

        tags = ["yuri"]
        posts = self.search_safebooru(tags)

        if posts:
            post = posts[0]
            image_url = post.attrib['file_url']
            post_link = f"https://safebooru.org/index.php?page=post&s=view&id={post.attrib['id']}"

            embed = discord.Embed(title="Yuri! baubaubaubau :3", url=post_link)
            embed.set_image(url=image_url)
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send("No yuri found :c")

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            await self.client.add_cog(yuri(self.client))
            return
        except Exception as e:
            return

async def setup(client):
    try:
        await client.add_cog(yuri(client))
        return
    except Exception as e:
        return