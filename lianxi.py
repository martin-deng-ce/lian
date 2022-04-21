# -*- coding:utf-8 -*-
# @Time:2022/04/22 07:23
# @Author:martin
# @File:test_login.py.py
import os
current_path = os.getcwd()
print(current_path)
t = os.path.dirname(current_path, "test_login")
print(t)

import requests
class Date1():
     def date_location(self,city,key):

         url= "http://apis.juhe.cn/simpleWeather/query"
         par= {
          "city":city,
          "key": key
         }
         result= requests.post(url=url,params=par)

         print(result)
         print(result.text)
         print(type(result))

if __name__ == '__main__':
    d =Date1()
    result = d.date_location("深圳","19927d9690ab707f8494cade6a11034a")





# http://124.223.33.41:7081/mgr/login/login.html 教育系统开源

# http://124.223.33.41:7081/mgr/login/login.html 教育系统开源

import requests
import unittest
class Test_login_01():
    def test_login_success(self,username,password):
        host  = 'http://124.223.33.41:7081/'
        login_path = 'api/mgr/loginReq'
        payload ={
             "username":username,
            "password":password
            }
        req = requests.post(host+login_path,data=payload)
    #判断登录首次成功成功，响应数据
        print(req.status_code)
        print(req.json())
        print(req.text)

if __name__ == '__main__':
    T =Test_login_01()
    req = T.test_login_success("auto","sdfsdfsdf")

import turtle

turtle.pensize(4)
turtle.pencolor('red')

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(1000)

turtle.mainloop()
def f (*args,**kwargs): # 参数和关键字，给函数传入可变长参数
    print(args)
    print(kwargs)
f(6,5,4,a=1,b=2,c=3)

断言assert
print("开始")
assert True
print("结束")

print("开始")
assert False
print("结束")
print("开始")
assert 10 ==10,'条件成立，断言成功'
print("结束")


print("开始")
assert 10 ==11,'条件不成立，断言失败'
print("结束")

yield 和return的区别 ,生成器
def gen_num():
    n = [1,2,3]
    for i  in  n :
        yield i
        #return
        print("继续执行")
print(gen_num())
print(type(gen_num()))
for x in gen_num():
    print(x)

def gen_num():
    n = [1,2,3]
    for i  in  n :
        #yield i
        return i
#         print("继续执行")
# print(gen_num())
# print(type(gen_num()))
# for x in gen_num():
#     print(x)
列表推导式,例子打印从0到20的奇数
list_1 = [i for i  in range (0,20) if i % 2 ==1 ] #列表
print("方法一:",list_1)

#方法二
list_2=[]
for i  in  range(0,20):
    if i % 2 ==1:
        list_2.append(i)
print("方法二:", list_2)
列表排序sort 和sorted的区别
sorted 内建函数，返回的是一个新的list
sort 应用在list 的方法，对已经存在的list进行排序
a = [5,9 ,34,2 ,45,5]
b = sorted(a)
print ("sorted()后的a：",a)
print("b:",b)
a.sort()
a.sort(reverse=True)#降序
print("a.sort()后的a：",a)
-*- coding:utf-8 -*-
@Time:2022/3/19 14:17
@Author:martin
@File:test_login01.py.py
import requests
import json

url='http://apis.juhe.cn/simpleWeather/query'
par = {
    "city":"深圳",
    "key":"19927d9690ab707f8494cade6a11034a"
}
result = requests.get(url=url,params=par)
response = result.json()
# print (type (result.text))
print (result)
print (result.text)

import requests
class Date1():
     def date_location(self,city,key):

         url= "http://apis.juhe.cn/simpleWeather/query"
         par= {
          "city":city,
          "key": key
         }
         result= requests.post(url=url,params=par)

         print(result)
         print(result.text)
         print(type(result))

if __name__ == '__main__':
    d =Date1()
    result = d.date_location("深圳","19927d9690ab707f8494cade6a11034a")

import requests
import json
url = "http://apis.juhe.cn/cxdq/brand"
params = {
    "frist_letter":"B",
    "key":"11a213f7f132b85f6e734d13c6493f7b"
}
result = requests.get(url=url,params=params)
# print(result.text) #文本
res = result.json()

import requests
url = "http://v.juhe.cn/todayOnhistory/queryEvent.php"
params = {
    "date":"3/19",
    "key":"a4075ec965f0e179726ca26e17a02f73"
}
res = requests.get(url=url,params= params)
# print (res.text)#获取返回的结果
data =res.json()['code'] =200#返回json格式状态码
print(data)
# r = res.status_code
# if res.status_code==200;
#     print(res.text)
# else:
#     print("请求出现错误，状态码")

