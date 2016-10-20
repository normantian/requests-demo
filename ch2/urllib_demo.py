# -*- coding: utf-8 -*-
import urllib2
import urllib

URL_IP = 'http://127.0.0.1:8000/ip'

URL_USER_AGENT = 'http://127.0.0.1:8000/user-agent'

URL_ENCODING_UTF8 = 'http://127.0.0.1:8000/encoding/utf8'

URL_GET = 'http://127.0.0.1:8000/get'

'''
	简单GET请求
'''
def use_simple_urllib2(url):
	response = urllib2.urlopen(url)
	print '>>>>Response Headers:'
	print response.info()

	print '>>>>Response Body:'
	print "".join([line for line in response.readlines()])

def use_params_urllib2():
	params = urllib.urlencode({'param1':'hello','param2':'world'})
	print 'Request params:'
	print params
	#发送请求
	response = urllib2.urlopen('?'.join([URL_GET,'%s']) % params)
	#处理响应
	print '>>>>Response Headers:'
	print response.info()

	print '>>>>Status Code:'
	print response.getcode()

	print '>>>>Response Body:'
	print "".join([line for line in response.readlines()])

if __name__ == '__main__':
	print '>>>>use simple urllib2:'
	use_simple_urllib2(URL_IP)

	print '******'*20

	print '>>>>use param urllib2:'
	use_params_urllib2()

	#print '******'*20
	#use_simple_urllib2(URL_USER_AGENT)
	#print '******'*20
	#use_simple_urllib2(URL_ENCODING_UTF8)
