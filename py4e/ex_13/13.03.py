import urllib.error, urllib.parse, urllib.request
import json
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
place = 'University of Essex'
api_key = '42'

url = serviceurl + urllib.parse.urlencode({'address' : place}) + '&key=' + api_key
print(url)

uh = urllib.request.urlopen(url)
data = uh.read().decode()

js = json.loads(data)

print(js['results'][0]['place_id'])
