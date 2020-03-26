# coding=utf-8
'''
日志：
0.新建 signs 类。 By wei.wei in 202003041803

说明：
钉钉群聊机器人加签参数计算模块。

使用方法：
import d_key
signs('SECxxxxxx')

input：加签字符串
output：时间与加签组合字符串（请求后半段）

'''

import time
import hmac
import hashlib
import base64
import urllib

class signs(object):
    def __init__(self,sec):
        self.secret = sec

    def __str__(self):
        timestamp = long(round(time.time() * 1000))
        secret = self.secret
        secret_enc = bytes(secret).encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = bytes(string_to_sign).encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.quote_plus(base64.b64encode(hmac_code))
        out_str = '&timestamp='+str(timestamp)+'&sign='+sign
        return str(out_str)
