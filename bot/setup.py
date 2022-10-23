import discord
from decouple import config

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

my_secret = config('TOKEN')
print(my_secret)


def set_up():
    client.run(my_secret)
