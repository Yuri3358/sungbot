import discord
import requests
from discord.ext import commands
from time import strftime

class ExchangeRates(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @discord.slash_command()
    async def dolar(self, ctx, amount=1.00):
        bid = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL").json()
        value = float(bid['USDBRL']['bid'])
        
        embed = discord.Embed(
            title='Cotação do Dólar Americano frente ao Real Brasileiro',
            color=0x03f0fc 
            )
        embed.add_field(name='Valor em Dólares Americanos (USD)', value=f"U${float(amount):.2f}", inline=False)
        embed.add_field(name='Valor em Reais Brasileiros (BRL)', value=f"R${value*float(amount):.2f}", inline=False)
        embed.set_footer(text=f'Dados de {strftime("%d/%m/%Y || %H:%M")}')
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(ExchangeRates(bot))