import requests
import json
def test_date(date,key): #定义函数
    url = "http://v.juhe.cn/todayOnhistory/queryEvent.php"
    par= {
        "date":"3/18",
        "key":"a4075ec965f0e179726ca26e17a02f73"
    }
    result  = requests.get(url=url,parmas=par)
    print(result)
    return  result

# print(test_date())  # 获取返回结果
    re = result.json()['code'] # 获取返回状态码
    print(re)

def fun():#函数，类 对象区分
    a =100
    print(a)
    return a +10
print(fun())

import requests
import json
import unittest

class TestDate(unittest.TestCase):
    def __setUp(self):
        print(pass)

    def test_date_01(self):
        url ="http://v.juhe.cn/todayOnhistory/queryEvent.php"
        par = {
            "date":"3/19",
            "key":"a4075ec965f0e179726ca26e17a02f73"
        }
        r1 = requests.get(url,params=par)
        return r1
        print(r1.text) #获取返回的结果
        print(r1.history)
        print(r1.status_code)
        result = r1.json()['code']# 获取状态码
        print(result)
        self.assertEqual(200,result)
        self.assertIn('msg',r1.text)
        # self.assertTrue(''in r1.text)
    # def tearDown(self):
        print("执行测试用例01")
    def test_date_02(self):
        url ="http://v.juhe.cn/todayOnhistory/queryEvent.php"
        par = {
            "date":"3/32",
            "key":"a4075ec965f0e179726ca26e17a02f73"
        }
        r2 = requests.get(url,params=par)
        return r2
        print(r2.text) #获取返回的结果
        print(r2.history)
        print(r2.status_code)
        result2 = r2.json()['code']# 获取状态码
        print(result2)
        self.assertEqual(200,result2)
        self.assertIn('msg',r2.text)
        # self.assertTrue(''in r.text)
    # def tearDown(self):
        print("执行测试用例02")

    def test_date_03(self):
        url = "http://v.juhe.cn/todayOnhistory/queryEvent.php"
        par = {
            "date": "3/0",
            "key": "a4075ec965f0e179726ca26e17a02f73"
        }
        r3 = requests.get(url, params=par)
        return r3
        print(r3.text)  # 获取返回的结果
        print(r3.history)
        print(r3.status_code)
        result3 = r3.json()['code']  # 获取状态码
        print(result3)
        # self.assertEqual(200, result)
        # self.assertIn('msg', r.text)
        assert result3['code'] ==200
        # self.assertTrue(''in r.text)
        assert result3['msg'] =="fail"
        # def tearDown(self):
        print ("执行测试用例03")

if __name__ == '__main__':
    unittest.main()



import requests
import unittest
import json
class TestWeather(unittest.TestCase):
    def setUp(self):
        print("pass")
    def test_weather_01(self):
        print("test_weather_o1")
        url= "http://apis.juhe.cn/simpleWeather/query"
        params={
            "city":"江西",
            "key":"19927d9690ab707f8494cade6a11034a"
        }
        r = requests.get(url=url,params=params)
        return r
        print(r)
        respones =self.result.text
        self.assertEqual(self.r.status_code,200)
        print(self.r.status_code)
        print("登录成功")
    def tearDown(self):
        print("一条测试用例执行完成！")

if __name__ == '__main__':
    unittest.main()

import requests
s = requests.session

class Weather(object):

    def __init__(self,s):
        self.s= s
        self.host = ""
    def weather(self,city,key):
        url = self.host +""
        par = {
            "city":"city"
            "key":"key"
        }
        r = self.s.get(url=url,params=par)
        return r
if __name__ == '__main__':
    import requests
    s = requests.session()
    w = Weather(s)
    r = w.weather("","")
    print(r.text)

import requests
# s = requests.session

class Weather(object):

    # def __init__(self,s):
    #     self.s= s
    #     self.host = ""
    def weather(self,city,key):
        # url = self.host +""
        url = "http://apis.juhe.cn/simpleWeather/query"
        par = {
            "city":city,
            "key":key
        }
        r = requests.get(url=url,params=par)
        return r
if __name__ == '__main__':
    import requests
    w = Weather()
    r = w.weather("九江","19927d9690ab707f8494cade6a11034a")
    print(r.text)


