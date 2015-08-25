from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

csvFile = open("major.csv",'wt')

html = urlopen("http://gaokao.chsi.com.cn/sch/zyk/zydm_bk.jsp#b_zx")

bs = BeautifulSoup(html.read())
#print(bs)
sl = bs.findAll("tr",{"bgcolor":"#FFFFFF"})
'''for s in sl:
    print(s.get_text())
    w=s.get_text().split()
    print(len(w[0]))

'''
try:
    writer = csv.writer(csvFile)
    for s in sl:
        w = s.get_text().split()
        pc=''
        
        if len(w[0]) == 2:
            pc='0'
        elif len(w[0])==4:
            pc=w[0][0:2]
        else:
            pc=w[0][0:4]
        writer.writerow((w[0],w[1],pc))
finally:
    csvFile.close()
#    print(s.get_text())
