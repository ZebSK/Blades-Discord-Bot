import discord
from discord.ext import commands

from .utils import *

class ClockCommands(commands.Cog):
    """
    Module handling commands related to creating clocks

    Functions:
        progress_clock:     creates an embed with the desired clock and ability to increment, decrement or delete the clock

    """
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def testing(self, ctx):
        await print("jdn")

    @discord.slash_command(description = "Make a singular progress clock")
    async def progress_clock(self, ctx: discord.ApplicationContext,
                    title: discord.Option(str, required = False, default = "Clock", description = "title of clock"), # type: ignore
                    segments: discord.Option(int, required = False, default = 6, choices = [4, 6, 8], description= "number of segments"), # type: ignore
                    ticks: discord.Option(int, required = False, default = 0, choices = list(range(9)), description = "number of starting ticks"), # type: ignore
                    colour: discord.Option(str, required = False, default = "red", choices = ["red", "green"], description = "colour of clock")): # type: ignore
        """
        Creates an embed with the desired clock and buttons to increment, decrement or delete the clock

        Parameters:
            ctx (discord.ApplicationContext):   the invocation context of the command eg. which channel the command was sent to
            title (str):                        the title of the embed
            segments (int):                     the number of segments on the clock
                                                    segments = 4, 6, 8
            ticks (int):                        the number of ticks on the clock
                                                    0 >= ticks >= segments
            colour (str):                       the colour of the clock
                                                    colour = 'red', 'green'
        """
        
        # Check inputs are valid
        if ticks > segments: ticks = segments

        # Create the embed
        embed = discord.Embed(title = title)
        embed.set_image(url = f"attachment://{colour}_{segments}_{ticks}.gif")

        # Sends the embed to discord, and attaches the View class that contains the buttons
        await ctx.respond(file = discord.File(f"resources\clock_images\{colour}_{segments}_{ticks}.gif"), embed = embed,
                          view = ProgressView(segments = segments, current_ticks = ticks, colour = colour, title = title))


# Sets up the cog and adds it to the bot
def setup(bot): bot.add_cog(ClockCommands(bot))