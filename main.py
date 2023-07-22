import discord
from os import listdir
from accesskey import TOKEN

bot = discord.Bot()

for file in listdir('./commands'): 
    if file.endswith('.py'):
        bot.load_extension(f'commands.{file[:-3]}')

@bot.event
async def on_ready():
    print(f'Logged as {bot.user}')

bot.run(TOKEN) 