import discord
from discord.ext import commands
from yt_dlp import YoutubeDL
import os
import settings
import logging
import asyncio

logger = logging.getLogger("bot")

def main():
    intents = discord.Intents.default()
    intents.message_content = True
    # Discord bot Initialization
    client = discord.Client(intents=intents)

    voice_clients = {}

    yt_dl_opts = {'format': 'bestaudio/best'}
    ytdl = YoutubeDL(yt_dl_opts)

    ffmpeg_options = {'options': "-vn"}


    # This event happens when the bot gets run
    @client.event
    async def on_ready():
        print(f"Bot logged in as {client.user}")


    # This event happens when a message gets sent
    @client.event
    async def on_message(msg):
        if msg.content.startswith("?play"):

            try:
                voice_client = await msg.author.voice.channel.connect()
                voice_clients[voice_client.guild.id] = voice_client
            except:
                print("error")

            try:
                url = msg.content.split()[1]

                loop = asyncio.get_event_loop()
                data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

                song = data['url']
                player = discord.FFmpegPCMAudio(song, **ffmpeg_options, executable=f"{os.getcwd()}\\ffmpeg\\ffmpeg.exe")

                voice_clients[msg.guild.id].play(player)

            except Exception as err:
                print(err)


        if msg.content.startswith("?pause"):
            try:
                voice_clients[msg.guild.id].pause()
            except Exception as err:
                print(err)

        # This resumes the current song playing if it's been paused
        if msg.content.startswith("?resume"):
            try:
                voice_clients[msg.guild.id].resume()
            except Exception as err:
                print(err)

        # This stops the current playing song
        if msg.content.startswith("?stop"):
            try:
                voice_clients[msg.guild.id].stop()
                await voice_clients[msg.guild.id].disconnect()
            except Exception as err:
                print(err)

    client.run(settings.DISCORD_TOKEN, root_logger=True)

if __name__ == "__main__":
    main()