import requests
import unittest
import json
class TestWeather(unittest.TestCase):
    def test_weather_01(self):
        print("test_weather_01")
        url = "http://apis.juhe.cn/simpleWeather/query"
        par = {
            "city":"深圳",
            "key":"19927d9690ab707f8494cade6a11034a"
        }
        r1 = requests.get(url,params=par)
        print(r1.text)
        return r1
        self.assertIn('深圳' in r1.text)

        print("测试成功")
    def test_weather_02(self):
        print("test_weather_02")
        url = "http://apis.juhe.cn/simpleWeather/query"
        par = {
            "city": "江西",
            "key": "19927d9690ab707f8494cade6a11034a"
        }
        r2 = requests.get(url, params=par)
        print(r2.text)
        return r2
        self.assertIn('暂不支持该城市' in r2.text)
        print("测试失败")
    def test_weateher_03(self):
        print("test_weather_03")
        url = "http://apis.juhe.cn/simpleWeather/query"
        par = {
            "city": "九江",
            "key": ""
        }
        r3 = requests.get(url, params=par)
        print(r3.text)
        # result =r3.json()['code']
        # print(r3.status_code)
        return r3
        # self.assertEqual(101,result)
        # self.assertEqual(r3.status_code,10001)
        self.assertIn('错误的请求KEY'in r3.text)
        print("测试通过")

if __name__ == '__main__':
     unittest.main()


#_*_ coding:utf-8 _*_

import requests
import unittest
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class demoTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(4 + 5, 9)

    def test2(self):
        self.assertNotEqual(5 * 2, 10)

    def test3(self):
        self.assertTrue(4 + 5 == 9, "The result is False")

    def test4(self):
        self.assertTrue(4 + 5 == 10, "assertion fails")

    def test5(self):
        self.assertIn(3, [1, 2, 3])

    def test6(self):
        self.assertNotIn(3, range(5))


if __name__ == '__main__':
    unittest.main()




import unittest
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class demoTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(4 + 5, 9)

    def test2(self):
        self.assertNotEqual(5 * 2, 10)

    def test3(self):
        self.assertTrue(4 + 5 == 9, "The result is False")

    def test4(self):
        self.assertTrue(4 + 5 == 10, "assertion fails")

    def test5(self):
        self.assertIn(3, [1, 2, 3])

    def test6(self):
        self.assertNotIn(3, range(5))


if __name__ == '__main__':
    unittest.main()


import pytest

class Test():

    def test01(self):
        print('第一条用例')
        assert 1==1

    def test02(self):
        print('第二条用例')
        assert 2==2

    def test03(self):
        print('第三条用例')
        assert 3==3


if __name__ == '__main__':
    pytest.main()



import unittest
from comment import HTMLTestRunner
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

current_path = os.getcwd()  # 当前文件路径
report_path = os.path.join(current_path, "report")
# 测试报告为result.html
result_path = os.path.join(report_path, "result.html")


# 加载全部用例
def all_case():
    case_path = os.path.join(current_path, "case")  # 用例路径
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="test*.py")
    return discover


def send_email(smtpserver, port, sender, psw, receiver):
    # 写信模板
    msg = MIMEMultipart()
    msg['Subject'] = "招生项目的接口自动化测试报告"
    msg['From'] = sender
    msg['to'] = receiver

    # 通过os获取文件路径
    annex = open(result_path, "r", encoding="utf-8").read()  # 附件，打开并且读取测试报告

    main_body = '<pre><h1>这是XX项目的接口自动化测试报告，请查阅！自动发送的邮件，不用回复。' \
                '<br />联系人：<br />xxx   研发部' \
                '<br />联系电话：132655869<br />邮箱地址：wei@163.com<br />' \
                '联系地址：深圳市南山区xx<br /></h1></pre>'  # 正文的内容

    # 添加正文到容器
    body = MIMEText(main_body, "html", "utf-8")
    msg.attach(body)

    # 添加附件到容器
    att = MIMEText(annex, "base64", "utf-8")
    att["Content-Type"] = "application/octet-sream"
    att["Content-Disposition"] = 'attachment;filename="APos_test_report.html"'  # 附件名称
    msg.attach(att)

    # 连接发送邮件
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


if __name__ == "__main__":

    # 打开文件，把结果写进文件中，w，有内容的话，清空了再写进去
    fp = open(result_path, "wb")  # 打开result.html，把测试结果写进去
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title="测试报告",
                                               description="用例执行情况")
    # 调用all_case函数返回值
    runner.run(all_case())
    # 有开有闭，关闭刚才打开的文件
    fp.close()

    # 发送邮件
    send_email("smtp.qq.com", 465, "3437871062@qq.com", "tdcejfnutrascjee", "1039020476@qq.com")



http://124.223.33.41:7081/mgr/login/login.html


 from faker import Faker
 fake = Faker('zh_CN')
 print(fake.profile())
 print(fake.random.randint(0,100))


