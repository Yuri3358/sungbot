import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name='ping', description="Retorna a latência entre a usuário e o cliente")
    async def latency(self, ctx):
        ping = self.bot.latency*100
        await ctx.respond(content=f"Pong! **{ping:.2f}**ms")

def setup(bot):
    bot.add_cog(Ping(bot))