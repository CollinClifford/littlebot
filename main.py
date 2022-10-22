import discord
import random
from quotes import quotes
from keep_alive import keep_alive
from decouple import config
from data_dude import da_collector
from flask import Flask

    
my_secret = config('TOKEN')

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_connect():
    print("Connected")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content.lower().startswith(
            'ho') or message.content.lower().find('ho ho') != -1:
        await message.channel.send('Ho ho!')

    if message.content.lower().find('bye') != -1:
        await message.channel.send(f'{message.author} is irretrievably lost')

    if message.content.lower().find("thirsty") != -1 or message.content.lower(
    ).find("hungry") != -1 or message.content.lower().find("sad") != -1:
        await message.channel.send('Put a tiger in your tank!')

    if message.content.startswith("$quote"):
        await message.channel.send(random.choice(quotes))
    
    await da_collector(message)
   
@client.event
async def on_ready():
    print('Ready!')

# keep_alive()
client.run(my_secret)