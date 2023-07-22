from random import choice
from discord.ext import commands

class Choice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
           
    def choice(option):
        game = ['Pedra', 'Papel', 'Tesoura']
        bot_choice = choice(game)
        result = None

        if option not in game:
            f'{option} não é uma opção válida.'

        else:
            if bot_choice == option:
                result = 'Empate!'

            elif bot_choice == 'Tesoura' and option == 'Papel' or bot_choice == 'Pedra' and option == 'Tesoura' or bot_choice == 'Papel' and option == 'Pedra':
                result = 'Derrota!'

            elif bot_choice == 'Papel' and option == 'Tesoura' or bot_choice == 'Tesoura' and option == 'Pedra' or bot_choice == 'Pedra' and option == 'Papel':
                result = 'Vitória!'

        output = {
            'bot': bot_choice,
            'player': str(option).capitalize(),
            'result': result
        }
        return output

def setup(bot):
    bot.add_cog(Choice(bot))