from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.ipin.com/school/schoolFilter.do")
bsObj = BeautifulSoup(html)

print(bsObj)

namelist = bsObj.findAll("td",{"class","col1td"})
for name in namelist:
    print(name)
