import discord

client=discord.client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('!everybody'):
		msg = 'Hello beter'.format(message)
		await client.send_message(message.channel, msg)



client.run('NDg1NzA0NzEwMjI2MDUxMDcy.Dm0n8w.mUAW9mrbm4H_6-FHVQ5AB7iiRb8')