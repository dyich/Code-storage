# encoding:utf-8
import requests

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"

params = "[{\"image\": \"https://img03.sogoucdn.com/app/a/100520146/fb6f0bace625c60476c6d860f6f7b0d1\", \"image_type\": \"URL\", \"face_type\": \"LIVE\", \"quality_control\": \"LOW\"},{\"image\": \"https://img03.sogoucdn.com/app/a/100520146/ed38b03c32d9c8b3c24018e79351a699\", \"image_type\": \"URL\", \"face_type\": \"LIVE\", \"quality_control\": \"LOW\"}]"
access_token = '24.8004863e80c37173c937b99a56056e86.2592000.1584189234.282335-18464666'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
