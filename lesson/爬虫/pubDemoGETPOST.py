from urllib.request import Request,urlopen
from urllib import parse

baseUrl = "http://www.baidu.com/s?{}"

d = {
    'wd':'小说网'
}

parseD = parse.urlencode(d)

url = baseUrl.format(parseD)

ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'

req = Request(url,headers={
    'User-agent':ua
})
with urlopen(req) as res:
    with open('test.html','wb+') as f:
        f.write(res.read())
        f.flush()

print(url)