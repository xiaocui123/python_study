import requests, re
urlbase = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
REsearchNUM = re.compile("(\d+)").search
initNUM = '63579'
while True:
    webContents = requests.get(urlbase + initNUM).text
    match = REsearchNUM(webContents)
    if match:
        initNUM = match.group(1)
        print ("We're now going to", initNUM)
    else:
        print (webContents)
        break