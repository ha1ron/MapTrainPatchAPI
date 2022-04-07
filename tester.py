import json
import requests
from requests.auth import HTTPBasicAuth



s = requests.Session()
s.headers.update({'Connection': 'keep-alive', 'X-CSRF-TOKEN': 'Fetch'})
r = s.get('http://172.22.202.84:5000/tutorials?MONTH=222222&poezd=57386388007008', auth=HTTPBasicAuth('ocrv', 'ocrv'))

print(r.text)
