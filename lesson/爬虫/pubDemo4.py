from urllib.request import Request,urlopen
import ssl   #当遇到有的网站没有CA认证的证书时，使用此包给予信任

# 此示例展示了抓取不可信任的网站

baseUrl = "https://www.12306.cn/mormhweb/"


ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'

req = Request(baseUrl,headers={
    'User-agent':ua
})

#忽略不信任证书
context = ssl._create_unverified_context()

with urlopen(req,context = context) as res:
    print(res._method)
    print(res.read())
