# -*- coding: utf-8 -*-
# @File    : handle_path.py
# @Time    : 11月 07, 2022
# @Author  : Martin.deng
# @E-mail  : 1637754392@qq.com
# @Software: PyCharm
# 处理路径的库，os或者pathlib
import os
# # 先获取项目根目录的路径
print(__file__)
# # 上一层路径../
print(os.path.dirname(__file__))
project_path1 = os.path.dirname(os.path.dirname(__file__))
project_path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('工程根路径--->', project_path2)
#  data数据路径， 绝对路径比较好处理
data_path = os.path.join(project_path2, 'data')
report_path = os.path.join(project_path2, r'outFiles\report\tmp')
config_path = os.path.join(project_path2, 'configs')
log_path = os.path.join(project_path2, r'outFiles\logs')
