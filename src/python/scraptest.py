from urllib.request import urlopen
from bs4 import BeautifulSoup
try:
    html = urlopen("http://it-ebooks.info/book/6035/")
except HTTPError as e:
    print(e)
    #return null, break,or do some other "Plan B"
else:
bsObj=BeautifulSoup(html.read())
print(bsObj.h1)

##print(html.read())
