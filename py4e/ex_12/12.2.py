import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_750684.html').read()
soup = BeautifulSoup(html, 'html.parser')

sum =0
lines = soup('span')
print(type(lines[0]))
for line in lines:
    line = str(line)
    x = re.findall('[0-9]+',line)
    sum = sum + int(x[0])

print(sum)
