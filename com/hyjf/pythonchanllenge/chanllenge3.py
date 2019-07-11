import requests

r=requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
sourcestr=r.text

sourcestr=sourcestr.split('\n')
sourcestr=sourcestr[22:1271]
sourcestr=''.join(sourcestr)

import re
print ("".join(re.findall(r'[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]', sourcestr)))