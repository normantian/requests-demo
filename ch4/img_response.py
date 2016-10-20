# -*- coding: utf-8 -*-
import requests

def download_image():
	'''
		下载图片，文件
	'''
	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
	url = 'http://d.hiphotos.baidu.com/baike/c0%3Dbaike180%2C5%2C5%2C180%2C60/sign=c9b698fab67eca80060831b5f04afcb8/e61190ef76c6a7efb5bc96fffbfaaf51f2de6654.jpg'
	response = requests.get(url,headers = headers,stream = True)
	with open('demo.jpg','wb') as fd:
		for chunk in response.iter_content(128):
			fd.write(chunk)
	#print response.status_code, response.reason
	#print response.content
def download_image_improved():
	#伪造header信息
	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
	#限定url
	url = 'http://d.hiphotos.baidu.com/baike/c0%3Dbaike180%2C5%2C5%2C180%2C60/sign=c9b698fab67eca80060831b5f04afcb8/e61190ef76c6a7efb5bc96fffbfaaf51f2de6654.jpg'

	#response = requests.get(url,headers = headers,stream = True)

	from contextlib import closing
	with closing(requests.get(url,headers = headers,stream = True)) as response:
		#打开文件
		with open('demo1.jpg','wb') as fd:
			#每128写入一次
			for chunk in response.iter_content(128):
				fd.write(chunk)
	

if __name__ == '__main__':
	#download_image()
	download_image_improved()
