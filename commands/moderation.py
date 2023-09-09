import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    moderator = discord.SlashCommandGroup(name="mod", description="Comandos de moderação")

    @moderator.command(name="ban", description="Bane um membro do servidor")
    @commands.has_permissions(ban_members=True)
    async def ban_member(self, ctx, member: discord.Member, reason, messages_days=0):
        ban_embed = discord.Embed(title="Punição realizada!")
        ban_embed.add_field(name="Moderador", value=f"<@{ctx.author.id}>")
        ban_embed.add_field(name="Membro", value=f"<@{member.id}>", inline=False)
        ban_embed.add_field(name="Motivo", value=f"{str(reason).capitalize()}", inline=False)
        ban_embed.add_field(name="Mensagens apagadas", value=f"{messages_days} dia(s)")

        await member.ban(reason=reason, delete_message_days=messages_days)
        await ctx.respond(embed=ban_embed)

    @moderator.command(name="kick", description="Expulsa um membro do servidor")
    @commands.has_permissions(kick_members=True)
    async def kick_member(self, ctx, member: discord.Member, reason):
        kick_embed = discord.Embed(title="Expulsão realizada!")
        kick_embed.add_field(name="Moderador", value=f"<@{ctx.author.id}>", inline=False)
        kick_embed.add_field(name="Membro", value=f"<@{member.id}>", inline=False)
        kick_embed.add_field(name="Motivo", value=f"{str(reason).capitalize()}")

        await member.kick(reason=reason)       
        await ctx.respond(embed=kick_embed)
    
    @kick_member.error
    @ban_member.error
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond("Permissões insuficientes!")

def setup(bot):
    bot.add_cog(Moderation(bot))    