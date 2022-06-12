import discord
from discord.ext import commands
from time import monotonic

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def latencia(self, ctx):
        tempo_inicial = monotonic()
        msg = await ctx.send('Pong!')
        ping = (monotonic() - tempo_inicial) * 1000
        await msg.edit(content=f"Pong! **{ping:.0f}**ms")

def setup(bot):
    bot.add_cog(Ping(bot))