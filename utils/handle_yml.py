# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: handle_yml.py
# @Author: Martin.deng
# @E-mail: 1637754392@qq.com
# @Time: 11月 05, 2022
import yaml
import os.path

class Loader(yaml.Loader):  # 继承
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)
    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, 'r') as f:
            return yaml.load(f, Loader)

Loader.add_constructor('!include', Loader.include)


def get_yml_data(file_path: str):
    with open(file_path, encoding='utf-8') as fo:  # file object
        #  把读取的字符串转为Python好操作的字典与列表之类的类型
        return yaml.safe_load(fo.read())  # 加载模式

def get_case_data(file_path:str):
    res_list = []
    res = get_yml_data(file_path)
    print(res)
    for one in res:
        res_list.append((one['detail'], one['data'], one['resp']))
    return res_list


if __name__ == '__main__':

    res = get_case_data('../data/loginCase.yml')  # 相对路径
    print(res)
