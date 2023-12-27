from discord.ext import commands
from random import choice
import discord

class Chooser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="choose", description="Peça para eu escolher uma opção dentre várias! Separe entre vírgulas!")
    async def chooser(self, ctx, elements):
        options = elements.split(", ")
        chose_option = choice(options)
        await ctx.respond(f"Eu escolho {chose_option}!")

def setup(bot):
    bot.add_cog(Chooser(bot))