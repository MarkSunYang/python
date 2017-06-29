import urllib.request
import urllib.parse

url='http://www.baidu.com'
#url = 'http://www.qiushibaike.com/hot/'
#1.1 最简单
#访问 open 一个url并且 read最后输出
#
# rep=urllib.request.urlopen(url)
# html=rep.read()
# print (html)


#2.使用request
# req=urllib.request.Request(url)
# rep=urllib.request.urlopen(req)
# the_page=rep.read()
# print(the_page)

#发送数据
# uer_agent=''
# value={
#     'act':'login',
#     'login[email]':'mark.sun@163.com',
#     'login[password]':'123445'
# }
# data=urllib.parse.urlencode(value)
# req=urllib.request.Request(url,data)
# req.add_header('Referer','')#是从该网址转到当前url


#异常处理
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

req=Request('http://www.baidu.com')
try:
    rep=urlopen(req)
except HTTPError as e:
    print('The server couldnt fulfill the request')
except URLError:
    print('Url Error')
else:
    print('Good')
    print(rep.read().decode("utf8"))

