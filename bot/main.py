from setup import client
from message_handler import handle_message


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
    handle_message(message)
