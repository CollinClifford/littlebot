from setup import discord_client, discord_token
from message_handler import handle_message
from keep_alive import keep_alive


@discord_client.event
async def on_connect():
    print("Connected")


@discord_client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(discord_client))


@discord_client.event
async def on_message(message):
    await handle_message(message)

discord_client.run(discord_token)
keep_alive()
