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
        self.title = title

        # Create the embed
        embed = Embed(title = title)
        embed.set_image(url = f"attachment://{colour}_{segments}_{current_ticks}.gif")

        # Create the buttons
        increment_button = self.StepButton(label = "Increment", style = ButtonStyle.secondary,
                                            segments = segments, current_ticks = current_ticks, colour = colour, title = title, embed = embed)
        decrement_button = self.StepButton(label = "Decrement", style = ButtonStyle.secondary,
                                            segments = segments, current_ticks = current_ticks, colour = colour, title = title, embed = embed)
        delete_button = self.DeleteButton(label = "Delete", style = ButtonStyle.secondary)

        # Add the buttons to the View class
        self.add_item(increment_button)
        self.add_item(decrement_button)
        self.add_item(delete_button)

    def __repr__(self):
        """ Defines the string representation of the View """
        return f"<ButtonView, title={self.title}>"
    
    # Subclasses for individual buttons
    class StepButton(Button):
        """
        Creates a button to increment or decrement the clock by one

        Functions:
            callback:   creates a new clock changed by one and deletes the old clock when button is pressed
        """
        def __init__(self, label: str, style: ButtonStyle, segments: int, current_ticks: int, colour: str, title: str, embed: Embed):
            self.segments = segments
            self.current_ticks = current_ticks
            self.colour = colour
            self.title = title
            self.embed = embed
            super().__init__(label = label, style = style)

        async def callback(self, interaction: discord.Interaction): # A function called when the button is pressed
            """ Creates a new clock changed by one and deletes the old clock when button is pressed """

            # Determine number of ticks for next clock
            if self.label == "Increment": next_ticks = min(self.current_ticks + 1, self.segments)
            else: next_ticks = max(self.current_ticks - 1, 0)

            # When pressed, send new embed to discord and delete message with this button
            await interaction.response.send_message(file = discord.File(f"resources\clock_images\{self.colour}_{self.segments}_{next_ticks}.gif"),
                            embed = self.embed.set_image(url = f"attachment://{self.colour}_{self.segments}_{next_ticks}.gif"),
                            view = ProgressView(segments = self.segments, current_ticks = next_ticks, colour = self.colour, title = self.title))
            await interaction.message.delete()

    class DeleteButton(Button):
        """
        Creates a button to delete the clock

        Functions:
            callback:       deletes the clock when button is pressed
        """
        def __init__(self, label: str, style: ButtonStyle):
            super().__init__(label = label, style = style)

        async def callback(self, interaction: discord.Interaction): 
            """ Deletes the clock when button is pressed """
            await interaction.message.delete()