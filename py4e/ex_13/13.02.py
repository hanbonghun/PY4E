import json
import urllib.error, urllib.parse, urllib.request
data = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_750687.json').read()
data = json.loads(data)
data = data['comments']
sum = 0
for dt in data:
    sum=  sum + int(dt['count'])

print(sum)


#the JSON object must be str, bytes or bytearray, not HTTPResponse
