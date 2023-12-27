from discord.ext import commands
import discord

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Operações aritméticas simples")
    async def calc(self, ctx, expression):
        expression = "".join(expression)
        try:
            if "/" in expression or  "*" in expression or "+" in expression or "-" in expression or "**" in expression:
                await ctx.respond(eval(expression))
            else:
                await ctx.respond("Operação Inválida!")
        except SyntaxError:
            await ctx.respond("Operação Inválida")

def setup(bot):
    bot.add_cog(Calculator(bot))