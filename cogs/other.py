import discord
from discord.ext import commands


class OtherCommands(commands.Cog):
    """
    Module handling all random, fun, and unrelated commands. 

    Functions:
        box_ghost:  sends box ghost to the current chat

    """
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Box Ghost says hi!")
    async def box_ghost(self, ctx: discord.ApplicationContext):
        """ Sends box ghost to the current chat """
        # Create the embed
        embed = discord.Embed()
        filename = "box_ghost"
        embed.set_image(url = f"attachment://{filename}.gif")

        # Sends the embed to discord, and attaches the View class that contains the button
        await ctx.respond(file = discord.File(f"resources\other_images\{filename}.gif"), embed = embed)



# Sets up the cog and adds it to the bot
def setup(bot): bot.add_cog(OtherCommands(bot))