import json

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


def get_usernames(uuid):
    return requests.get('https://api.mojang.com/user/profiles/{}/names'.format(uuid)).json()


def get_profiles(*usernames):
    return requests.post(
        url='https://api.mojang.com/profiles/minecraft',
        headers={
            b'Content-Type': b'application/json'
        },
        data=json.dumps(list(usernames))
    ).json()
