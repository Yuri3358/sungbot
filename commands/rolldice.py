import asyncio
import discord
from discord.ext import commands
from random import randrange

class Rolldice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['rnumber', 'randint', 'dice', 'roll', 'rolldice'])
    async def dado(self, ctx, faces=6):
        msg = await ctx.send('Rolando o dado... :game_die:')
        await asyncio.sleep(2)
        face = randrange(1, int(faces)+1)
        await msg.edit(content=f'O dado caiu no **{face}**') 

def setup(bot):
    bot.add_cog(Rolldice(bot))