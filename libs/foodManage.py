# -*- coding: utf-8 -*-
# @File    : foodManage.py
# @Time    : 11月 16, 2022
# @Author  : Martin.deng
# @E-mail  : 1637754392@qq.com
# @Software: PyCharm
# 食品管理
# 增
from common.baseApi import BaseAPI
from libs.login import Login
from libs.shop import Shop
import json


class FoodManage(BaseAPI):
    def category_list(self, id):
        """
        :param id:
        :return:
        """
        return self.request_send(id=id)

    def add(self,inData):
        if inData.get('attributes'):
            inData


    # 查询
    def query_food(self):
        pass

    # 修改
    def update_food(self):
        pass

    # 删除
    def deleter_food(self):
        pass

if __name__ == '__main__':
    login_data = {'username': 'th0198', 'password': 'xintian'}
    token = Login().login(login_data, get_token=False)
    resp = FoodManage(token).category_list()
