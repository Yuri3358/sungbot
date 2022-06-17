from random import choice
from discord.ext import commands

class Choice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
           
    def escolha(option):
        jogo = ['pedra', 'papel', 'tesoura']
        escolha_bot = choice(jogo)
        resultado = 'undefined'

        if option not in jogo:
            f'{option} não é uma opção válida, tente outra vez'

        else:
            if escolha_bot == option:
                resultado = 'Empate!'

            elif escolha_bot == 'tesoura' and option == 'papel' or escolha_bot == 'pedra' and option == 'tesoura' or escolha_bot == 'papel' and option == 'pedra':
                resultado = 'Derrota!'

            elif escolha_bot == 'papel' and option == 'tesoura' or escolha_bot == 'tesoura' and option == 'pedra' or escolha_bot == 'pedra' and option == 'papel':
                resultado = 'Vitória!'

        output = {
            'bot': escolha_bot,
            'jogador': str(option).capitalize(),
            'resultado': resultado
        }
        return output


def setup(bot):
    bot.add_cog(Choice(bot))