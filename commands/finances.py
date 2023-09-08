import discord
from discord.ext import commands
from discord.ext.commands import BucketType, cooldown
from commands.database.currencyops import *

class Finances(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    currency = discord.SlashCommandGroup(name="finances", description="Sistema monetário")

    @currency.command(name="register")
    async def register_user(self, ctx):
        create_account(ctx.author.id)
        await ctx.respond(f"Criar conta para <@{ctx.author.id}>")
    
    @currency.command(name="wealth")
    async def user_credits(self, ctx):
        user_wealth = get_user_wealth(ctx.author.id)
        bank_embed = discord.Embed(title="Informações Bancárias")
        bank_embed.add_field(name="Titular", value=f"<@{ctx.author.id}>")
        bank_embed.add_field(name="Saldo em conta", value=f"${user_wealth:.2f}")
        
        await ctx.respond(embed=bank_embed)
    
    @currency.command(name="work")
    @cooldown(1, 86400, BucketType.user)
    async def working(self, ctx):
        work_data = work(str(ctx.author.id))
        user_credits = get_user_wealth(ctx.author.id)

        job_embed = discord.Embed(title="Trabalho realizado!")
        job_embed.add_field(name="Valor recebido", value=f"${work_data:.2f}")
        job_embed.add_field(name="Saldo da conta", value=f"${user_credits:.2f}")

        await ctx.respond(embed=job_embed)

    @working.error
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.respond("Você só pode trabalhar 1 vez por dia!")
        else:
            raise error

    @currency.command(name="pix")
    async def transfer(self, ctx, amount, to: discord.Member):
        if float(amount) <= get_user_wealth(ctx.author.id):
            transfer_money(str(ctx.author.id), target_account=str(to.id), amount=amount)
            pix_embed = discord.Embed(title="Transferência realizada!")
            pix_embed.add_field(name="Rementente", value=f"<@{ctx.author.id}>", inline=False)
            pix_embed.add_field(name="Destinatário", value=f"<@{to.id}>", inline=False)
            pix_embed.add_field(name="Quantia", value=f"{amount}")
            await ctx.respond(embed=pix_embed)
        else: 
            await ctx.respond("Saldo insuficiente para a transação!!")

    @currency.command(name="inflation")
    @commands.is_owner()
    async def set_inflation(self, ctx, tax):
        inflation(tax)
        await ctx.defer()
        await ctx.respond(f"Inflação ajustada para {tax}% \nDiária ajustada para ${get_current_wage():.2f}")
        
def setup(bot):
    bot.add_cog(Finances(bot))