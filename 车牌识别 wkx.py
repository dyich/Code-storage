# encoding:utf-8

import requests
import base64
import urllib.request
import os ,stat
'''
车牌识别
'''

url = "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2653272359,224531920&fm=26&gp=0.jpg"
urllib.request.urlretrieve(url,filename="Desktop/new.jpg")

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"
# 二进制方式打开图片文件
f = open('Desktop/new.jpg','rb')
img = base64.b64encode(f.read())
params = {"image":img}
access_token = '24.0792a5692746cd91785d80a7885a7a95.2592000.1585822854.282335-18659015'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())