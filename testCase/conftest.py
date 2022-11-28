# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: conftest.py
# @Author: Martin.deng
# @E-mail: 1637754392@qq.com
# @Time: 11月 04, 2022
from configs.conf import NAME_PWD
from libs.login import Login
from libs.shop import Shop
import pytest
# @pytest.fixture(scope='session',autouse=True,params= ['第1次运行>>','第2次运行>>>'])
# def start_running(request):
#     print(f'----我准备运行了---测试开始{request.param}')
#     yield
#     print('---这里可以写数据清除的代码')
#登操作的初始化操作
@pytest.fixture(scope= 'session')
def login_init():
    print('---用户登录操作---')
    # 登录操作
    token = Login().login(NAME_PWD, get_token=True)
    yield token # 有返回值的作用
    print('---退出操作---')

# 创建店铺实例操作
# 技术点1:不同的fixture可以相互调用，下一个fixture函数定义时候，参数写上一个fixture函数名
#技术点2：如何使用 上一个fixture的返回值，下一个fixture函数里面直接使用上一个fixture函数名就是它的返回值

@pytest.fixture(scope= 'session')
def shop_init(login_init):
    print('---创建店铺实例---')
    # 1.登录操作
    # 2.传递token--创建店铺实例
    shop = Shop(login_init)
    yield shop


