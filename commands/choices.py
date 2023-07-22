from random import choice
from discord.ext import commands

class Choice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
           
    def escolha(option):
        jogo = ['Pedra', 'Papel', 'Tesoura']
        escolha_bot = choice(jogo)
        resultado = None

        if option not in jogo:
            f'{option} não é uma opção válida, tente outra vez'

        else:
            if escolha_bot == option:
                resultado = 'Empate!'

            elif escolha_bot == 'Tesoura' and option == 'Papel' or escolha_bot == 'Pedra' and option == 'Tesoura' or escolha_bot == 'Papel' and option == 'Pedra':
                resultado = 'Derrota!'

            elif escolha_bot == 'Papel' and option == 'Tesoura' or escolha_bot == 'Tesoura' and option == 'Pedra' or escolha_bot == 'Pedra' and option == 'Papel':
                resultado = 'Vitória!'

        output = {
            'bot': escolha_bot,
            'jogador': str(option).capitalize(),
            'resultado': resultado
        }
        return output


def setup(bot):
    bot.add_cog(Choice(bot))