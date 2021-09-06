import requests
import time

url = 'https://msg.going-link.com/'     #这里url末尾要有'/'
with open("SpringBoot信息泄露目录字典.txt", 'r') as web:
    webs = web.readlines()
w = open('easyresult.txt', 'w+')
for web in webs:
    web = web.strip()
    u = url + web
    response = requests.get(u)
    
    #print("url为:"+u)
    print("url为:" + u + ' ' + "状态为:%d"%response.status_code + ' ' + "content-length为:" + str(len(response.content)))
    time.sleep(5)       #想睡多久看自己~
    w.write("url为:" + u + ' ' + "状态为:%d"%response.status_code + ' ' + "content-length为:" + str(len(response.content)) + '\n')
