import discord
from discord.ext import commands
from discord.ext.commands import BucketType, cooldown
from commands.database.currencyops import *

currency_symbol = "K$"

class Finances(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    currency = discord.SlashCommandGroup(name="finances", description="Sistema monetário")

    @currency.command(name="register", description="Abra sua conta bancária")
    async def register_user(self, ctx):
        create_account(ctx.author.id)
        await ctx.respond(f"Criar conta para <@{ctx.author.id}>")

    @currency.command(name="wealth", description="Consulte sua conta bancária")
    async def user_credits(self, ctx):
        user_wealth = get_user_wealth(ctx.author.id)
        bank_embed = discord.Embed(title="Informações Bancárias")
        bank_embed.add_field(name="Titular", value=f"<@{ctx.author.id}>")
        bank_embed.add_field(name="Saldo em conta", value=f"{currency_symbol}{user_wealth:.2f}")
        
        await ctx.respond(embed=bank_embed)
    
    @currency.command(name="work", description="Trabalhe para ganhar dinheiro, a diária é corrigida pela inflação")
    @cooldown(1, 86400, BucketType.user)
    async def working(self, ctx):
        work_data = work(str(ctx.author.id))
        user_credits = get_user_wealth(ctx.author.id)

        job_embed = discord.Embed(title="Trabalho realizado!")
        job_embed.add_field(name="Valor recebido", value=f"{currency_symbol}{work_data:.2f}")
        job_embed.add_field(name="Saldo da conta", value=f"{currency_symbol}{user_credits:.2f}")

        await ctx.respond(embed=job_embed)

    @working.error
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.respond("Você só pode trabalhar 1 vez por dia!")
        else:
            raise error

    @currency.command(name="pix", description="Faça transferências para outros membros")
    async def transfer(self, ctx, amount, to: discord.Member):
        if float(amount) <= get_user_wealth(ctx.author.id):
            transfer_money(str(ctx.author.id), target_account=str(to.id), amount=amount)
            pix_embed = discord.Embed(title="Transferência realizada!")
            pix_embed.add_field(name="Rementente", value=f"<@{ctx.author.id}>", inline=False)
            pix_embed.add_field(name="Destinatário", value=f"<@{to.id}>", inline=False)
            pix_embed.add_field(name="Quantia", value=f"{currency_symbol}{amount}")
            await ctx.respond(embed=pix_embed)
        else: 
            await ctx.respond("Saldo insuficiente para a transação!!")

    @currency.command(name="inflation", description="Ajuste a inflação da moeda, o salário também é ajustado")
    @commands.is_owner()
    async def set_inflation(self, ctx, tax):
        inflation(tax)
        inflation_output = discord.Embed(title="Inflação ajustada!!")
        inflation_output.add_field(name="Inflação atual", value=f"{get_inflation()}%")
        inflation_output.add_field(name="Diária atual", value=f"{currency_symbol}{get_current_wage():.2f}")
        
        await ctx.defer()
        await ctx.respond(embed=inflation_output)

    @currency.command(name="dashboard", description="Informações sobre a moeda corrente")
    async def get_currency_info(self, ctx):
        info_embed = discord.Embed(title="Informações monetárias")
        info_embed.add_field(name="Símbolo", value=currency_symbol)
        info_embed.add_field(name="Inflação atual", value=f"{get_inflation()}%")
        info_embed.add_field(name="Diária atual", value=f"{currency_symbol}{get_current_wage():.2f}")
        
        await ctx.respond(embed=info_embed)

def setup(bot):
    bot.add_cog(Finances(bot))