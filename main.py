import os
import discord
from dotenv import load_dotenv

#First we need to connect to a client
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
# TOKEN = "MTIwODQ1Mzc4NzYyMzA5NjM2MA.GNZSUE.AACEioTT4lAanvlc986os64t0vLDgODK6lqCW0"

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})'
    )
client.run(TOKEN)