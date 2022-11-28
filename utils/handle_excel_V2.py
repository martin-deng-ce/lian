# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: handle_excel.py
# @Author: Martin.deng
# @E-mail: 1637754392@qq.com
# @Time: 10月 31, 2022
import xlrd
import json
"""
---------------V2.0-----------------
优化需求：
  -1. 如果选哟获取其他列数据--得修改源代码
  -2.数据格式，不符合数据得需求
解决方案：
  -1.使用*args参数 
       - 直接使用 列编号1，2，3，特点:可读性差，但是代码处理简单
       - 使用列表，请求参数，标题，特点，可读性号，代码不能直接取传递，需要转换
  -2 数据格式问题
        需要把请求参数json格式，---编程登录接口可加密的字典，json.loads()
        如果是json格式就转，不是json就不需要转换
"""
def get_excel_data(file_path,sheet_name,case_name,*args):
    """
    :param file_path: 文件路径
    :param sheet_name:
    :param case_name:
    :param args:
    :return:
    """
    res_list = []
    col_indexs = [] # 存放列编号
    #1. 打开excel文件，--在磁盘，代码需要操作，需要加载到内存里
    work_book = xlrd.open_workbook(file_path,formatting_info=True) # # formatting_info=Trure 样式 xls格式的excel  其他格式xlsx
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
    print('用户需要获取的数据列编号---->',col_indexs)
    row_index = 0 # 行编号初始值
    for one in work_sheet.col_values(0):
        if case_name in one:
            col_data = []
            for index in col_indexs: #需要获取列的编号-[9,11]
                tmp = is_json(work_sheet.cell(row_index,index).value) #列编号有几个，就循环几次
                col_data.append(tmp)  # 这一行的，这个几列数据的结果
            res_list.append(col_data)
        row_index += 1 # 行好加+1
    #print(res_list)
    #for one in res_list:
        #print(one)
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
    get_excel_data('../data/Delivery_System_V1.5.xls','登录模块','Login','标题','请求参数')# 文件地址，表名，用例名

"""
测试反馈：
-1.不能选择某一个，或者某些用例执行
-2.函数需要传递的参数太多
解决方案：
 -1.使用*args参数
 -2 数据格式
"""

