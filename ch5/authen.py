# -*- coding: utf-8 -*-
import requests

BASE_URL = 'https://api.github.com'

def construct_url(end_point):
	return '/'.join([BASE_URL,end_point])

def basic_auth():
	'''
		基本认证 base64
	'''
	response = requests.get(construct_url('user'),auth=('imoocdemo','imoocdemo123'))
	print response.text
	print response.request.headers

'''
	基本的OAuth
'''
def basic_oauth():
	headers={'Authorization':'token 572982888bafee4595e4c3df253b700c4c848959'}
	response = requests.get(construct_url('user/emails'),headers=headers)
	print response.text
	print response.request.headers
	print response.status_code

from requests.auth import AuthBase

class GithubAuth(AuthBase):

	def __init__(self,token):
		self.token = token

	def __call__(self,r):
		#requests 加 headers
		r.headers['Authorization'] = ' '.join(['token',self.token])
		return r

def oauth_advanced():
	auth = GithubAuth('572982888bafee4595e4c3df253b700c4c848959')
	response = requests.get(construct_url('user/emails'), auth = auth)
	print response.text

#basic_auth()
#basic_oauth()
oauth_advanced()
