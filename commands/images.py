import discord
import requests
from os import environ
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.pages import Paginator, Page

class GoogleSearch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Pesquise imagens no Google Images")
    async def img(self, ctx, search):
        load_dotenv()
        request = requests.get(f"https://serpapi.com/search.json?engine=google_images&q={search}&api_key={environ['SERPAPI_TOKEN']}").json()
        
        images_links = []
        results_pages = []
        for image in request['images_results']:
            images_links.append(image['thumbnail'])
        
        for result_index in range(1, len(images_links) + 1):
            results_pages.append(
                Page(
                    embeds=[
                        discord.Embed(title=f"Resultados da pesquisa sobre `{search.capitalize()}`", color=0xfc8403).set_image(url=images_links[result_index-1])
                    ]
                )
            )

        pag = Paginator(results_pages)
        
        await ctx.response.defer()
        await pag.respond(ctx.interaction)

def setup(bot):
    bot.add_cog(GoogleSearch(bot))