from urllib.parse import urlencode

from urllib.request import urlopen,Request
import simplejson


#此示例展示抓取一些通过ajax访问的数据。在浏览器的开发模式中，选择‘network’板块，选择对应的请求地址，该地址就是Ajax暗中访问的地址。在代码中对该地址进行抓取即可

ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'

jurl = 'https://movie.douban.com/j/search_subjects'

d = {
    'type':'movie',
    'tag':'热门',
    'page_limit':10,
    'page_start':10
}

req = Request('{}?{}'.format(jurl,urlencode(d)),headers={
    'User-agent':ua
})

with urlopen(req) as res:
   subjects = simplejson.loads(res.read())
   print(len(subjects['subjects']))
   print(subjects)

