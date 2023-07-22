import discord
from os import listdir, environ
from dotenv import load_dotenv
load_dotenv()

bot = discord.Bot()

for file in listdir('./commands'): 
    if file.endswith('.py'):
        bot.load_extension(f'commands.{file[:-3]}')

@bot.event
async def on_ready():
    activity = discord.Game(name="Servindo aos meus usuários")
    await bot.change_presence(activity=activity)
    print(f'Logged as {bot.user}')

bot.run(environ["TOKEN"]) 