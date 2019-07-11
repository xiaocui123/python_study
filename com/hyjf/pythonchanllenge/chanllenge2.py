import requests

r=requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")
print(r.status_code)
thestring = r.text


thestring = thestring.split('\n')
thestring = thestring[38:1257]
thestring = "".join(thestring)

print (thestring)

import collections
d = collections.defaultdict(int)
for c in thestring:
    d[c] += 1

for c in sorted(d, key=d.get, reverse=True):
    print ('%s %6d' % (c, d[c]))
