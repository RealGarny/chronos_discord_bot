import discord
from discord.ext import commands
import settings
import logging

logger = logging.getLogger("bot")

def main():
    intents = discord.Intents.default()

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        print('-----------------------')

    bot.run(settings.DISCORD_TOKEN, root_logger=True)

if __name__ == "__main__":
    main()