# -*- coding:utf-8 -*-

import requests
import re
import sys

headers = {
    'Cookie':'route=3b432386b71e29c2457eaf7073b54875; JSESSIONID_ids1=0001h0p5_SPpY3QRskHfUwQoV1i:-221F58',
    'Host':'idas.uestc.edu.cn',
    'Referer':'http://idas.uestc.edu.cn/authserver/login',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
session = requests.session()

login_url = 'http://idas.uestc.edu.cn/authserver/login'
html = session.get(login_url,headers = headers).text
# 匹配lt和execution参数
pattern1 = re.compile('name="lt" value="(.*?)"')
pattern2 = re.compile('name="execution" value="(.*?)"')
lt = re.findall(pattern1,html)
execution = re.findall(pattern2,html)
# 向网站提交的参数
username = raw_input('username = ')
password = raw_input('password = ')
post_data = {
    'username':username,
    'password':password,
    'lt':lt,
    'dllt':'userNamePasswordLogin',
    'execution':execution,
    '_eventId':'submit',
    'rmShown':'1',
}

session.post(url = login_url,data = post_data,headers = headers)
url = 'http://eams.uestc.edu.cn/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR'
data = {
    'tagId':'semesterBar13572391471Semester',
    'dataType':'semesterCalendar',
    'value':'123',
    'empty':'false',
}
req = session.get(url,headers=headers)
print req.content