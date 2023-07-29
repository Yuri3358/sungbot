import discord
from discord.ext import commands
from requests import get

class Cep(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name="cepinfo", description="Informações a partir de CEP")
    async def cep_info(self, ctx, cep):
        req = get(f"https://cep.awesomeapi.com.br/json/{cep}").json()
        if "code" in req:
            await ctx.respond("CEP inválido!")
        else:
            cep_embed = discord.Embed(title=f"Informações do CEP {cep}", color=0xd98518)
            cep_embed.add_field(name="Endereço", value=req["address"], inline=True)
            cep_embed.add_field(name="Bairro", value=req["district"], inline=True)
            cep_embed.add_field(name="Cidade", value=req["city"], inline=True)
            cep_embed.add_field(name="Estado", value=req["state"], inline=True)
            cep_embed.add_field(name="DDD", value=req["ddd"], inline=True)
            cep_embed.add_field(name="Registro IBGE", value=req["city_ibge"], inline=True)
            await ctx.respond(embed=cep_embed)

def setup(bot):
    bot.add_cog(Cep(bot))