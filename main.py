import discord
from discord.ext import commands
from os import listdir, system
from accesskey import TOKEN

bot = commands.Bot(">") #prefixo do bot

for arquivo in listdir('./commands'): #obtêm os nomes de cada arquivo terminado em .py, excluindo a pasta '__pycache__'.
    if arquivo.endswith('.py'):
        bot.load_extension(f'commands.{arquivo[:-3]}')

@bot.event #decorador de uma função que aguarda o evento (tentativa de login)
async def on_ready():
    print(f'Login em {bot.user} efetuado com sucesso!') #mensagem que mostra o sucesso do login cliente-servidor, se aparecer isso, seu planejamento pode seguir normalmente

bot.run(TOKEN) #roda o bot, a constante token exige uma chave de acesso, recomendável em um arquivo modularizado

system('cls') #limpa a linha de comando