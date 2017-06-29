import requests
from bs4 import BeautifulSoup

info=[]
count=0

for i in range(5,10):
    url='https://www.qiushibaike.com/hot/page/'+str(i)+'/?s=4995471'
    print(url)
    rep=requests.get(url,timeout=40)
    soup=BeautifulSoup(rep.text,'html.parser')
    tag=soup.find_all(name='div',attrs={'class','article block untagged mb15'})

for g in tag:
        info.append(g.text.split()[:5])
for j in info:
        count=count+1
        with open('D://123.txt','a') as f:
            f.write('\n\n')
            f.writelines(j[2:-1])
            f.close()
