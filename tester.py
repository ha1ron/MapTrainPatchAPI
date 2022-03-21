import json
import requests
from requests.auth import HTTPBasicAuth



s = requests.Session()
s.headers.update({'Connection': 'keep-alive', 'X-CSRF-TOKEN': 'Fetch'})
r = s.get('http://192.168.0.101:5000/tutorials', auth=HTTPBasicAuth('admin', 'admin'))

print(r.text)
