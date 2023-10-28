import discord
from discord.ext import commands
import settings
import logging

logger = logging.getLogger("bot")

def main():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        logger.info(f"User: {client.user} (ID: {client.user.id})")
        print('-----------------------')

    @client.event
    async def on_message(message):
        msg = message.content
        #Игнорирование собственных сообщений
        if message.author == client.user:
            return
        
        if msg.startswith("!ping"):
            await message.channel.send("pong!")

    client.run(settings.DISCORD_TOKEN, root_logger=True)

if __name__ == "__main__":
    main()