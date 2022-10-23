import discord
from decouple import config
from message_handler import handle_message
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

my_secret = config('TOKEN')
print(my_secret)

client.run(my_secret)


@client.event
async def on_connect():
    print("Connected")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_ready():
    print('Ready!')


@client.event
async def on_message(message):
    await handle_message(message)


keep_alive()
