# -*- coding: utf-8 -*-
import requests

URL_IP = 'http://127.0.0.1:8000/ip'

URL_USER_AGENT = 'http://127.0.0.1:8000/user-agent'

URL_ENCODING_UTF8 = 'http://127.0.0.1:8000/encoding/utf8'

URL_GET = 'http://127.0.0.1:8000/get'

'''
	简单GET请求
'''
def use_simple_requests(url):
	response = requests.get(url)
	print '>>>>Response Headers:'
	print response.headers

	print '>>>>Response Body:'
	print response.text

def use_params_requests():
	params = {'param1':'hello','param2':'world'}
	#发送请求
	response = requests.get(URL_GET,params=params)
	#处理响应
	print '>>>>Response Headers:'
	print response.headers

	print '>>>>Status Code:'
	print response.status_code
	print response.reason


	print '>>>>Response Body:'
	print response.json()


if __name__ == '__main__':
	print '>>>>use simple requests:'
	use_simple_requests(URL_IP)

	print '******'*20

	print '>>>>use param requests:'
	use_params_requests()
	#use_params_urllib2()

	#print '******'*20
	#use_simple_urllib2(URL_USER_AGENT)
	#print '******'*20
	#use_simple_urllib2(URL_ENCODING_UTF8)
