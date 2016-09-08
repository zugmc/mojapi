# mojapi
Python library for interacting with Mojang APIs.

# Installation
```
pip install mojapi
```

# Usage
Make basic API requests to Mojang as laid out at http://wiki.vg/Mojang_API. Where appropriate, timestamps are converted to native Python `datetime` objects, and base64 encoded JSON objects are automatically expanded.

```python
>>> from mojapi import *
>>> get_uuid('gozug')
{'id': 'bdc46881e95447b694e82d10bac42ccb', 'name': 'gozug'}
>>> get_detailed_profile('bdc46881e95447b694e82d10bac42ccb')
{'properties': [{'value': {'textures': {'SKIN': {'url': 'http://textures.minecraft.net/texture/1d9e8dafe7d87bb7cba7eb3d8d2d5bf58eab72ecdfdf9ecce3d1c03871c0'}}, 'profileId': 'bdc46881e95447b694e82d10bac42ccb', 'timestamp': datetime.datetime
(2016, 9, 8, 23, 44, 15, 472000), 'profileName': 'gozug'}, 'name': 'textures'}], 'id': 'bdc46881e95447b694e82d10bac42ccb', 'name': 'gozug'}
```

# Contributions
Contributions are welcome.
