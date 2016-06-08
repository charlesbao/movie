from urlparse import urlparse

files = open('out1.txt')
urls = []
for each in files.readlines():
    # url = urlparse('http://'+each).hostname
    # if not url in urls and not url is None:
    #     urls.append(url)
    if 'tumblr' in each:
        urls.append(each)


fp = open('url.txt','w')
fp.write('\n'.join(urls))
fp.close()