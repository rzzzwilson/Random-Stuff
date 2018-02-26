import requests
from pprint import pprint

UserAgent = 'my bot 0.1'
Username = 'rzzzwilson'

r = requests.get(f'http://www.reddit.com/user/{Username}/comments/.json',
                 {'limit': 2}, headers={'User-agent': UserAgent})
data = r.json()
for k in data:
    print(k)
print(data['kind'])
for k in data['data']:
    print(k)
print(f"len(data['data'])={len(data['data'])}")
#pprint.pformat(data)
pprint(data)
