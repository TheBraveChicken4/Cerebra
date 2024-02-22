import os
import discord
from dotenv import load_dotenv

#First we need to connect to a client
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == "Hello":
        await message.channel.send("Hello!")

    if message.content.startswith('!When do we meet?'):   
        await message.channel.send('We meet every other Monday from 7-8pm. Our meeting schedule is on our website.')

    if message.content == "raise-exception":
        raise discord.DiscordException


client.run(TOKEN)