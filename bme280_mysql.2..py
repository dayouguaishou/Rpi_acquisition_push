# -*- coding: utf-8 -*-
import bme280
import mysql_use
import time#引入时间模块
import sys
import Internal_temperature
import dd_send_msg
import def_ambient

while True :
    if time.localtime(time.time()).tm_sec == 0 :
        try:
            cpu = Internal_temperature.get_cpu_temp()

            temperature,pressure,humidity = bme280.readBME280All()
            
            time.sleep(0.5)
            #gpu = def_ambient.read_ambient()
            gpu = Internal_temperature.get_gpu_temp()#CPU温度与GPU温度同为一个温度，查询无意义，替换为光感

            outprint = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())," CPU温度 : ",str(cpu),"℃"," 光照强度 : ",str(gpu),"lx"," 温度 : ",str(temperature),"℃"," 大气压强 : ",str(round(pressure,2)),"hPa"," 湿度 : ",str(round(humidity,2)),"%"
            SQL = "INSERT INTO temptest (cpu,gpu,error,wendu,shidu,times) VALUES ('{cpu}','{gpu}','{error}', '{wendu}','{shidu}','{shijian}')".format(
                cpu = cpu ,gpu = gpu,error = pressure ,wendu = temperature,shidu = humidity,shijian = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            mysql_use.execute_to_mysql(SQL)
            print ','.join(outprint).replace(',','')
            dd_send_msg.send_Dingmsg(data = {"msgtype": "text", 
                                            "text": {"content": ','.join(outprint).replace(',','')},
                                            })
        except IOError, e:
            print ("Error (0) %d: %s" % (e.args[0], e.args[1]))
            dd_send_msg.send_Dingmsg(data = {"msgtype": "text", 
                                            "text": {"content": "Error (0) %d: %s" % (e.args[0], e.args[1])}, 
                                            "at": {"atMobiles": ["15101690260"], "isAtAll": False},
                                            })
            #sys.exit(0)
        time.sleep(1)
    else:
        time.sleep(1)


