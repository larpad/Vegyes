


import requests
import json


def jokes():
    f = r"https://official-joke-api.appspot.com/random_ten"
    data = requests.get(f)
    tt = json.loads(data.text)
    return tt


