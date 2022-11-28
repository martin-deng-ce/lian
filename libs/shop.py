# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: shop.py
# @Author: Martin.deng
# @E-mail: 1637754392@qq.com
# @Time: 11月 02, 2022
from common.baseApi import BaseAPI
from libs.login import Login


class Shop(BaseAPI):
    pass

    # 更新接口，不光使用父类的update发送请求根据excel数据读取到值
    # 额外功能，需要动态关联店铺id，还有图片信息
    # 总结：baseAPI父类update方法不满足当前的店铺更新接口需求，需要重写
    # 问题：每一个用例都需要更新实时店铺id???不需要，用例分类，正向用例/反向用例
    # 问题2：代码如何识别哪一个用例是否需要更新对应的数据(店铺id，图片信息)在用例架上标识
    # 问题2解决方案：${id} 用例标志区分
    def update(self, data=None, shop_id=None, image_info=None):
        """

        :param data:
        :param shop_id:
        :param image_info:
        :return:
        """
        """
        :param data: 读取到用例的数据
        :param shop_id: 实时店铺的id
        :param image_info: 实时的图片信息
        :return :
        """
        if data['id'] == '${id}':  # 这个用例的店铺id需要更新实时的id
            data['id'] = shop_id
        # 图示是否需要更新，自己写代码if
        data['image_path'] = image_info
        data['image'] = f'/file/getImgStream?fileName={image_info}'
        # 发送请求---自雷如何去调用父类的方法
        # super(子类的类名，self实例).update()
        return super(Shop, self).update(data=data)


if __name__ == '__main__':
    # 登录操作
    login_data = {'username': 'th0198',
                  'password': 'xintian'}
    token = Login().login(login_data, get_token=True)
    # 1.查询的测试数据
    query_data = {"page": 1, "limit": 20}
    # 2.创建店铺实例
    shop = Shop(token)
    res = shop.query(query_data)
    shop_id = res['data']['records'][0]['id']
    # print(res)
    # 3.文件上传接口
    res = shop.file_upload('../data/123.png')
    # print(res)
    image_info = res['data']['realFileName']
    # 4.店铺的更新接口
    update_data = {
        "name": "星巴克新建店12",
        "address": "上海市静安区秣陵路303号",
        "id": "999999",
        "Phone": "13176876632",
        "rating": "6.0",
        "recent_order_num": 100,
        "category": "快餐便当/简餐",
        "description": "满30减5，满60减8",
        "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
        "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"
    }
    res = shop.update(update_data, shop_id, image_info)
    print(res)
