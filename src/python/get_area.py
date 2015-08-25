from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

csvFile = open("area.csv",'wt')

html = urlopen("http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201504/t20150415_712722.html")

bs = BeautifulSoup(html.read())
#print(bs)
sl = bs.findAll("p",{"class":"MsoNormal"})
try:
    writer = csv.writer(csvFile)
    for s in sl:
        w = s.get_text().split()
        pc=''
        
        if w[0][2:] == '0000':
            pc='0'
        elif w[0][4:]=='00':
            pc=w[0][0:2]+'0000'
        else:
            pc=w[0][0:4]+'00'
        writer.writerow((w[0],w[1],pc))
        #for w in s.get_text().split():
         #   print (w +'\n')
finally:
    csvFile.close()
#    print(s.get_text())