import requests
host  = 'http://124.223.33.41:7081/'
login_path = 'api/mgr/loginReq'
payload ={
    "username":"auto",
    "password":"sdfsdfsdf"
}
req = requests.post(host+login_path,data=payload)
#判断登录首次成功成功，响应数据
print(req.status_code)
print(req.json())



import pytest
@pytest.mark.parametrize('n1,n2',[(1,2),(2,2)])
def test_param(n1,n2):
    print("hello,world")
    print('n1',n1)
    print('n2',n2)
    assert n1==n2


# def test_login(): #函数，必须是以test开头
#     print("hello world")
#     assert 1==1   #断言assert 是python的断言关键字

if __name__ == '__main__':
    # main 方法args 参数
    #__ffile__ 文件
    #-s 输入print的内容捕获信息
    #-v 详细日志
    pytest.main(['-sv',__file__])

#argsname
#argsvalue
#装饰器的用法

import pytest
import requests
host  ='http://124.223.33.41:7081/'
#装饰器的用法
@pytest.mark.parametrize('username,password','retcode',[('auto','sdfsdfsdf',0),('auto','sdfsdfsdf1',1)])
def  test_api_login(username,password,retcode):
    login_path = 'api/mgr/loginReq'
    payload ={
    "username":"username",
    "password":"password"
    }
    req=requests.post(host+login_path,data=payload)
#判断登录首付成功，响应数据
    print(req.status_code)
    print(req.json())
    # assert req.json() {'retcode':0}==req.json()
    assert req.json(){'retcode'} == retcode


    assert req.status_code ==200
if __name__ == '__main__':
    pytest.main(['-sv', __file__])
import os

file = "D:\\script\\python_script\\case\\test.txt" # \转义符 同一个文件目录下的操作
f = open(file,'r',encoding='utf-8')# utf-8编码方式打开文件
list = f.readlines()
print(list)
data =f.read() # 操作文件
f.close()  #关闭文件
print(data) #
with open(file,'r',encoding='utf-8') as f:
    print(f.read())

http://124.223.33.41:7081/mgr/login/login.html 教育系统开源

import requests
import unittest
class Test_login_01():
    def test_login_success(self,username,password):
        host  = 'http://124.223.33.41:7081/'
        login_path = 'api/mgr/loginReq'
        payload ={
             "username":username,
            "password":password
            }
        req = requests.post(host+login_path,data=payload)
    #判断登录首次成功成功，响应数据
        print(req.status_code)
        print(req.json())

if __name__ == '__main__':
    T =Test_login_01()
    req = T.test_login_success("auto","sdfsdfsdf")


import requests
import unittest
class Test_login_01(unittest.TestCase):
    def setUp(self):
        pass
        print("测试开始")

    def test_login_success_01(self):
        host  = 'http://124.223.33.41:7081/'
        login_path = 'api/mgr/loginReq'
        payload ={
            "username":"auto",
            "password":"sdfsdfsdf"
            }
        req = requests.post(host+login_path,data=payload)
       #判断登录首次成功成功，响应数据
        assert req.status_code ==200
        self.assertEqual(200,req.status_code)#断言
        # self.assertTrue("登录成功"in req.text)
        print(req.status_code)
        print(req.json())

    def test_login_fail_01(self):
        host = 'http://124.223.33.41:7081/'
        login_path = 'api/mgr/loginReq'
        payload = {
            "username": "",
            "password": "sdfsdfsdf"
        }
        req = requests.post(host + login_path, data=payload)
        # 判断登录首次成功成功，响应数据
        assert req.status_code ==200
        self.assertTrue("用户或者密码错误" in req.text)
        print(req.status_code)
        print(req.json())

    def test_login_fail_is_null(self):
        host = 'http://124.223.33.41:7081/'
        login_path = 'api/mgr/loginReq'
        payload = {
            "username": "",
            "password": ""
        }
        req = requests.post(host + login_path, data=payload)
        # 判断登录首次成功成功，响应数据
        assert req.status_code ==200
        self.assertTrue(1 in req.text)
        print(req.status_code)
        print(req.json())

    def tearDown(self):
        pass
        print("测试结束")


if __name__ == '__main__':
  unittest.main()




import requests
import json

