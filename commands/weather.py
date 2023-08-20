import discord
from discord.ext import commands
from requests import get
from dotenv import load_dotenv
from os import environ

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(description="Mostra informações meteorológicas sobre a cidade pesquisada")
    async def weather(self, ctx, city):
        load_dotenv()
        header = {"accept": "application/json"}
        request = get(f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey={environ['TOMORROW_TOKEN']}", headers=header).json()
        data = request['data']['values']
        color = ""
        weather_data = {
            "temperature": data["temperature"],
            "wind_speed": data["windSpeed"],
            "humidity": data["humidity"],
            "rain_prob": data["precipitationProbability"]
        }

        if weather_data['temperature'] > 17:
            color = 0xd9a20d
        else:
            color = 0x0dbad9

        weather_embed = discord.Embed(title=f"Informações Meteorológicas de `{city.capitalize()}`", color=color)
        weather_embed.add_field(name="Temperatura", value=f"{weather_data['temperature']}ºC")
        weather_embed.add_field(name="Umidade do Ar", value=f"{weather_data['humidity']}%")
        weather_embed.add_field(name="Velocidade dos Ventos", value=f"{weather_data['wind_speed']}km/h")
        weather_embed.add_field(name="Probabilidade de Chuva", value=f"{weather_data['rain_prob']}%")
        weather_embed.set_footer(text="Dados fornecidos por https://tomorrow.io")

        await ctx.respond(embed=weather_embed)

def setup(bot):
    bot.add_cog(Weather(bot))