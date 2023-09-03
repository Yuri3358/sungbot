import discord
from discord.ext import commands
from os import listdir, environ
from dotenv import load_dotenv
load_dotenv()

bot = discord.Bot()

for file in listdir('./commands'): 
    if file.endswith('.py'):
        bot.load_extension(f'commands.{file[:-3]}')

@bot.event
async def on_ready():
    discord.Activity(type=discord.ActivityType.listening, name="meus usuários")
    print(f'Logged as {bot.user}')
    
@bot.event
async def on_application_command_error(ctx, err):
    if isinstance(err, commands.NotOwner):
        await ctx.respond("Você não possui as permissões necessárias")
    else:
        raise err

bot.run(environ["TOKEN"])