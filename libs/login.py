# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: login.py
# @Author: Martin.deng
# @E-mail: 1637754392@qq.com
# @Time: 11月 02, 2022
from common.baseApi import BaseAPI  #
from utils.encrype_data import get_md5_data

# 如果子类里面没有__init__ 方法，那么子类创建实例时候会自动调用父类的__init__
"""
登录接口的特性：
    1.本身接口需要做自动化测试---ddt
    2.需要提取token鉴权值,给后续接口关联
"""


class Login(BaseAPI):  # 继承类
    def login(self, data, get_token=False):
        data['password'] = get_md5_data(data['password'])
        resp_data = self.request_send(data=data)
        # 需要获取token
        if get_token:
            return resp_data['data']['token']
        return resp_data
        # print(resp_data)


if __name__ == '__main__':
    login_data = {'username': 'th0198', 'password': 'xintian'}
    res = Login().login(login_data, get_token=False)
    # print(res)
