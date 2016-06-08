#coding=utf8
import requests
import re
import urlparse
import json

def getMovie(keywords):
    url = 'http://www.xiaomw.com/search.php?keywords=' + keywords
    try:
        contents = requests.get(url,headers = header).content
    except:
        return ERROR
    rep = re.findall('''<a class="pic" title="(.+?)" href="(.+?)"''',contents,re.S)
    if len(rep) > 0:
        title = rep[0][0]
        url = rep[0][1]
    else:
        return ERROR
    try:
        contents = requests.get(url,headers = header).content
    except:
        return ERROR
    url = re.findall('''<iframe src="(.+?)"''',contents,re.S)[0]
    query = urlparse.urlparse(url).query
    if query.startswith('url'):
        getUrlMovie(title,url)
    elif query.startswith('vid'):
        url = 'http://qq.xiaomw.com/api.php?' + query
        getM3u8Movie(title,url)
    else:
        print query

def getUrlMovie(title,url):
    try:
        contents = requests.get(url,headers = header).content
    except:
        return ERROR
    rep = re.findall('''"time"\s*\:\s*"(.*?)"\s*,\s*"key"\s*\:\s*"(.*?)"\s*,\s*"url"\s*\:\s*"(.+?)"\s*,\s*"type"\s*\:\s*"(.*?)"''',contents,re.S)[0]
    data = {
        "time":rep[0],
        "key":rep[1],
        "url":rep[2],
        "type":rep[3]
    }
    contents = requests.post('http://mk.xiaomw.com/api.php',data = data,headers = header).content
    resp = json.loads(contents)
    if resp['success'] == '1':
        if resp['play'] == 'm3u8':
            getM3u8Movie(title,resp['url'])
        else:
            getHtmlMovie(title,resp['url'])

def getHtmlMovie(title,url):
    # try:
    #     contents = requests.get(url,headers = header).content
    # except:
    #     return ERROR
    print url


def getM3u8Movie(title,url):
    try:
        contents = requests.get(url,headers = header).content
    except:
        return ERROR
    fp = open(title+'.m3u8','w')
    fp.write(contents)
    fp.close()
    print 'success'
    return SUCCESS

ERROR = 'error'
SUCCESS = 'success'
header = {
    'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}

keywords = '百鸟朝凤'
getMovie(keywords)

