# coding=utf-8
'''
日志：
0.新建测试代码。 By wei.wei in 202003041850
1.简化为函数，使用时导入填参即可。 By wei.wei in 202003191148

说明：
修改为调用参数的函数。

使用方法：
调用send_Dingmsg函数直接在程序中运行
'''

import d_key
import d_send


def send_Dingmsg(url = 'https://oapi.dingtalk.com/robot/send?access_token=22143e93ca5d6103700a3ab15857781d4dfb984ba29c7a406247b35d143bb7fd',
                keys_str = 'SEC2b7be95a5ff3c2ff1a65c79ecf3eefeeeb20a73558be0fbc670041a623c45f94',
                    data = {"msgtype": "text","text": {"content": "这是一条测试消息"},}):
    keys = str(d_key.signs(keys_str))
    send_url = url+keys
    return (d_send.send_msg(send_url,data))#返回服务参数


if __name__=="__main__":
   main()
#send_Dingmsg()
