from discord.ext import commands
import discord

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Operações aritméticas simples")
    async def calc(self, ctx, expression):
        expression = "".join(expression)
        await ctx.respond(eval(expression))

def setup(bot):
    bot.add_cog(Calculator(bot))