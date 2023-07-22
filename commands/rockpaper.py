import discord
from discord.ext import commands
from .choices import Choice

class SelectBox(discord.ui.View): 
    @discord.ui.select(
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(
                label="Pedra"
            ),
            discord.SelectOption(
                label="Papel"
            ),
            discord.SelectOption(
                label="Tesoura"
            )
        ]
    )
    async def callback(self, select, interaction): 
        manager = Choice
        outputs = manager.choice(option=select.values[0])
        await interaction.response.send_message(f"Eu escolhi: {outputs['bot']} \nVocê escolheu: {outputs['player']} \nResultado: {outputs['result']}")

class Jokenpo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @discord.slash_command(description="Jogue jokenpo tradicional")
    async def jokenpo(self, ctx):
        await ctx.respond("Pedra, papel ou tesoura?", view=SelectBox())

def setup(bot):
    bot.add_cog(Jokenpo(bot))