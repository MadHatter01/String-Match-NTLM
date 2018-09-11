import requests
from requests_ntlm import HttpNtlmAuth
import re

def match_content(url,username,pswd,match_word):
	username="\\"+username
	try:
		r=requests.get(url,auth=HttpNtlmAuth(username,pswd))
	except Exception as e:
		print("Couldn't get the Request.")

	if(r.status_code)==401:
		raise Exception('Unauthorized Error')
	elif(r.status_code)==404:
		raise Exception('Not Found')
	elif(r.status_code)==400:
		raise Exception('Bad Request')
	elif(r.status_code)==500:
		raise Exception('Internal Server Error')
	elif(r.status_code)==502:
		raise Exception('Bad Gateway')
	elif(r.status_code)==503:
		raise Exception('Service Unavailable')
	elif(r.status_code)==200:
		response=r.text
		count=re.findall(match_word,response)
		if not count:
			print("Failed to match content")
		else:
			print("Content matched successfully")
	else:
		print(r.status_code,'error')
		
