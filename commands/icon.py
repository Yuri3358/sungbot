import discord
from discord.ext import commands

class Icon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def icon_profile(self, ctx, *, membicon : discord.User=None):
        if membicon is None:
            membicon = ctx.author
        user_avatar = membicon.display_avatar.url

        embed_icon = discord.Embed(
            title=f'Avatar de {membicon}',
            colour=0x03fc14
        )
        embed_icon.set_image(url=user_avatar)
        await ctx.respond(embed=embed_icon)

def setup(bot):
    bot.add_cog(Icon(bot))