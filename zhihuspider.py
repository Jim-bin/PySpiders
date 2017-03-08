# -*- coding:utf-8 -*-
import requests
import re
import sys

class ZhihuSpider:
    def __init__(self):
        self.url = 'https://www.zhihu.com/'
        self.email_login_url = 'https://www.zhihu.com/login/email'
        self.phone_number_login_url = 'https://www.zhihu.com/login/phone_num'
        self.headers = {
            "Host": "www.zhihu.com",
            "Referer": "https://www.zhihu.com/",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
        self.session = requests.session()

    def get_xsrf(self):
        try:
            req = self.session.get(url = self.url,headers = self.headers)
            if req.status_code == 200:
                print u'打开网页成功'
            html = req.text
        except:
            print u'打开网页失败'
            sys.exit(0)
        pattern = re.compile('name="_xsrf" value="(.*?)"')
        try:
            _xsrf = re.findall(pattern,html)
            print u'获取_xsrf参数成功'
            return _xsrf
        except:
            print u'获取_xsrf参数失败'
            sys.exit(0)

    def login(self):
        user_name = raw_input('username = ')
        password = raw_input('password = ')
        if re.match(r'^1\d{10}$',user_name):
            print u'手机号登录'
            post_url = self.phone_number_login_url
            post_data = {
                '_xsrf' : self.get_xsrf(),
                'password' : password,
                'phone_num' : user_name,
            }
        else:
            if '@' in user_name:
                print u'邮箱登录'
                post_url = self.email_login_url
                post_data = {
                    '_xsrf' : self.get_xsrf(),
                    'password' : password,
                    'email' : user_name,
                }
        req = self.session.post(url = post_url,data = post_data,headers = self.headers)
        print req.status_code

spider = ZhihuSpider()
spider.login()
