import urllib.request, urllib.parse, urllib.error
import json
serviceurl ='https://maps.googleapis.com/maps/api/geocode/json?'

while(True):
    address = input('Enter location ')
    if len(address)<1:break
    api_key= 'AIzaSyAtmlNZaYm4eRF68ad3KOsou2_yLMtCVaw'
    url = serviceurl + urllib.parse.urlencode({'address' : address}) + '&key=' + api_key
    print('Retrieving',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved',len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status']!='OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent= 4))

    lat = js["results"][0]["geometry"]['location']['lat']
    lng = js["results"][0]["geometry"]['location']['lng']

    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
