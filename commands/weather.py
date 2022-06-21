from discord.ext import commands
import discord
from pandas import value_counts
import requests

class Weather(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='tmbr', aliases=['weather', 'tempo'])
    async def metereologia(self, ctx, cidade):

        url = f"https://aerisweather1.p.rapidapi.com/observations/{cidade},br"

        headers = {
            "X-RapidAPI-Key": "63a0471d73msh083fc74704d3a99p133905jsn90e37f8bceec",
            "X-RapidAPI-Host": "aerisweather1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers).json()

        embed_tempo = discord.Embed(
            title = f'Temperatura em {cidade.capitalize()}',
            description = 'Veja o tempo da sua cidade',
            colour = 0xdbd10d
        )
        dados = response["response"]["ob"]

        embed_tempo.add_field(name='Temperatura', value=f"{dados['tempC']}°C", inline=True)
        embed_tempo.add_field(name='Umidade', value=f"{dados['humidity']}%", inline=True)
        embed_tempo.add_field(name='Velocidade dos ventos', value=f"{dados['windSpeedKPH']}km/h", inline=False)
        embed_tempo.set_footer(name='Fonte: Aerisweather // Margem de erro: 1°C para mais ou para menos')
        await ctx.send(embed=embed_tempo)

def setup(bot):
    bot.add_cog(Weather(bot))