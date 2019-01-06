import discord
import sys
import subprocess
import random
import asyncio
import time

tmp_command_dir = "./tmp_command.txt"
client = discord.Client()

def save_tmp_command(command):
    with open(tmp_command_dir, "w") as f:
        f.write(command)

def get_tmp_command():
    with open(tmp_command_dir, "r") as f:
        for line in f:
            return line

def execute_cmd(cmd):
    subprocess.call(cmd.split())

def arrange_players(players_str):
    real_players = []
    for player in players_str.split("\n"):
        if len(player) < 3 or 15 < len(player):
            continue
        real_players.append(player.strip())
    return real_players

@client.event
async def on_ready():
    print("Logged in!")

@client.event
async def on_message(message):
    if message.content.startswith('/team -ch'):
        save_tmp_command(message.content)
        info = message.content.split(" ")[:5]
        voice_channel = discord.utils.get(
                message.server.channels, 
                name=info[2], 
                type=discord.ChannelType.voice)

        member = [mem.display_name for mem in voice_channel.voice_members]
        random.shuffle(member)
        teamA = ", ".join(member[:int(len(member)/2)])
        teamB = ", ".join(member[int(len(member)/2):])
        msg =  "---- :cowboy: ----\n"
        msg += "{0}\n"
        msg += "---- :hugging: ----\n"
        msg += "{1}\n"
        msg = msg.format(teamA, teamB)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('/re'):
        msg = get_tmp_command()
        await client.send_message(message.channel, msg)

    if message.content.startswith('おとしちゃった'):
        try:
            sound_bot = await client.join_voice_channel(client.get_channel("455280262079709184"))
        except:
            pass
        sound = sound_bot.create_ffmpeg_player("otoshichatta.mp3")
        sound.start()
        await asyncio.sleep(7)
        try:
            await sound_bot.disconnect()
        except:
            pass
    
    if message.content.startswith('とまるんじゃねえぞ'):
        try:
            sound_bot = await client.join_voice_channel(client.get_channel("455280262079709184"))
        except:
            pass
        sound = sound_bot.create_ffmpeg_player("tomarunjya1.mp3")
        sound.start()
        await asyncio.sleep(14)
        #try:
        #    await sound_bot.disconnect()
        #except:
        #    pass
        #
        #await asyncio.sleep(1)
        #
        #try:
        #    sound_bot = await client.join_voice_channel(client.get_channel("455280262079709184"))
        #except:
        #    pass
        sound = sound_bot.create_ffmpeg_player("tomarunjya2.mp3")
        sound.start()
        await asyncio.sleep(6)
        try:
            await sound_bot.disconnect()
        except:
            pass

if __name__=="__main__":
    TOKEN = ""
    client.run(TOKEN)
