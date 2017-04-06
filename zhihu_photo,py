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
            'Cookie': 'd_c0 = "ABAAhYNM2gqPTjP5rVTJ5JW9XMDyq7YmdlQ=|1479228481";zap = d2ee27a5 - 128a - 4964 - 9668 - e6302f61eed3;r_cap_id = "YTkxNjZhYmU1NWFiNGNhNmFmMGM3NGFkODYxNWY4NTc=|1488960249|37a0b1dc740b94388b7fd89de024ec530658c26e";cap_id = "ZWE5ZDFjZjc5NmExNDQxN2EzMDRkNTk5MWE0ODI1NjE=|1488960249|0c02021a22ac5a596da3dbb22819a4b5f650a284";_ga = GA1.2.804709831.1489498982;q_c1 = 000d76b7db66453daf52fbc2e10be92a | 1490010539000 | 1479228480000;nweb_qa = heifetz;aliyungf_tc = AQAAAJQhe193sQQAEGQp0pS0Tjq8bZKV;_xsrf = 2b4f57f862cb4db90e652e69b3a83859;__utma = 51854390.804709831.1489498982.1490157835.1491449793.6;__utmc = 51854390;__utmz = 51854390.1489676250.3.3.utmcsr = baidu | utmccn = (organic) | utmcmd = organic;__utmv = 51854390.100 - 1 | 2 = registration_date = 20140811 = 1 ^ 3 = entry_date = 20140811 = 1;s - q = gakki % E7 % 85 % A7 % E7 % 89 % 87;s - i = 8;sid = lf1vml11;s - t = autocomplete;z_c0 = Mi4wQUFEQWJNbzBBQUFBRUFDRmcwemFDaGNBQUFCaEFsVk5BMGpuV0FDODh3LWFweU9JUU8yVktiaWY3T1h6bk5DWUVn | 1491451063 | 08733be5bce042978addd1866b001f8fa03a6cd5'
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
