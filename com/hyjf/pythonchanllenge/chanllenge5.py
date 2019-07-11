import urllib.request
import _pickle as cPickle

webContents=urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()

pwc=cPickle.loads(webContents)

for line in pwc:
    array=[]
    for column in line:
        array.append(column[0]*column[1])
        # print(array)
    print(''.join(array))

print('\n'.join([''.join(column[0]*column[1] for column in line) for line in pwc]))
