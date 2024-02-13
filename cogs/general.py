import discord
from discord.ext import commands

class General(commands.Cog):
    """
    Module handling responses to events and other general functionality

    Functions:
        on_ready:   Outputs message in terminal when the bot comes online
        
    """

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        """ Outputs message in terminal when the bot comes online """
        print(f"{self.bot.user.name} is online.")


# Sets up the cog and adds it to the bot
def setup(bot): bot.add_cog(General(bot))