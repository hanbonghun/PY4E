import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Jan.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = input('Enter count: ')
count = int(count)
position = input('Enter position: ')
position = int(position)

print('Retrieving: ',url)
for i in range(int(count)):
    tags=soup('a')
    tag = tags[position-1]
    b= tag.attrs['href']
    print('Retrieving: ',b)
    url = b
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
