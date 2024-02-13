import discord
from discord import ButtonStyle, Embed
from discord.ui import View, Button

""" Creates Button Views """
class ProgressView(View):  # Create a class called Buttons that subclasses discord.ui.View
    """
    Creates a View with three buttons, one to increase the clock by one, one to decrease it by one, and one to delete it

    Subclasses:
        StepButton:     creates a button to increment or decrement the clock by one
        DeleteButton:   creates a button to delete the clock
    """
    def __init__(self, segments: int, current_ticks: int, colour: str, title: str) -> None:
        super().__init__(timeout = None)  # Makes sure buttons do not timeout

        # Create the embed
        embed = Embed(title = title)
        embed.set_image(url = f"attachment://{colour}_{segments}_{current_ticks}.gif")

        # Create the buttons
        delete_button = self.DeleteButton(label = "Delete", style = ButtonStyle.secondary)

        # Add the buttons to the View class
        self.add_item(delete_button)

    def __repr__(self):
        """ Defines the string representation of the View """
        return f"<ButtonView, title={self.title}>"
    
    # Subclasses for individual buttons
    class DeleteButton(Button):
        """
        Creates a button to delete the clock

        Functions:
            callback:       deletes the clock when button is pressed
        """
        def __init__(self, label: str, style: ButtonStyle, custom_id: str):
            super().__init__(label = label, style = style, custom_id = custom_id)

        async def callback(self, interaction: discord.Interaction): 
            """ Deletes the clock when button is pressed """
            await interaction.message.delete()