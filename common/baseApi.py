# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: baseApi.py
# @Author: Martin.deng
# @E-mail: 1637754392@qq.com
# @Time: 11月 02, 2022
import inspect
import requests
from configs.conf import HOST
from utils.handle_yml import get_yml_data #工具方法
class BaseAPI:
    # def __init__(self,user_token= None,**kwargs):
    #     self.data = ''
    #     if user_token:
    #         self.header = {'':user_token}
    #         self.header.update(kwargs)
    #     else:
    #         self.header =None
    #     print('模块的请求头--->',)
    """接口的基础类,所有的业务类都需要继承的"""
    # 每一个业务都会去继承这个基类，都会创建实例，拿到自己的接口实例
    def __init__(self, user_token=None, **kwargs):
        self.data = get_yml_data('../configs/apiPathConfig.yml')[self.__class__.__name__]  # 怎么取？
        #print('当前是哪一个对象--->',self)
        #print(self.data)
        # 不是所有模块都需要都运传递token,只有后续业务模块才需要关联token
        if user_token:# 业务模块
            self.header = {'Authorization': user_token}
            self.header.update(kwargs)   #  如果有一些特定模块有其他的头的参数 比如uid可以再增加
        else:  # 登录模块
            self.header = None
        # print('---模块的请求头---->', self.header)

    # 公共的发送方法：请求方法、url
    """
    # 一个请求里对于的测试用例，不变是，请求方法，url、请求头；变的是哪一个，参数、预期响应
    # 执行用例的自动化测试：使用ddt 
     ---excel
     ---yaml 
     把url和method单独配置yaml 
    """
    def request_send(self, id='', **kwargs):  # **定义关键字变量--装包
        # requests.request(method=method,url=url,**kwargs) #** 展开关键字参数--解
        try:
            __config_data = self.data[inspect.stack()[1][3]]
            # print(__config_data)
            resp = requests.request(
                method=__config_data['method'],
                url= f'{HOST}{__config_data["path"]}{id}',
                headers=self.header,
                **kwargs)  # **站看关键字参数-解包
            return resp.json()
        except:
            pass
            print('----请求有错误，请检查---')
            # 日志处理
    # -----封装增删改查方法-------
    # 为什么要封装：我们在BaseAPI这个父类封装了增删改查方法，后续其他业务模块继承
    # 如果子类没有特殊需求，之间不写具体的增删改查，去继承父类方法
    # 如果子类有特殊需求，重写父类，增删改查

    # 查询方法
    def query(self, data):
        return self.request_send(params=data)
    # 增加方法:可以是json 可以是表单

    def add(self, **kwargs):
        return self.request_send(**kwargs)

    # 修改方法
    def update(self, id ='',  **kwargs):
        return self.request_send(id=id, **kwargs)

    # 删除方法
    def delete(self,  id):
        return self.request_send(id=id)

    # 文件上传接口
    """
    文件上传接口需要传递的参数；给哪一个变量，文件名，文件类型、文件本身的数据
    {'变量名':(文件名，文件本身数，文件类型)}
    {'file':('123.png',open(文件路径，'rb','image/png')}
    """
    # ../data/123.png
    def file_upload(self, file_path):
        # 文件名
        file_name = file_path.split('/')[-1]
        file_type = file_path.split('.')[-1]
        user_file = {'file': (file_name, open(file_path, 'rb'), file_type)}
        return self.request_send(files=user_file)







if __name__ == '__main__':
    def test():
        print('---执行test函数---')
        for one in inspect.stack():
            print(one)
        print('调用我的函数名是', inspect.stack()[1])
        for one in inspect.stack()[1]:
            print(one)
        print('调用我的函数名是', inspect.stack()[1][3])

    def a():
        test()
    a()