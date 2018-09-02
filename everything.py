import discord
import asyncio

client=discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
	if message.content.startswith('!everybody'):
		msg=""
		for member in message.server.members:
			msg+="<@"+str(member.id)+">\n"
		await client.send_message(message.channel, msg)
f=open("discord.key","r")
key=f.readline()	
client.run(key)