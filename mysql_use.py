#coding: utf-8
'''
#cnf.ini
[db]
db_host = 192.168.137.137
db_port = 3306
db_user = root
db_pass = root@123
db_name = test
'''
'''
函数名称：cnfdb(filename = "cnf.ini")
说明：从filename文件中获取mysql连接参数
返回：dictionary（字典）-cnfg_dict{}

函数名称：select_MYSQL(SQL)
说明：查询数据库
返回：数据集（元组）-datas() 或输出错误信息

函数名称：select_datas_column(datas,num = 0)
说明：查询数据集某一列（num）num>=0
返回：数据列（list）-list[]

函数名称：execute_to_mysql(SQLS)
说明：执行SQL语句
返回：无 或输出错误信息
'''

import MySQLdb as mdb
import ConfigParser
import sys,os

def cnfdb(filename = "cnf.ini"):
    cf = ConfigParser.ConfigParser()
    cf.read(os.path.dirname(os.path.abspath(__file__))+'/'+filename)
    cnfg = []
    cnfname = ["db_host","db_user","db_pass","db_name","db_port"]
    for i in range(len(cnfname)):
        cnfg.append(cf.get("db", cnfname[i]).decode('gbk').encode('utf-8'))
    cnfg_dict = dict(zip(cnfname, cnfg))
    return cnfg_dict

def select_MYSQL(SQL):
    conf = cnfdb()
    try:
        conn = mdb.connect(host=conf["db_host"] , port = int(conf["db_port"]) , user=conf["db_user"], passwd=conf["db_pass"], db=conf["db_name"], charset='utf8')
        cursor = conn.cursor()
        cursor.execute(SQL)
        nums = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
    except IOError, e:
        print "Error (0) %d: %s" % (e.args[0], e.args[1])
        sys.exit(0)
    return nums

def select_datas_column(datas,num = 0):
    list = []
    for i in range(len(datas)):
         list.append(datas[i][num])
    return list


def execute_to_mysql(SQLS):
    conf = cnfdb()
    try:
        conn = mdb.connect(host=conf["db_host"] , port = int(conf["db_port"]) , user=conf["db_user"], passwd=conf["db_pass"], db=conf["db_name"], charset='utf8')
        cursor = conn.cursor()
        cursor.execute(SQLS)
        conn.commit()
        cursor.close()
        conn.close()
    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)



#datas = select_MYSQL(SQL = "SELECT * FROM weixin ")

#print select_datas_column(datas,2)
