import urllib3
from urllib.parse import urlencode
import requests
#实现urllib3和requests库的使用

d = {
    'wd':'小说网'
}

baseUrl = "http://www.baidu.com/s"

url = '{}?{}'.format(baseUrl,urlencode(d))

with urllib3.PoolManager() as http:
    response = http.request('GET',url,headers={
        'User-agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
    })
    print(type(response))
    # response:HTTPResponse = HTTPResponse()
    print(response.status)
    print(response.data)