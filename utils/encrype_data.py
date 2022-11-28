# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: encrype_data.py
# @Author: Martin.deng
# @E-mail: 1637754392@qq.com
# @Time: 10月 26, 2022
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1
"""
加密算法分类：
        -md5系列加密
        -aes加密 对称加密  加密/解密是一个秘钥
        -rsa加密 非对称加密  加密、解密使用一对公钥
        -sm4加密 国密
"""
def get_md5_data(data:str, salt=''):

    """
    :param data: 被加密的数据
    :param salt: 盐值，默认为空
    :return: 返回加密后得到16进制数据的密文
    """
    # 1.创建md5实例
    md5 = hashlib.md5()
    data = f'{data}{salt}'
    # 2.调用加密函数
    md5.update(data.encode('utf-8'))
    # 3.返回加密的密文
    return md5.hexdigest()


if __name__ == '__main__':
    res = get_md5_data('123456')
    print(res)
"""
RSA加密的代码逻辑：
1-安装对应的库 cmd--pip install pycryptodome
2-rsa加密处理流程：
   -1.先获取、加密的公钥文件
   -2.输入需要加密的明文数据--加密函数一定有一个形参data
   -3.把输入的字符串---byte str:'adc'----b'abc'
   -4.使用加密方法加密
   -5.使用base64编码（加密的密文进行编码）
   -6.解密---密文是bytes字节码---dencode（）---字符串
   """
class RsaEndecrypt:
    """Rsa的类"""
    def __init__(self, file_path='./'):
        self.file_path = file_path
    def encrypt(self, crypt_data):
            # 1.先获取/加密公钥文件--公钥数据
        with open(f'{self.file_path}pulic.pem', rb)as fo:
            # 2.获取公钥的内容
            key_content_bytes = fo.read()
            #3.把输入的明文密码--bytes
            crypt_data.encode('utf-8')
            #4.需要把公钥的内容给对应的函数---RSA公钥对象
            public_key= RSA.importKey(key_content_bytes)
            #5.使用公钥对象，生产一个加密对象
            cipher = PKCS1_cipher.new(public_key)
            #6.调用加密方法encrypt(必须是bytes参数)
            encrypt_text = cipher.encrypt(crypt_data)
            #7.使用base64编码
            base64.b64encode(encrrpt_text).decode('utf-8')


if __name__ == '__main__':
    res = RsaEndecrypt().encrypt('123456')
    print(res)