#甄选产品
#OpenAcctGetDetailRecord 开户接口
url='https://test.ciccten.com/fcgi/common.fcgi?cmdname=OpenAcctGetDetailRecord&t=1649603054779'
#header= {Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1}
par = {
    "app_ver":"2.0.1-202204080301",
    "platform":"weixin",
    "device_id":"3a3dfac7818b5f16ab3316c361435e81",
    "broker_id":2
}
result = requests.get(url=url,params=par)
#response = result.json()
# print (type (result.text))
print (result)
print (result.text)
#GetPartnerAuthInfo 接口
url='https://test.ciccten.com/jt-qa/simuLogin'
par = {
    "app_ver":"2.0.1-202204080301",
    "platform":"weixin",
    "device_id":"3a3dfac7818b5f16ab3316c361435e81",
    "broker_id":2,
    "dummy":""}
result = requests.get(url=url,params=par)
#response = result.json()
# print (type (result.text))
print (result)
print (result.text)


#GetUserTraceByTraceId 留痕接口
url='https://test.ciccten.com/jt-qa/simuLogin'
par = {"app_ver":"2.0.1-202204080301",
       "platform":"weixin",
       "device_id":"3a3dfac7818b5f16ab3316c361435e81",
       "trace_ids":["4"]

    }
result = requests.get(url=url,params=par)
#response = result.json()
# print (type (result.text))
print (result)
print (result.text)

##GetUserTraceByTraceId 留痕接口
url = 'https://test.ciccten.com/jt-qa/simuLogin'
par = {"app_ver": "2.0.1-202204080301",
       "platform": "weixin",
       "device_id": "3a3dfac7818b5f16ab3316c361435e81",
       "trace_ids": ["4"]

       }
result = requests.get(url=url, params=par)
# response = result.json()
# print (type (result.text))
print(result)
print(result.text)

#BatchGetRedPointList 红点接口
url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=BatchGetRedPointList&t=1649603054988'
par = {"app_ver":"2.0.1-202204080301",
       "platform":"weixin",
       "device_id":"3a3dfac7818b5f16ab3316c361435e81",
       "rp_pos_id_list":["jt_my_asset","jt_activity_page_entrance","jt_fuli_center"]

       }
result = requests.get(url=url, params=par)
# response = result.json()
# print (type (result.text))
print(result)
print(result.text)

#BatchGetRedPointList 分享页面接口
url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=GetShareWebPage&t=1649603055000'
par = {"app_ver":"2.0.1-202204080301",
       "platform":"weixin",
       "device_id":"3a3dfac7818b5f16ab3316c361435e81",
       "scenes":1

       }
result = requests.get(url=url, params=par)
# response = result.json()
# print (type (result.text))
print(result)
print(result.text)


#QueryUserWhiteLists 白名单接口
url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=QueryUserWhiteLists&t=1649603055018'
par = {"app_ver":"2.0.1-202204080301",
       "platform":"weixin",
       "device_id":"3a3dfac7818b5f16ab3316c361435e81",
       "white_list_ids":[2000,7031]

       }
result = requests.get(url=url, params=par)
# response = result.json()
# print (type (result.text))
print(result)
print(result.text)


#GetToufang 投放接口
url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=GetToufang&t=1649603055023'
par = {"app_ver":"2.0.1-202204080301",
       "platform":2,
       "device_id":"3a3dfac7818b5f16ab3316c361435e81",
       "page_id":8

       }
result = requests.get(url=url, params=par)
# response = result.json()
# print (type (result.text))
print(result)
print(result.text)


#GetReserveIndexInfo 投顾信息接口
url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=GetReserveIndexInfo&t=1649603055059'
par = {"app_ver":"2.0.1-202204080301",
       "platform":"weixin",
       "device_id":"3a3dfac7818b5f16ab3316c361435e81",
       "dummy":""

       }
