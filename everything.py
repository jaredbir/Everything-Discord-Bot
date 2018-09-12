""" 
 This is a discord bot that I wrote. It can mention everyone for those pesky servers that turn off the ability to @everyone. 
 It has the ability for users to search youtube videos in discord and have this bot join the channel the user is in and play the youtube video.
 I plan on adding some pre-downloaded memes that the bot can play if the user mentions them. This is just a small project that I started and will add to from time to time.
"""

# Packages that I used

import discord
import asyncio
import logging
import youtube_dl

# Initializes and logs problems and errors that the code has, rather than to the console

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client=discord.Client()

# Checks if the Opus voice library has loaded, and if it hasn't it will load the Opus library for Voice use

if not discord.opus.is_loaded():
	discord.opus.load_opus('opus')

# On ready function that runs as soon as the bot has loaded and is ready to process info

@client.event 
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
# On message function that runs when a message is sent in the discord server or to the bot directly. There are multiple outcomes, and uses the prefix of ! to call functions.

@client.event
async def on_message(message):

	await client.add_reaction(message, emoji="💦")
	msg=""
	if message.content.startswith('!everybody'):
		for member in message.server.members:
			msg+="<@"+str(member.id)+">\n"
	if len(msg)!=0:
		print(message.server.emojis)
		await client.send_message(message.channel, msg)
	if message.content.startswith('!nut'):
		msg+="ٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴI"
		msg+="ٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴI"
		msg+="ٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴٴI"
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
		await client.send_message(message.channel, msg)
	"""if message.content.startswith('!beter'):
		emoji=get(client.get_all_emojis(), name='ringo')
		msg+=emoji
		await client.send_message(message.channel, msg)"""
	"""if message.content.startswith('!search') & message.author.voice_channel!=none:
					chan=message.author.voice_channel
					voice = await client.join_voice_channel(chan)
					player = await voice.create_ytdl_player()
					player.start()
			"""
# Runs the discord secret token so that the bot can run, and reads it from a file which is not uploaded.

f=open("discord.key","r")
key=f.readline()	
client.run(key)