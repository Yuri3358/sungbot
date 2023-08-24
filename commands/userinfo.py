import discord 
from discord.ext import commands
from datetime import datetime

class UserSearch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name="userinfo", description="Obtenha informações de usuários do Discord")
    async def user_info(self, ctx, user_id: discord.User):

        account_creation = datetime.strftime(user_id.created_at, "%d-%m-%Y (%H:%M:%S)")
        infos_embed = discord.Embed(title=f"Informações de {str(user_id).removesuffix('#0')}", color=0xf0a000)
        infos_embed.add_field(name="Nome de usuário/apelido", value=user_id.display_name, inline=False)
        infos_embed.add_field(name="Data de chegada", value=account_creation, inline=False)

        infos_embed.set_thumbnail(url=user_id.display_avatar.url)
        await ctx.respond(embed=infos_embed)

def setup(bot):
    bot.add_cog(UserSearch(bot))