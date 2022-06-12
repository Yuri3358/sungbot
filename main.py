import discord
from discord.ext import commands
from os import listdir, system
from accesskey import TOKEN


bot = commands.Bot(">")

for arquivo in listdir('./commands'):
    if arquivo.endswith('.py'):
        bot.load_extension(f'commands.{arquivo[:-3]}')

@bot.event 
async def on_ready():
    print(f'Login em {bot.user} efetuado com sucesso!')

bot.run(TOKEN)

system('cls')