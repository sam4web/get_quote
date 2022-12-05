import random
import requests


def get_rand(len):
    rand = random.randint(0, len - 1)
    return rand


def get_quote():
    url = "https://type.fit/api/quotes"
    r = requests.get(url)
    quote_list = r.json()
    quote = quote_list[get_rand(len(quote_list))]
    return quote
