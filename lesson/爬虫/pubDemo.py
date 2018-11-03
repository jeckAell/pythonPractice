#coding=utf-8
import urllib.request
from bs4 import BeautifulSoup

nameList = []
scoreList = []
countryList = []
url = 'https://movie.douban.com/top250'

#此文件实现了一个简单的爬虫例子

def getDate(url): #根据rul获取整个页面
    '''
    两个获取页面到方法
    urllib.request.urlopen()
    request.get()    该方法可以应对反爬虫

    '''
    res = urllib.request.urlopen(url).read().decode()  #读取整个页面read(),decode()用于解码
    return res

def parseData(html): #数据分析，提取所需信息
    soup = BeautifulSoup(html,'html.parser')
    mZone = soup.find('ol')
    movieList = mZone.find_all('li')

    for movie in movieList:
        movieName = movie.find('span',attrs={'class':'title'}).getText()    # find返回的是第一结果
        movieScore = movie.find('span',attrs={'class':'rating_num'}).getText()
        movieCountry = movie.find('p').getText().rstrip().split('/')[-2]  #将字符串用 / 分割开，[-2]只取倒数第二个
        nameList.append(movieName)
        scoreList.append(movieScore)
        countryList.append(movieCountry)

    next_url =  soup.find('span',attrs={'class':'next'}).find('a')   #得到a标签中到href属性中到内容
    if next_url:
        newUrl = url + next_url['href']
        html = getDate(newUrl)
        parseData(html)
    return nameList,scoreList,countryList

def saveData(nameList,scoreList,countryList): #数据存储，存储到txt文件
    try:
        resFile = open('resout.txt','w',encoding='utf-8')
        for i in range(250):
            lineText = '名字：' + nameList[i] + '\t得分:' + scoreList[i] + '\t国家:'+ countryList[i]
            resFile.write(lineText+ '\n')

        resFile.close()
    except:
        print('file not exsit')



myHtml = getDate(url)

nameList,scoreList,countryList = parseData(myHtml)

saveData(nameList,scoreList,countryList)