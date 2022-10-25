import random
from books import total_books
from bot.quotes import quotes
# from data_dude import da_collector
from setup import discord_client
from quotes2 import quotes2


async def handle_message(message):
    if message.author == discord_client.user:
        return

    # --- COMMANDS --- #

    if message.content == "$quote":
        await message.channel.send(random.choice(quotes))
    elif message.content == "$books":
        for indx, book in enumerate(total_books, start=1):
            await message.channel.send(f'{indx}) {book}')

    # --- TEXT TRIGGERS --- #

    if message.content.lower().startswith(
            'ho') or message.content.lower().find('ho ho') != -1:
        await message.channel.send('Ho ho!')

    if message.content.lower().find('bye') != -1:
        await message.channel.send(f'{message.author} is irretrievably lost')

    if message.content.lower().find("thirsty") != -1 or message.content.lower(
    ).find("hungry") != -1 or message.content.lower().find("sad") != -1:
        await message.channel.send('Put a tiger in your tank!')

    if message.content.startswith('Hi littlebot'):
        name = message.author.split('#')[0]
        await message.channel.send(f'Hi {message.author.split("#")[0]}!')
    
    # if message.content == "$addquote":
    #     await quotes.append(message.content)

    if message.content.startswith("$quote Collin"):
        await message.channel.send(quotes2["Collin"][0])
    elif message.content == "$quote" and message.content.contains("1Q84"):
        await message.channel.send(quotes2[random.choice('1Q84')])
    elif message.content == "$quote" and message.content.contains("The Glass Bees"):
        await message.channel.send(quotes2[random.choice('The Glass Bees')])
           
        
    # --- DATA COLLECTION --- #

    # await da_collector(message)
