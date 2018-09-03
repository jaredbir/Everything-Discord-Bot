import discord
import asyncio

client=discord.Client()

if not discord.opus.is_loaded():
	discord.opus.load_opus('opus')

class VoiceEntry:
    def __init__(self, message, player):
        self.requester = message.author
        self.channel = message.channel
        self.player = player
    def __str__(self):
        fmt = '*{0.title}* uploaded by {0.uploader} and requested by {1.display_name}'
        duration = self.player.duration
        if duration:
            fmt = fmt + ' [length: {0[0]}m {0[1]}s]'.format(divmod(duration, 60))
        return fmt.format(self.player, self.requester)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message):
	msg=""
	if message.content.startswith('!everybody'):
		for member in message.server.members:
			msg+="<@"+str(member.id)+">\n"
	

	await client.send_message(message.channel, msg)
		
f=open("discord.key","r")
key=f.readline()	
client.run(key)