from setup import client
from setup import set_up
from message_handler import handle_message
from keep_alive import keep_alive


set_up()

@client.event
def on_connect():
    print("Connected")


@client.event
def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
def on_ready():
    print('Ready!')


@client.event
async def on_message(message):
    await handle_message(message)


keep_alive()
