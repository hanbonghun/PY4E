import urllib.error, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

fhand=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_750686.xml').read()
tree = ET.fromstring(fhand)
results = tree.findall('comments/comment/count')
sum = 0
for i in results:
    sum = sum + int(i.text)
print(sum)
