print('很高兴认识你，下面就跟我聊天吧')
while True:
    date = input ('\n')
    import requests
    r = requests.get("http://api.tianapi.com/txapi/robot/index?key=71668f903b08350eb7b9a6947c631817&question={获取值}".format(获取值=date))
    shuju = r.json()
    print (str(shuju)[75:-3])
    #print(shuju)