result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #GetUserKeyValue 登录value接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=GetUserKeyValue&t=1649603055160'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "cache_key_list":["NewClientCurtain"]
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #GetArticleListByCategoryId 咨询文章接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=GetArticleListByCategoryId&t=1649603055172'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "category_id":56,
#        "expect_count":2,
#        "last_index":0
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #GetCustomMadeProductList 50货架接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=GetCustomMadeProductList&t=1649603055177'
# par = {"app_ver":"2.0.1-202204080301","platform":"weixin","device_id":"3a3dfac7818b5f16ab3316c361435e81","visible_channel":2
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #TestUserHave50Product 分是否持有50接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=TestUserHave50Product&t=1649603055194'
# par = {"app_ver":"2.0.1-202204080301","platform":"weixin","device_id":"3a3dfac7818b5f16ab3316c361435e81"
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #GetUserTradeBuyAction  是否买过产品接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=GetUserTradeBuyAction&t=1649603056807'
# par = {"app_ver":"2.0.1-202204080301","platform":"weixin","device_id":"3a3dfac7818b5f16ab3316c361435e81"
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #GetFrontUnifiedConfig 配置接口
# url = ' https://test.ciccten.com/fcgi/common.fcgi?cmdname=GetFrontUnifiedConfig&t=1649603057187'
# par = {"app_ver":"2.0.1-202204080301","platform":"weixin","device_id":"3a3dfac7818b5f16ab3316c361435e81","config_keys":["jv_config_product_act_tip"]
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #GetUserOperationInfo 运营接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=GetUserOperationInfo&t=1649603058155'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "page_source":"shelves-index"
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
# #GetGoodsShelvesProductList 货架页接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=GetGoodsShelvesProductList&t=1649603054558'
# par = {"visible_channel":2
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
#
#
#
# #定制服务页面
#
# #QueryUserWhiteLists 分享页面接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=QueryUserWhiteLists&t=1649603055018'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "white_list_ids":[2000,7031]
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
# #QueryUserWhiteLists 分享页面接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=QueryUserWhiteLists&t=1649603055018'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "white_list_ids":[2000,7031]
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #QueryUserWhiteLists 分享页面接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=QueryUserWhiteLists&t=1649603055018'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "white_list_ids":[2000,7031]
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #QueryUserWhiteLists 分享页面接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=QueryUserWhiteLists&t=1649603055018'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "white_list_ids":[2000,7031]
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #QueryUserWhiteLists 分享页面接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=QueryUserWhiteLists&t=1649603055018'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "white_list_ids":[2000,7031]
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #QueryUserWhiteLists 分享页面接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=QueryUserWhiteLists&t=1649603055018'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "white_list_ids":[2000,7031]
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #QueryUserWhiteLists 分享页面接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=QueryUserWhiteLists&t=1649603055018'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "white_list_ids":[2000,7031]
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #QueryUserWhiteLists 分享页面接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=QueryUserWhiteLists&t=1649603055018'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "white_list_ids":[2000,7031]
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #QueryUserWhiteLists 分享页面接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=QueryUserWhiteLists&t=1649603055018'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "white_list_ids":[2000,7031]
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
# #QueryUserWhiteLists 分享页面接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=QueryUserWhiteLists&t=1649603055018'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "white_list_ids":[2000,7031]
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #QueryUserWhiteLists 分享页面接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=QueryUserWhiteLists&t=1649603055018'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "white_list_ids":[2000,7031]
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #QueryUserWhiteLists 分享页面接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=QueryUserWhiteLists&t=1649603055018'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "white_list_ids":[2000,7031]
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #QueryUserWhiteLists 分享页面接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=QueryUserWhiteLists&t=1649603055018'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "white_list_ids":[2000,7031]
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)
#
#
# #QueryUserWhiteLists 分享页面接口
# url = 'https://test.ciccten.com/fcgi/common.fcgi?cmdname=QueryUserWhiteLists&t=1649603055018'
# par = {"app_ver":"2.0.1-202204080301",
#        "platform":"weixin",
#        "device_id":"3a3dfac7818b5f16ab3316c361435e81",
#        "white_list_ids":[2000,7031]
#
#        }
# result = requests.get(url=url, params=par)
# # response = result.json()
# # print (type (result.text))
# print(result)
# print(result.text)



import requests
import json
import pytest
def test_01():
    url='http://apis.juhe.cn/simpleWeather/query'
    par = {
    "city":"深圳",
    "key":"19927d9690ab707f8494cade6a11034a"
        }
    result = requests.get(url=url,params=par)
    response = result.json()
# print (type (result.text))
    print (result)
    print (result.text)
if __name__ == '__main__':
    pytest.main()

import random
a =random.randint(0,1000) #随机整数
print(a)
m = random.random()#随机浮点数
print(m)


import requests
class Date1():
     def date_location(self,city,key):

         url= "http://apis.juhe.cn/simpleWeather/query"
         par= {
          "city":city,
          "key": key
         }
         result= requests.post(url=url,params=par)

         print(result)
         print(result.text)
         print(type(result))

if __name__ == '__main__':
    d =Date1()
    result = d.date_location("深圳","19927d9690ab707f8494cade6a11034a")

import requests
import json
url = "http://apis.juhe.cn/cxdq/brand"
params = {
    "frist_letter":"B",
    "key":"11a213f7f132b85f6e734d13c6493f7b"
}
result = requests.get(url=url,params=params)
# print(result.text) #文本
res = result.json()

import requests
url = "http://v.juhe.cn/todayOnhistory/queryEvent.php"
params = {
    "date":"3/19",
    "key":"a4075ec965f0e179726ca26e17a02f73"
}
res = requests.get(url=url,params= params)
# print (res.text)#获取返回的结果
data =res.json()['code'] =200#返回json格式状态码
print(data)
r = res.status_code
if res.status_code==200;
    print(res.text)
