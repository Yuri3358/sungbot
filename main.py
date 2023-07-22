import discord
from os import listdir
from accesskey import TOKEN

bot = discord.Bot()

for arquivo in listdir('./commands'): 
    if arquivo.endswith('.py'):
        bot.load_extension(f'commands.{arquivo[:-3]}')

@bot.event
async def on_ready():
    print(f'Login em {bot.user} efetuado com sucesso!')

bot.run(TOKEN) 