import json
import requests
from decouple import config

total_books = [
    'Perdido Street Station by China Mieville',
    'The Scar by China Mieville',
    'Hyperion by Dan Simmons',
    'Little, Big by John Crowley',
    'A Wild Sheep Chase by Haruki Murakami',
    'What Does It All Mean? by Thomas Nagel',
    'Transcend by Scott Barry Kaufmann',
    'All The Good Indians by Stephen Graham Jones',
    'Chronicles of Amber 1-5 by Robert Zelazny',
    'Midnight in the Garden of Good and Evil by John Berendt',
    'Crime and Punishment by Fyodor Dostoevsky',
    'Rasputin by Douglas Smith',
    'The Lord of the Rings by J. R. R. Tolkien',
    'A Canticle for Liebowitz by Walter M. Miller Jr.',
    'The Lottery and Other Stories by Shirley Jackson',
    'Piranesi by Susanna Clarke',
    'The Name of the Rose by Umberto Eco',
    'Slewfoot by Brom',
    'Frankenstein by Mary Shelley',
    '1Q84 by Haruki Murakami',
    'Denial of Death by Ernst Becker',
    'Storm of Steel by Ernst Junger',
    'The Glass Bees by Ernst Junger',
    'Atomic Habits by James Clear',
    'Real Happiness by Sharon Salzberg',
]

# look into pulling quotes from massive files.
# Pull between . ? !  except . following abbreviations

books_api_key = config('BOOKS_API_KEY')
books_base_url = config("BOOKS_BASE_URL")
books_api_uid = config("BOOKS_API_UID")


def get_user_details():
    get_user_details_url = '{}/users/{}/bookshelves&key={}'.format(books_base_url, books_api_uid, books_api_key)
    response = requests.get(get_user_details_url)
    return json.loads(response.text)

