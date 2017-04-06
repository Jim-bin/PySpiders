# -*- coding:utf-8 -*-
import requests
import sys
import re
import urllib2
import time
'''  
从知乎上下载了很多gakki的照片，问题链接：https://www.zhihu.com/question/36059311
'''   
class zhihu:
    def __init__(self):
        self.question_url = 'https://www.zhihu.com/question/36059311'
        self.headers = {
            "Host": "www.zhihu.com",
            "Referer": "https://www.zhihu.com/",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Cookie': ''
        }
        self.session = requests.session()
        self.url_set = set()
        self.filepath = r'C:/Users/DELL/Desktop/Gakki/'

    def get_photo_url(self):
        try:
            html = self.session.get(url=self.question_url, headers=self.headers).text
        except:
            print 'cannot open the page'
            sys.exit(-1)
        regex = re.compile(r'https://(.*?).jpg')
        page_urls = re.findall(regex, html)
        for url in page_urls:
            if url.endswith('_r'):
                photo_url = 'https://' + url + '.jpg'
                self.url_set.add(photo_url)

    def download_photo(self):
        id = 0
        for photo_url in self.url_set:
            try:
                photo = urllib2.urlopen(url=photo_url).read()
            except:
                pass
            with open(self.filepath + str(id) + '.jpg', 'wb') as f:
                f.write(photo)
            f.close()
            id += 1
            time.sleep(5)

test = zhihu()
test.get_photo_url()
test.download_photo()
