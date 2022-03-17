import json
import requests
from local_settings import server_url


s = requests.Session()
s.headers.update({'Connection': 'keep-alive', 'X-CSRF-TOKEN': 'Fetch'})
r = s.get(server_url)

print(r.text)
