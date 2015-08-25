from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

namelist = bsObj.findAll("span", {"class","green"})
for name in namelist:
    print(name.get_text())

hlist = bsObj.findAll({"h1","h2","h3","h4","h5","h6"})
for h in hlist:
    print(h)


alist = bsObj.findAll("span",{"class":"green","class":"red"})
for a in alist:
    print(a)


#text 
nlist = bsObj.findAll(text="the prince",limit=1)
print(len(nlist))
for n in nlist:
    print(n)

#keyword
alltext = bsObj.findAll(id="text")

for aa in alltext:
    print(aa)
print(len(alltext))

















