import requests
import time


def get_statuses():
    return requests.get('https://status.mojang.com/check/').json()


def get_uuid(username, unix_timestamp=None):
    if unix_timestamp is None:
        unix_timestamp = int(time.time())
    return requests.get(
        'https://api.mojang.com/users/profiles/minecraft/{}?at={}'.format(username, unix_timestamp)
    ).json()
