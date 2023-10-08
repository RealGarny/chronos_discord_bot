import discord
from discord.ext import commands
from settings import DISCORD_TOKEN

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)


@client.command()
async def hello(ctx):
    await ctx.send("hello")

'''
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f"User {message.author.name} Said: {message.content}")
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
'''
if __name__ == "__main__":
    client.run(DISCORD_TOKEN)