# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: test_login.py
# @Author: Martin.deng
# @E-mail: 1637754392@qq.com
# @Time: 10月 31, 2022
import pytest
from libs.login import Login  # 接口路径
from common.apiAssert import ApiAssert
from utils.handle_excel_V2 import get_excel_data  # 工具方法 测试数据
# from utils.handle_yml import get_case_data
from utils.handle_path import  data_path
import allure
import os


@allure.epic('点餐系统')
@allure.feature('登录模块')
class TestLogin:
    """登录的测试类"""

    # @pytest.mark.parametrize(get_case_data('../data/loginCase.yml'))
    @pytest.mark.parametrize('title,body,resp_exp',
                             get_excel_data(os.path.join(data_path,'Delivery_System_V1.5.xls'), '登录模块', 'Login', '标题', '请求参数',
                                            '响应预期结果'))
    @allure.story('登录接口')
    @allure.title('标题')
    def test_login(self, title, body, resp_exp):
        """登录的测试方法"""
        # 1.执行请求发送
        res = Login().login(body)
        # 2.断言
        # assert res['msg'] == resp_exp['msg']
        ApiAssert.api_assert(res, '==', resp_exp, 'msg', msg='登录接口的断言')


if __name__ == '__main__':
    pytest.main([__file__, '-s', '--alluredir', '../outFiles/report/tmp', '--clean-alluredir'])
    os.system('allure serve ../outFiles/report/tmp')