import discord
from decouple import config
from goodreads import client

discord_token = config('TOKEN')
# goodreads_api_key = config("GOODREADS_API_KEY")
# goodreads_api_secret = config("GOODREADS_API_SECRET")

# ----- discord ----- #
intents = discord.Intents.default()
intents.message_content = True

discord_client = discord.Client(intents=intents)

# ----- goodreads ----- #
# goodreads_client = client.GoodreadsClient(goodreads_api_key, goodreads_api_secret)
