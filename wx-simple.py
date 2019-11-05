#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import sys
def get_token():
  
  url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
  values = {'corpid' : '[企业号的标识]' ,
      'corpsecret':'[管理组凭证密钥]',
       }
  req = requests.post(url, params=values) 
  data = json.loads(req.text)
  return data["access_token"]
  
def send_msg():
    url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+get_token()
    values = json.dumps({
                    'touser':"[企业号中的用户帐号]",
                    'toparty':"[企业号中的部门id]",
                    'msgtype':"[消息类型]",
                    'agentid':"[企业号中的应用id]",
                    'text':{
                                'content':'[消息]'
                    },
                    'safe':'0'
                },ensure_ascii=True)
    print(values)
    data = json.loads(values)
    req = requests.post(url, values) 
  
if __name__ == '__main__':
  send_msg()