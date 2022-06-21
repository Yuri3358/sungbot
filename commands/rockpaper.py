import discord
from discord.ext import commands
from .choices import Choice

class Rockscissors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(nome='pedrapapel', aliases=['rc', 'ppt'])
    async def rps(self, ctx, option):     
        choice = Choice
        valores = choice.escolha(option=option)

        embed = discord.Embed(
            title = 'Papel, pedra ou tesoura'
        )
        embed.add_field(name='Jogador', value=valores['jogador'])
        embed.add_field(name='Bot', value=valores['bot'], inline=True)
        embed.add_field(name='Resultado', value=valores['resultado'], inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Rockscissors(bot))