from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

try:
    html = urlopen("http://www.test.com/index.html")
except HTTPError as e:
    print(e)
else:
   if html is None:
       print("URL is not found")
   else:
           bsObj = BeautifulSoup(html.read())
           print(bsObj)
