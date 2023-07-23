import discord
from discord.ext import commands
from os import remove
from numpy import linspace, sin as sen, cos, tan
from matplotlib import pyplot as plt

class Plotter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Gera um gráfico em linha de uma função")
    async def plot(self, ctx, function, 
                   highlight_x: discord.Option(float, "Ponto (n) a ser destacado em X, decimal sem vírgulas", required=False), 
                   highlight_y: discord.Option(float, "Ponto (n) ser destacado em Y, decimal sem vírgulas", required=False)):
        x = linspace(-100, 100, 200)
        y = eval(function)
        plt.plot(x, y)

        plt.xlabel("X")
        plt.ylabel("Y")
        plt.axhline(0, color="black", linewidth=1.5)
        plt.axvline(0, color="black", linewidth=1.5)
        plt.xlim(-100, 100)
        plt.ylim(-100, 100)
        plt.grid(True)

        if highlight_x != None and highlight_y != None:
            if highlight_x > 10 or highlight_y > 10:
                highlight_x /= 10
                highlight_y /= 10 
                plt.scatter(highlight_x, highlight_y)
        
        plt.savefig("plot.png")
        plt.close()

        plot_embed = discord.Embed(
            title=f"Gráfico da função f(x)=`{function}`",
            colour=discord.Colour.blue()
        )
        
        with open("plot.png", "rb") as file:
            discord_file = discord.File(file, filename="plot.png")
            plot_embed.set_image(url="attachment://plot.png")
            await ctx.respond(file=discord_file, embed=plot_embed)
        remove("plot.png")

def setup(bot):
    bot.add_cog(Plotter(bot))