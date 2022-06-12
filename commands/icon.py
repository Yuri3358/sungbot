import discord
from discord.ext import commands

class Icon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='avatar', aliases=['icon', 'fotinho'])
    async def icon_profile(self, ctx, *, membicon : discord.User=None):
        if membicon is None:
            membicon = ctx.author
        user_avatar = membicon.avatar_url

        embed_icon = discord.Embed(
            title=f'Avatar de {membicon}'
        )
        embed_icon.set_image(url=user_avatar)
        await ctx.send(embed=embed_icon)

def setup(bot):
    bot.add_cog(Icon(bot))