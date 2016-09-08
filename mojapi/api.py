import json

import requests
import time

from .utils import currenttimemillis_to_python_datetime


__all__= [
    'get_statuses',
    'get_uuid',
    'get_usernames',
    'get_profiles',
    'get_blocked_server_hashes'
]


def get_statuses():
    return requests.get('https://status.mojang.com/check/').json()


def get_uuid(username, unix_timestamp=None):
    if unix_timestamp is None:
        unix_timestamp = int(time.time())
    return requests.get(
        'https://api.mojang.com/users/profiles/minecraft/{}?at={}'.format(username, unix_timestamp)
    ).json()


def get_usernames(uuid):
    username_infos = requests.get('https://api.mojang.com/user/profiles/{}/names'.format(uuid)).json()
    for username_info in username_infos:
        try:
            changed_to_at = username_info['changedToAt']
        except KeyError:
            continue
        else:
            username_info['changedToAt'] = currenttimemillis_to_python_datetime(changed_to_at)
    return username_infos


def get_profiles(*usernames):
    return requests.post(
        url='https://api.mojang.com/profiles/minecraft',
        headers={
            b'Content-Type': b'application/json'
        },
        data=json.dumps(list(usernames))
    ).json()


def get_blocked_server_hashes():
    response = requests.get('https://sessionserver.mojang.com/blockedservers')
    response.raise_for_status()
    sha1_hashes = response.content.split(b'\n')
    return sha1_hashes
