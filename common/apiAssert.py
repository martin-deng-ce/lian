# -*- coding: utf-8 -*-
# @File    : apiAssert.py
# @Time    : 11月 07, 2022
# @Author  : Martin.deng
# @E-mail  : 1637754392@qq.com
# @Software: PyCharm
# 封装断言意义: 更好的定位问题，让报错信息可以日志或者allure提醒
# 断言分类 == ！= in ont  equal > <
class ApiAssert:
    """断言类，不需要创建实例 """

    @classmethod  # 类方法
    def api_assert(cls, result, condition, exp_result, assert_info, msg='断言操作'):

        """
        :param result: 实际的返回数据
        :param condition: 判断条件
        :param exp_result: 预期的返回数据
        :param assert_info: 断言的关键信息 code msg
        :param msg: 操作备注
        :return: 返回结果
        """
        try:
            assert_type = {
                "==": result[assert_info] == exp_result[assert_info],
                "!=": result[assert_info] == exp_result[assert_info],
            }
            if condition in assert_type:  # 当前的断言条件在我们的规划的断言类型里
                assert assert_type[condition]
            else:
                AssertionError('你输入的断言类型，不在规划里面，请检查断言条件！')

        except:

            pass
            # 打印日志
