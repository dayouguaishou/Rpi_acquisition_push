# coding=utf-8
'''
日志：
0.新建 send_msg 。 By wei.wei in 202003041829

说明：
钉钉群聊机器人发送模块。

使用方法：
import d_send
send_msg(url,data)


input
url:钉钉机器人接口地址（Webhook+d_key）
data:要发送的信息 data = {}

output：发送返回参数

//发送成功
{"errcode":0,"errmsg":"ok"}

// 消息内容中不包含任何关键词
{"errcode":310000,"errmsg":"keywords not in content"}

// timestamp 无效
{"errcode":310000,"errmsg":"invalid timestamp"}

// 签名不匹配
{"errcode":310000,"errmsg":"sign not match"}

// IP地址不在白名单
{"errcode":310000,"errmsg":"ip X.X.X.X not in whitelist"}

'''

import requests
import json

def send_msg(url,data):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    r = requests.post(url,data = json.dumps(data),headers=headers)
    return r.text

if __name__=="__main__":
   main()
'''    data = {
     "msgtype": "markdown",
     "markdown": {
         "title":"MarkDown 测试",
         "text": "# 一级标题 \n" +
                 "## 二级标题 \n" +
                 "### 三级标题 \n" +
                 "#### 四级标题 \n" +
                 "##### 五级标题 \n" +
                 "###### 六级标题 \n" +
                 "**bold** \n"+
                 "*italic* \n"+
                 "![](http://name.com/pic.jpg) \n"+
                 ">- 无序列表1  \n"+
                 ">- 无序列表2  \n"+
                 "1. 有序列表1  \n"+
                 "2. 有序列表2  \n"+
                 "> A man who stands for nothing will fall for anything.\n"
     }}'''


'''

data = {
    "msgtype": "text", 
    "text": {"content": "我就是我, 是不一样的烟火@156xxxx8827"}, 
    "at": {"atMobiles": ["156xxxx8827", "189xxxx8325"], "isAtAll": false}
}
'''

'''
data = {
    "msgtype": "link", 
    "link": {
        "text": "这个即将发布的新版本，创始人xx称它为“红树林”。
而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红树林”？", 
        "title": "时代的火车向前开", 
        "picUrl": "", 
        "messageUrl": "https://www.dingtalk.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI"
    }
}
'''
'''

'''