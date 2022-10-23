import random
from bot.quotes import quotes
from data_dude import da_collector
from setup import client


def handle_message(message):
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

    if message.content.startswith('Hi littlebot'):
        name = message.authorsplit('#')[0]
        await message.channel.send(f'Hi {name}!')

    await da_collector(message)
