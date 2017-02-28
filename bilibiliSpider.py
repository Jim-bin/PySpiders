# -*- coding:utf-8 -*-
'''
给定视频ID,爬取B站弹幕  
在未登录时只能爬取少量弹幕  
登录后的爬取以后更新
'''
import requests
import sys
import re

class BilibiliSpider:
	def __init__(self,videoId):
		self.videoUrl = 'http://www.bilibili.com/video/av' + str(videoId) + '/'
		self.commentBaseUrl = 'http://comment.bilibili.com/'

	def getCommentCid(self):
		try:
			html = requests.get(self.videoUrl).content
		except:
			print ('cannot open video pages')
			sys.exit(0)
		regex = re.compile('cid=(\d{7})')
		try:
			cid = re.findall(regex,html)[0]
		except:
			print ('cannot find cid!')
			sys.exit(0)
		return cid

	def getComments(self):
		cid = self.getCommentCid()
		commentUrl = self.commentBaseUrl + str(cid) + '.xml'
		try:
			commentXml = requests.get(commentUrl).content
		except:
			print ('cannot open comment XML files')
			sys.exit(0)
		regex = re.compile('<d p=(.*?)>(.*?)</d>')
		try:
			comments = re.findall(regex,commentXml)
		except:
			print ('cannot finnd comments')
			sys.exit(0)
		return comments

if __name__ == '__main__':
	spider = BilibiliSpider(5043905)
	comments = spider.getComments()
	for comment in comments:
		print(comment[1])
