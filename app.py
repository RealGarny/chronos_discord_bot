import discord
from discord.ext import commands
from settings import DISCORD_TOKEN

def main():
    intents = discord.Intents.default()

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"bot started as: {bot.user}")
        print('-----------------------')

    bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main()