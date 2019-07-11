import re
import requests

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

i = 63579

while 1:
    print ("Trying url = " + url + str(i))
    u = requests.get(url + str(i))
    s = u.text
    print ('\t' + s)
    print
    i = re.findall(r'([0-9]+)', s)[0]
    u.close()
