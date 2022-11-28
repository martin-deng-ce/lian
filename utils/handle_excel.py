# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: handle_excel.py
# @Author: Martin.deng
# @E-mail: 1637754392@qq.com
# @Time: 10月 31, 2022
import xlrd
import json
"""
需求：
代码方案：
-1.打开excel 
"""
def get_excel_data(file_path,sheet_name):
    """
    :param file_path: 文件路径
    :param sheet_name:
    :param case_name:
    :param args:
    :return:
    """
    res_list = []
    # col_indexs= []
    # col_data = []
    #1. 打开excel文件，--在磁盘，代码需要操作，需要加载到内存里
    # formatting_info=Trure 样式
    work_book = xlrd.open_workbook(file_path,formatting_info=True)  # xls格式的excel  其他格式xlsx
    print(work_book.sheet_names())
    # 获取所有表的名
    # print()
    # 2.操作对应的表
    work_sheet = work_book.sheet_by_name(sheet_name)
    # 3.获取对应的数据
    print(work_sheet.row_values(0))# 获取对应的数据--1行
    print(work_sheet.col_values(0))# 获取对应的数据--1列
    print(work_sheet.cell(0,0).value) # 获取对应的数据---单元格--cell(行编号，列编号)
    # -----
    """
    """
#     for one in args:
#        col_indexs.append(work_sheet.row_values(0).index(one))
      #for one in range(0,10):
    row_index = 0 # 行编号初始值
    for one in work_sheet.col_values(0):
        req_body = work_sheet.cell(row_index,9).value # 请求数据
        resp_exp = work_sheet.cell(row_index,11).value # 预期响应数据
#         if case_name in one:
#             for index in col_indexs:
#                 tmp = is_json().work_sheet.cell(row_index,index).value
#                 col_data.append(tmp)
        res_list.append((req_body,resp_exp))#
#             res_list.append(col_data)
        row_index += 1 # 行好加+1
    for one in res_list:
        print(one)
# # 封装一个判断是否是json函数
# def is_json(str): # 判断返回的数据格式是否是json格式，字典格式
#     try:
#        return  json.loads(str)
#     except:
#         return False
if __name__ == '__main__':
    get_excel_data('../data/Delivery_System_V1.5.xls','登录模块')# 文件地址，表名，用例名





    """---扩展----
    a = [10, 20, 30]
    name = ['xiaoming', 'xt', 'sq']
    res = zip(a, name)
    print(list(res))
    """
"""
测试反馈：
-1.如果需要其他列的数据---得修改源代码
-2.数据格式，不符合数据的需求！
解决方案：
 -1.使用*args参数
 -2 数据格式
"""

