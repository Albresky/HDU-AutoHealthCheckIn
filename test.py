#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/11 12:33
# @File    : test.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import time
import json
import hashlib
import base64
from demo import CheckIn
import js2py
from urllib.parse import quote

# check_url = "https://healthcheckin.hduhelp.com/"
# mid_url = "https://api.hduhelp.com/login/direct/cas?clientID=healthcheckin&redirect=https%3A%2F%2Fhealthcheckin.hduhelp.com%2F%23%2Fauth"
# normal_headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
# }
# real_headers = {
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 10; IN2020 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3189 MMWEBSDK/20220105 Mobile Safari/537.36 MMWEBID/1209 MicroMessenger/8.0.19.2080(0x2800133D) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
# }
# MySha1 = ''
# MySession = requests.session()
#
# resp = MySession.get(url=mid_url,headers=normal_headers)
# # print(resp.text)
# soup = BeautifulSoup(resp.text,"lxml")
# _script =soup.find("script",id="password_template").get_text()
#
# RealSoup=BeautifulSoup(_script,"lxml")
# RealLT=RealSoup.find("input",attrs={"type":"hidden","id":"lt"})['value']
# print(RealLT)
#
# import js2py
# with open('des.js', 'r', encoding='UTF-8') as f:
#     js_code = f.read()
# context = js2py.EvalJs()
# context.execute(js_code)
# rsa='20041423'+'shikaiHDU7'+'LT-543127-rxHR4TXBfeupnDtIgP1g6dc0CWMco7-cas'
# result = context.strEnc(rsa,'1','2','3')
# print(result)

# usr=CheckIn()
# print(usr.login('20041423','shikaiHDU7'))
# usr.MySession.request(url=my)
# import js2py
# with open('sign.js', 'r', encoding='UTF-8') as f:
#     js_code = f.read()
# jsFunction = js2py.EvalJs()
# jsFunction.execute(js_code)
# sign = jsFunction.getUnencodeSign("石开", '20041423', '330000', '330100', '330101')
# sign = str(sign)
# print(sign)
# sha = hashlib.sha1(sign.encode('utf-8'))
# encrypts = sha.hexdigest()
# print(encrypts)
# print('石开'.encode('utf-8'))

# username="石开"
# userid ='20041423'
# provice = '330000'
# city = '330100'
# country = '330101'
# btoa_1 = str(base64.b64encode(userid.encode('utf-8')), "utf-8")
# timestamp = str(int(time.time() / 1e3))
# # timestamp='1646982253'
# btoa_2 = str(base64.b64encode(provice.encode('utf-8')), "utf-8")
# value = username + btoa_1 + timestamp + btoa_2 + city + country;
# print(value)
# sha = hashlib.sha1(value.encode('utf-8'))
# encrypts = sha.hexdigest()
# print(encrypts)

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36",
#     "Referer": "https://healthcheckin.hduhelp.com/",
#     "Accept": "application/json, text/plain, */*",
#     "Authorization": "token eaa6174d-3d6c-47d8-99d1-84f540a4d60b",
#     "Content-Type": "application/json, charset=UTF-8",
#     "Cookies": ""
# }
#
# data = {
#     "name": "石开",
#     "timestamp": 1646995092,
#     "province": "330000",
#     "city": "330100",
#     "country": "330101",
#     "answerJsonStr": "{\"ques1\":\"健康良好\",\"ques2\":\"正常在校（未经学校审批，不得提前返校）\",\"ques3\":null,\"ques4\":\"否\",\"ques5\":\"否\",\"ques6\":\"\",\"ques7\":null,\"ques77\":null,\"ques8\":null,\"ques88\":null,\"ques9\":null,\"ques10\":null,\"ques11\":null,\"ques12\":null,\"ques13\":null,\"ques14\":null,\"ques15\":\"否\",\"ques16\":\"否\",\"ques17\":\"无新冠肺炎确诊或疑似\",\"ques18\":\"37度以下\",\"ques19\":null,\"ques20\":\"绿码\",\"ques21\":\"否\",\"ques22\":\"否\",\"ques23\":\"否\",\"ques24\":\"共三针 - 已完成第三针\",\"carTo\":[\"330000\",\"330100\",\"330101\"]}"
# }
# jdata = json.dumps(data)
# print(data)
# print(jdata)
# req = requests.post(url="https://api.hduhelp.com/base/healthcheckin?sign=17bb623e053ad88487adf40496293730f6950921",
#                     headers=headers, json=data)
# print(req.content)

# url="https://api.hduhelp.com/sso?state=daf35b40-faca-4b16-b661-94b7f1952732&ticket=ST-496136-5ovs24oAuTy6Zk2bGeyd-cas"
# token =url.split('?')[-1].split('=')[-1]
# print(token)

str="b27dac1ebc90488d9314bd4e6c14feb7"
print(len(str))