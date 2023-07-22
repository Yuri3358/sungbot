import discord
from discord.ext import commands
from random import randrange

class Rolldice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Jogue um dado personalizado")
    async def roll(self, ctx, faces=6):
        face = randrange(1, int(faces)+1)
        await ctx.respond(f'O dado caiu no **{face}**') 

def setup(bot):
    bot.add_cog(Rolldice(bot))