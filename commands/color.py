from discord.ext import commands
import discord

class ColorSearcher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name="color", description="Descubra qualquer cor a partir do Hex")
    async def color_searcher(self, ctx, hex_code):
        if "#" in hex_code:
            hex_code = hex_code.removeprefix("#")

        color_embed = discord.Embed(title=f"Representação gráfica de `#{hex_code}`", colour=0xfc8403).set_image(url=f"https://singlecolorimage.com/get/{hex_code}/150x150")
        await ctx.respond(embed=color_embed)

def setup(bot):
    bot.add_cog(ColorSearcher(bot))