import requests
import urllib.request
import json
import gzip


r = requests.get("http://api.tianapi.com/txapi/ncovcity/index?key=71668f903b08350eb7b9a6947c631817")
shuju = r.json()
print (str(shuju))
#print(shuju)
date = input ('\n')