else:
    print("请求出现错误，状态码")

import requests
import json
def test_date(date,key): #定义函数
    url = "http://v.juhe.cn/todayOnhistory/queryEvent.php"
    par= {
        "date":"3/18",
        "key":"a4075ec965f0e179726ca26e17a02f73"
    }
    result  = requests.get(url=url,parmas=par)
    print(result)
    return  result

# print(test_date())  # 获取返回结果
    re = result.json()['code'] # 获取返回状态码
    print(re)

def fun():#函数，类 对象区分
    a =100
    print(a)
    return a +10
print(fun())

import requests
import json
import unittest

class TestDate(unittest.TestCase):
    # def __setUp(self):
    #     print(pass)

    def test_date_01(self):
        url ="http://v.juhe.cn/todayOnhistory/queryEvent.php"
        par = {
            "date":"3/19",
            "key":"a4075ec965f0e179726ca26e17a02f73"
        }
        r1 = requests.get(url,params=par)
        return r1
        print(r1.text) #获取返回的结果
        print(r1.history)
        print(r1.status_code)
        result = r1.json()['code']# 获取状态码
        print(result)
        self.assertEqual(200,result)
        self.assertIn('msg',r1.text)
        # self.assertTrue(''in r1.text)
    # def tearDown(self):
        print("执行测试用例01")
    def test_date_02(self):
        url ="http://v.juhe.cn/todayOnhistory/queryEvent.php"
        par = {
            "date":"3/32",
            "key":"a4075ec965f0e179726ca26e17a02f73"
        }
        r2 = requests.get(url,params=par)
        return r2
        print(r2.text) #获取返回的结果
        print(r2.history)
        print(r2.status_code)
        result2 = r2.json()['code']# 获取状态码
        print(result2)
        self.assertEqual(200,result2)
        self.assertIn('msg',r2.text)
        # self.assertTrue(''in r.text)
    # def tearDown(self):
        print("执行测试用例02")

    def test_date_03(self):
        url = "http://v.juhe.cn/todayOnhistory/queryEvent.php"
        par = {
            "date": "3/0",
            "key": "a4075ec965f0e179726ca26e17a02f73"
        }
        r3 = requests.get(url, params=par)
        return r3
        print(r3.text)  # 获取返回的结果
        print(r3.history)
        print(r3.status_code)
        result3 = r3.json()['code']  # 获取状态码
        print(result3)
        # self.assertEqual(200, result)
        # self.assertIn('msg', r.text)
        assert result3['code'] ==200
        # self.assertTrue(''in r.text)
        assert result3['msg'] =="fail"
        # def tearDown(self):
        print ("执行测试用例03")

if __name__ == '__main__':
    unittest.main()



import requests
import unittest
import json
class TestWeather(unittest.TestCase):
    def setUp(self):
        print("pass")
    def test_weather_01(self):
        print("test_weather_o1")
        url= "http://apis.juhe.cn/simpleWeather/query"
        params={
            "city":"江西",
            "key":"19927d9690ab707f8494cade6a11034a"
        }
        r = requests.get(url=url,params=params)
        return r
        print(r)
        respones =self.result.text
        self.assertEqual(self.r.status_code,200)
        print(self.r.status_code)
        print("登录成功")
    def tearDown(self):
        print("一条测试用例执行完成！")

if __name__ == '__main__':
    unittest.main()

import requests
s = requests.session

class Weather(object):

    def __init__(self,s):
        self.s= s
        self.host = ""
    def weather(self,city,key):
        url = self.host +""
        par = {
            "city":"city"
            "key":"key"
        }
        r = self.s.get(url=url,params=par)
        return r
if __name__ == '__main__':
    import requests
    s = requests.session()
    w = Weather(s)
    r = w.weather("","")
    print(r.text)

import requests
# s = requests.session

class Weather(object):

    # def __init__(self,s):
    #     self.s= s
    #     self.host = ""
    def weather(self,city,key):
        # url = self.host +""
        url = "http://apis.juhe.cn/simpleWeather/query"
        par = {
            "city":city,
            "key":key
        }
        r = requests.get(url=url,params=par)
        return r
if __name__ == '__main__':
    import requests
    w = Weather()
    r = w.weather("九江","19927d9690ab707f8494cade6a11034a")
    print(r.text)


