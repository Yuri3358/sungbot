import discord
from discord.ext import commands
from os import remove
from numpy import linspace
from matplotlib import pyplot as plt

class Plotter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Gera um gráfico em linha de uma função")
    async def plot(self, ctx, function):
        x = linspace(0, 10, 30)
        y = eval(function)
        plt.plot(x, y)
        plt.grid(True)
        plt.savefig("plot.png")
        plt.close()

        plot_embed = discord.Embed(
            title=f"Gráfico da função f(x)={function}"
        )
        
        with open("plot.png", "rb") as file:
            discord_file = discord.File(file, filename="plot.png")
            plot_embed.set_image(url="attachment://plot.png")
            await ctx.respond(file=discord_file, embed=plot_embed)
        remove("plot.png")

def setup(bot):
    bot.add_cog(Plotter(bot))