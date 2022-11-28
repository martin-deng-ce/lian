# -*- coding: utf-8 -*-
# @File    : handle_mock.py
# @Time    : 11月 10, 2022
# @Author  : Martin.deng
# @E-mail  : 1637754392@qq.com
# @Software: PyCharm
import requests
import time
import threading

HOST = 'http://127.0.0.1:9090'   # 协议要素
# def test():
#     url = f'{HOST}/sq'
#     payload = {"key1": "abc", "key2": "123"}
#     resp = requests.get(url, params=payload)
#     print(resp.text)
# ----申诉接口------
def commit_order(data):
    url = f'{HOST}/api/order/create/'
    payload = data
    resp = requests.post(url, json=payload)
    return resp.json()
# ----查询接口------
""" 接口的特性：不是你想查询就里面可以查询的，也不能一直循环查询
注意事项：
 使用具体id查询
 查询需要频率 单位是s秒 interval
 超时机制：timeout s秒
"""
def get_order_list(id,interval=5,timeout=30):
    """
    :param id: 需要查询的id
    :param interval:  频率 但是s
    :param timeout: 超时机制 超时30s
    :return: 返回值
    """
    url = f'{HOST}/api/order/get_result1/'
    payload = {"order_id": id}
    start_time = time.time()
    end_time = start_time+30
    cnt = 1 # 查询次数初始值
    while time.time() < end_time: # 没有超时就可以循环
        resp = requests.get(url,params = payload)
        if resp.text:
            print(f'第{cnt}查询结果是---->',resp.text)
            return resp.text
        else:
            print(f'----第{cnt}次查询没有返回结果‘，请稍等5秒后再查询---')
        time.sleep(interval) #频率
        cnt += 1
    print('---查询超时，请联系平台管理员人工处理')
    resp = requests.get(url, params=payload)
    return resp.text

if __name__ == '__main__':
    start_time = time.time() # 主线程执行开始时间
    order_data = {
        "user_id": "sq123456",
		"goods_id": "20200815",
		"num":1,
		"amount":200.6
    }
    res = commit_order(order_data)
    id = res["order_id"]
    print(id)
    print('申诉请求响应--->', res)
    # 查询结果
    res2 = get_order_list(id)
    # ---创建子线程----
     # target =需要把哪一个函数做成子线程的函数名
    #args  子线程函数的需要传递的参数---要求是元组
    t1 = threading.Thread(target = get_order_list,args = (id,))

    t1.setDaemon(True)
    t1.start()
    for one in range(40):
        print(f'{one}---主线程自动化测试')
        time.sleep(1)
    end_time = time.time() #主线程执行结束时间
    print('查询结果是--->',res2)



"""
编程阶段:
1.逻辑功能先实现
2.优化：代码结果+执行效率
沟通:
领导:这个接口是实现了，但是有没有优化的空间，执行的效率比较低！
分析:深入分析，time.sleep(5)*6=30s 分析原因
技术分析:
 -cpu分析
   cpu密集 算法当面，阶乘运算
   cpu io阻塞 sleep request请求
方案：解决效率问题

 1 多线程技术：在一个进程里面去创建多个线程执行多个任务！进程里的线程共享进程的资源
 强调是充分利用一个cpu核的资源
 2 多进程：实现多个客户端去执行，并行
 3 协程 更小的线程
 3 多进程+协程
扩展方案:
 -pytest自带的分布方式模式
 - pytest -xdist 多进程方案
  -- pytest -paraller 多线程方案
  具体实现: 
  多线程实现
   1 主线程
    是不是整个代码运行自动化测试
   2 子线程
    查询结果的接口
"""
