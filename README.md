# DoskBot
A Discord Bot to make progress clocks for the Blades in the Dark roleplaying game

## Installing and Creating Bot
To get started with this project, follow these steps:
1. Clone the repository using https://github.com/ZebSK/Blades-Discord-Bot.git
2. Install dependencies using `pip install requirements.txt`
3. Create a Discord Bot using the Discord Developer Portal at https://discord.com/developers/applications. From here, generate a token for your bot and a link to add it to a discord server
5. Rename .env.example to .env and replace the token value with your own
6. Add the bot to your server and run the run.py file. It may take a while for Discord to add the commands to the bot the first time you run the code

## Usage
### `/progress_clock` 
Generates a 4, 6, or 8 segment clock in either red or green. Title and starting ticks are customisable

![](resources\demo_images\demo_progress_clock_1.gif)

Increment, decrement and delete buttons allow the clock to be edited

![](resources\demo_images\demo_progress_clock_2.gif)