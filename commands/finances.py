import discord
from discord.ext import commands
from discord.ext.commands import BucketType, cooldown
from commands.database.currencycore import *

class Finances(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    currency = discord.SlashCommandGroup(name="finances", description="Sistema monetário")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        create_settings(guild.id)

    @currency.command(name="wealth", description="Consulte sua conta bancária")
    async def user_credits(self, ctx):
        await ctx.defer()
        if create_account(ctx.author.id) == 1:
            user_wealth = get_user_wealth(ctx.author.id)
            bank_embed = discord.Embed(title="Informações Bancárias")
            bank_embed.add_field(name="Titular", value=f"<@{ctx.author.id}>")
            bank_embed.add_field(name="Saldo em conta", value=f"{get_currency_symbol(ctx.guild.id)}{user_wealth:.2f}")
            
            await ctx.respond(embed=bank_embed)
        else:
             await ctx.respond("Conta criada, tente novamente!")
    
    @currency.command(name="work", description="Trabalhe para ganhar dinheiro, a diária é corrigida pela inflação")
    @cooldown(1, 86400, BucketType.user)
    async def working(self, ctx):
        await ctx.defer()

        if create_account(ctx.author.id) == 1:
            work(str(ctx.author.id), ctx.guild.id)
            user_credits = get_user_wealth(ctx.author.id)
            wage = get_current_wage(ctx.guild.id)
            
            job_embed = discord.Embed(title="Trabalho realizado!")

            job_embed.add_field(name="Valor recebido", value=f"{get_currency_symbol(ctx.guild.id)}{wage:.2f}")
            job_embed.add_field(name="Saldo da conta", value=f"{get_currency_symbol(ctx.guild.id)}{user_credits:.2f}")

            await ctx.respond(embed=job_embed)
        
        else: 
            await ctx.respond("Conta criada, tente novamente")
            ctx.command.reset_cooldown(ctx)

    @working.error
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.respond("Você só pode trabalhar 1 vez por dia!")
        else:
            raise error

    @currency.command(name="pix", description="Faça transferências para outros membros")
    async def transfer(self, ctx, amount, to: discord.Member):
        await ctx.defer()
        if create_account(ctx.author.id) == 1:
            if float(amount) <= get_user_wealth(ctx.author.id):
            
                transfer_money(str(ctx.author.id), target_account=str(to.id), amount=amount)
                pix_embed = discord.Embed(title="Transferência realizada!")
                pix_embed.add_field(name="Remetente", value=f"<@{ctx.author.id}>", inline=False)
                pix_embed.add_field(name="Destinatário", value=f"<@{to.id}>", inline=False)
                pix_embed.add_field(name="Quantia", value=f"{get_currency_symbol(ctx.guild.id)}{amount}")
            
                await ctx.respond(embed=pix_embed)
            else: 
                await ctx.respond("Saldo insuficiente para a transação!!")
        else:
            await ctx.respond("Conta criada! Tente novamente!")

    @currency.command(name="inflation", description="Ajuste a inflação da moeda, o salário também é ajustado")
    @commands.is_owner()
    async def set_inflation(self, ctx, tax):
        await ctx.defer()
        inflation(tax, ctx.guild.id)
        inflation_output = discord.Embed(title="Inflação ajustada!!")
        inflation_output.add_field(name="Inflação atual", value=f"{get_inflation(ctx.guild.id)}%")
        inflation_output.add_field(name="Diária atual", value=f"{get_currency_symbol(ctx.guild.id)}{get_current_wage(ctx.guild.id):.2f}")
        
        await ctx.respond(embed=inflation_output)

    @currency.command(name="dashboard", description="Informações sobre a moeda corrente")
    async def get_currency_info(self, ctx):
        await ctx.defer()
        info_embed = discord.Embed(title="Informações Monetárias")
        info_embed.add_field(name="Símbolo", value=get_currency_symbol(ctx.guild.id))
        info_embed.add_field(name="Inflação atual", value=f"{get_inflation(ctx.guild.id)}%")
        info_embed.add_field(name="Diária atual", value=f"{get_currency_symbol(ctx.guild.id)}{get_current_wage(ctx.guild.id):.2f}")
        
        await ctx.respond(embed=info_embed)
    
    @currency.command(name="symbol", description="Altere o símbolo da moeda")
    @commands.is_owner()
    async def set_currency_symbol(self, ctx, new_symbol):
        await ctx.defer()
        set_currency_symbol(new_symbol=new_symbol, guild_id=ctx.guild.id)
        await ctx.respond(f"Perfeito! Agora o símbolo da sua moeda será {get_currency_symbol(ctx.guild.id)}")

def setup(bot):
    bot.add_cog(Finances(bot))