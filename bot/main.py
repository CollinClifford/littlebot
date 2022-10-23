from setup import client, my_secret
from message_handler import handle_message
from keep_alive import keep_alive


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

client.run(my_secret)
keep_alive()
