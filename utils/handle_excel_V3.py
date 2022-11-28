# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: handle_excel.py
# @Author: Martin.deng
# @E-mail: 1637754392@qq.com
# @Time: 10月 31, 2022
import xlrd
import os
import json
from utils.handle_yml import get_yml_data
from utils.handle_path import config_path,data_path
"""
---------------V2.0-----------------
优化需求：
  -1. 不能选择某一个，或者某些用例执行
  -2.函数需要传递的参数太多了
解决方案：
  -1.用例筛选
    run_case场景分类：
       -1.全部运行 12345
       -2.只运行某一个 1
       -3.连续的几个，或者一段 345
       -4.混合的场景，有个或者某一段 1,345
  -2.是否可以考虑配置文件 yml
"""
def get_excel_data(sheet_name,case_name,run_case=None):
    """
    :param file_path: 文件路径
    :param sheet_name:
    :param case_name:
    :param args:
    :return:
    """
    # 读取excel配置文件
    excel_conf = get_yml_data(os.path.join(config_path, 'excelDataConfig.yml'))
    print(excel_conf)
    # TODO task 需要把路径做成自动识别的工程路径
    file_path = os.path.join(data_path,excel_conf["file_name"])
    args = excel_conf['cols']
    res_list = []
    col_indexs = [] # 存放列编号
    #1. 打开excel文件，--在磁盘，代码需要操作，需要加载到内存里
    work_book = xlrd.open_workbook(file_path, formatting_info=True) # # formatting_info=Trure 样式 xls格式的excel  其他格式xlsx
    # 获取所有表的名
    # 2.操作对应的表
    work_sheet = work_book.sheet_by_name(sheet_name)
    """-------------------重点---------------------
    示例：args = ’请求参数‘，’预期响应数据‘
    args 得到是一个元组
    """
    # 3.获取对应的数据
    #print(work_sheet.row_values(0))# 获取对应的数据--1行
    #print(work_sheet.col_values(0))# 获取对应的数据--1列
    #print(work_sheet.cell(0,0).value) # 获取对应的数据---单元格--cell(行编号，列编号)
    for one in args: # ’请求参数‘，预期响应数据---列号
        col_indexs.append(work_sheet.row_values(0).index(one)) # 表头是一个列表，使用index
        #---------用例筛选-----------
        # 示例 run_case= ['all’,‘003’,‘005-007,‘009’]
        run_case_list =[] # 需要运行的测试用例编号
        #1.全选
        if run_case is None or 'all' in run_case:
            run_case_list = work_sheet.col_values(0)
        else:  # 需要筛选
            for one in run_case :
                if '-' in one :  # 是连续的
                    start, end = one.split('-') # 字符串:star 005 end007
                    for num in range(int(start), int(end)+1):
                        run_case_list.append(f'{case_name}{num:0>3}')#组装好测试用例
                else:
                    run_case_list.append(f'{case_name}{one:0>3}')

    print('1.用户执行得用例编号---->', run_case_list)

    print('用户需要获取的数据列编号---->',col_indexs)
    row_index = 0 # 行编号初始值
    for one in work_sheet.col_values(0):
        if case_name in one and one in run_case_list:
            col_data = []
            for index in col_indexs :  # 需要获取列的编号-[9, 11]
                tmp = is_json(work_sheet.cell(row_index, index).value)  # 列编号有几个，就循环几次
                col_data.append(tmp)  # 这一行的，这个几列数据的结果
            res_list.append(col_data)
        row_index += 1  # 行好加+1
    #print(res_list)

    return res_list
# 封装一个判断是否是json函数
def is_json(str): # 判断返回的数据格式是否是json格式，字典格式
    """
    :param str: 需要判断的字符串数据
    :return: 结果
    """
    try:
       return  json.loads(str) # 是json字符串，---直接返回转换后得字典数据
    except:
        return str  # 不是json--原字符串返回

if __name__ == '__main__':
    res = get_excel_data('登录模块', 'Login',
                    )# 文件地址，表名，用例名
    print(res)
"""
测试反馈：
-1.不能选择某一个，或者某些用例执行
-2.函数需要传递的参数太多
解决方案：
 -1.使用*args参数
 -2 数据格式
"""

