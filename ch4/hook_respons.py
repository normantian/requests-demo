
# -*- coding:utf-8 -*-
import requests

def get_key_info(response,*args,**kwargs):
	'''
		hook
	'''
	print response.headers['Content-Type']
	print response.headers

def main():
	'''
		main
	'''
	requests.get('https://www.baidu.com',hooks=dict(response=get_key_info))

main()