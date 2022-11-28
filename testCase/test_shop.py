# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_shop.py
# @Author: Martin.deng
# @E-mail: 1637754392@qq.com
# @Time: 11月 04, 2022
from utils.handle_excel_V3 import get_excel_data  # 工具方法 测试数据
from utils.handle_path import data_path, report_path
import pytest
import os
import allure
from utils.handle_path import config_path
"""
fixture函数的调用：
        -1.没有返回值得fixture函数，直接方法或者类前面使用@pytest.mark.userfixtures('fixture函数名')
        -2.有返回值得fixutre函数，直接使用fixture函数名就行
            -执行fixutre函数里的代码
            -拿到它的返回值
"""
# @pytest.mark.userfixtures('fixture函数名')

@allure.epic('订餐系统')
@allure.feature('店铺模块')
@pytest.mark.shop
class TestShop:
    """ 店铺的测试类"""
    @pytest.mark.parametrize('title,body,exp_data', get_excel_data('我的商铺','listshopping'))
    @allure.story('店铺的查询')
    @pytest.mark.shop_query
    @allure.title('{title}')
    def test_shop_query(self, title, body, exp_data, shop_init):
        shop = shop_init # 获取这个fixture返回值--店铺的实例对象
        res = shop.query(body)
        assert res['code'] == exp_data['code']
        # 1.登录
        # 2.调用店铺查询接口
        # 3.ddt
        # 4.断言
        print('----我这里运行是的是--->', res)

    @pytest.mark.parametrize('title,body,exp_data', get_excel_data('我的商铺', 'updateshopping'))
    @allure.story('店铺的更新')
    @pytest.mark.shop_update
    @allure.title('{title}')
    def test_shop_update(self, title, body, exp_data, shop_init):
        with allure.step('1.登录操作'):
            pass
        with allure.step('2.创建店铺实例'):
            shop = shop_init
        with allure.step('3.更新店铺的id'):
            shop_id = shop.query({"page": 1, "limit": 20})['data']['records'][0]['id']
        with allure.step('4.更新图片信息'):
            image_info = shop.file_upload(os.path.join(data_path,'123.png'))['data']['realFileName']
        with allure.step('5.更新店铺'):
            res = shop.update(body, shop_id, image_info)
        with allure.step('6.断言'):
            assert res['code'] == exp_data['code']


if __name__ == '__main__':
    pytest.main([__file__, '-s', '-m', 'shop_query', '--alluredir', f'{report_path}',
                 '--clean-alluredir'])  # ../outFiles/report/tmp 相对路径
    os.system(f'allure serve {report_path}')
