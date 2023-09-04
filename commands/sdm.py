import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import environ

class Mad(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="mad", description="Apaga todos os chats de um servidor")
    @commands.is_owner()
    async def self_destruction(self, ctx, code: str):
        load_dotenv()
        if code == environ["MAD_CODE"]:
            channels_list = await ctx.guild.fetch_channels()
            await ctx.author.send(f"{len(channels_list)} chats foram deletados!!")
            for channel in channels_list:
                await channel.delete()
        else:
            await ctx.respond("Código errado!!")

    @self_destruction.error
    async def on_application_command_error(ctx, err):
        if isinstance(err, commands.NotOwner):
            await ctx.respond("Você não possui as permissões necessárias")
        else:
            raise err

def setup(bot):
    bot.add_cog(Mad(bot))