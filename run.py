import discord
from dotenv import dotenv_values

from config import Settings as s

# Fetch the bot token from the .env file
env = dotenv_values(".env")
token = env["TOKEN"]

# Create a new instance of the bot class and load cogs (modules)
bot = discord.Bot()
for cog in s.cogs_list: bot.load_extension(f"cogs.{cog}")

# Run the bot with the token
try: bot.run(token)
except KeyboardInterrupt: print(f"{bot.user.name} shutting down")