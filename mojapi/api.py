import requests


def get_statuses():
    return requests.get('https://status.mojang.com/check/').json()