import requests
import unittest
import json
class TestWeather(unittest.TestCase):
    def test_weather_01(self):
        print("test_weather_01")
        url = "http://apis.juhe.cn/simpleWeather/query"
        par = {
            "city":"深圳",
            "key":"19927d9690ab707f8494cade6a11034a"
        }
        r1 = requests.get(url,params=par)
        print(r1.text)
        return r1
        self.assertIn('深圳' in r1.text)

        print("测试成功")
    def test_weather_02(self):
        print("test_weather_02")
        url = "http://apis.juhe.cn/simpleWeather/query"
        par = {
            "city": "江西",
            "key": "19927d9690ab707f8494cade6a11034a"
        }
        r2 = requests.get(url, params=par)
        print(r2.text)
        return r2
        self.assertIn('暂不支持该城市' in r2.text)
        print("测试失败")
    def test_weateher_03(self):
        print("test_weather_03")
        url = "http://apis.juhe.cn/simpleWeather/query"
        par = {
            "city": "九江",
            "key": ""
        }
        r3 = requests.get(url, params=par)
        print(r3.text)
        # result =r3.json()['code']
        # print(r3.status_code)
        return r3
        # self.assertEqual(101,result)
        # self.assertEqual(r3.status_code,10001)
        self.assertIn('错误的请求KEY'in r3.text)
        print("测试通过")

if __name__ == '__main__':
     unittest.main()


_*_ coding:utf-8 _*_

import requests
import unittest
# import sys
#
# reload(sys)
# sys.setdefaultencoding("utf-8")


class demoTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(4 + 5, 9)

    def test2(self):
        self.assertNotEqual(5 * 2, 10)

    def test3(self):
        self.assertTrue(4 + 5 == 9, "The result is False")

    def test4(self):
        self.assertTrue(4 + 5 == 10, "assertion fails")

    def test5(self):
        self.assertIn(3, [1, 2, 3])

    def test6(self):
        self.assertNotIn(3, range(5))


if __name__ == '__main__':
    unittest.main()




import unittest
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class demoTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(4 + 5, 9)

    def test2(self):
        self.assertNotEqual(5 * 2, 10)

    def test3(self):
        self.assertTrue(4 + 5 == 9, "The result is False")

    def test4(self):
        self.assertTrue(4 + 5 == 10, "assertion fails")

    def test5(self):
        self.assertIn(3, [1, 2, 3])

    def test6(self):
        self.assertNotIn(3, range(5))


if __name__ == '__main__':
    unittest.main()


import pytest

class Test():

    def test01(self):
        print('第一条用例')
        assert 1==1

    def test02(self):
        print('第二条用例')
        assert 2==2

    def test03(self):
        print('第三条用例')
        assert 3==3


if __name__ == '__main__':
    pytest.main()

import unittest
import ddt

# 测试数据
datas = [ {"user": "admin", "psw": "123", "result": "true"},
        {"user": "admin1", "psw": "1234", "result": "true"},
        {"user": "admin2", "psw": "1234", "result": "true"},
        {"user": "admin3", "psw": "1234", "result": "true"},
        {"user": "admin4", "psw": "1234", "result": "true"},
        {"user": "admin5", "psw": "1234", "result": "true"},
        {"user": "admin6", "psw": "1234", "result": "true"},
        {"user": "admin7", "psw": "1234", "result": "true"},
        {"user": "admin8", "psw": "1234", "result": "true"},
        {"user": "admin9", "psw": "1234", "result": "true"},
        {"user": "admin10", "psw": "1234", "result": "true"},
        {"user": "admin11", "psw": "1234", "result": "true"}]

@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(*datas)
    def test_(self, d):
        """上海-悠悠：{0}"""
        print("测试数据：%s" % d)

if __name__ == "__main__":
    unittest.main()


import pytest

@pytest.fixture()
def test1():
    a = 'leo'
    return a


def test2(test1):
    assert test1 == 'leo'


if __name__ == '__main__':
    pytest.main('-q test_fixture.py')

import requests  #开源平台工具20220421
host  = 'https://demo.metersphere.com/'
login_path = 'isLogin'
payload ={
    "username":"demo",
    "password":"P@ssw0rd123"
}
req = requests.post(host+login_path,data=payload)
#判断登录首付成功，响应数据
print(req.status_code)


import requests
url = "https://demo.metersphere.com/isLogin"
# header = {"Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666"} #请求头
par= {
    "lastUser":"demo",
    "redirectUrl":"/setting",
    "project_name":"金融P2P",
    "changePassword":"false",
    "project_id":"f826b475-d8ad-4733-b207-c933f561e9eb",
    "workspace_id": "069e4b3e-cfe2-4066-8c1d-1ce8aae8a694"
}
req = requests.post(url=url,params=par)
print(req.text)
print(req.status_code)
