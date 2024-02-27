import discord
from discord.ext import commands

from utils import *

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

    @commands.Cog.listener()
    async def on_connect(self):
        """ Re-adds views to all active clocks when bot comes back online. """
        for clock_view in get_buttons():
            id, segments, current_ticks, colour, title = clock_view  # unpack view for each clock
            self.bot.add_view(ProgressView(id = id, segments = segments, current_ticks = current_ticks, colour = colour, title = title, reset = True))



# Sets up the cog and adds it to the bot
def setup(bot): bot.add_cog(General(bot))