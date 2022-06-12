from discord.ext import commands
import discord

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='calc')
    async def calculate(self, ctx, *expression):
        expression = "".join(expression)
        await ctx.send(eval(expression))

def setup(bot):
    bot.add_cog(Calculator(bot))