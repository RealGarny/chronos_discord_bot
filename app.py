import discord
from discord.ext import commands
import os
import settings
import logging

logger = logging.getLogger("bot")

def main():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="#", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        print('-----------------------')

    @bot.event
    async def on_message(message):
        msg = message.content
        #Игнорирование собственных сообщений
        if message.author == bot.user:
            return
        
        if msg.startswith("!music") or msg.startswith("!музыка"):
            await message.channel.send(msg)
            commandsEN = ["play", "stop", "pause", "queue", "resume"]
            commandsRU = ["начать", "стоп", "пауза", "очередь", "продолжить"]
            if msg.split()[1] in commandsEN:
                await message.channel.send("Command exists!")
            if msg.split()[1] in commandsRU:
                await message.channel.send("Есть Команда!")

    bot.run(settings.DISCORD_TOKEN, root_logger=True)

if __name__ == "__main__":
    main()