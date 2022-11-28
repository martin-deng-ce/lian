mock技术：
 -概念：也叫测试桩/挡板
 -使用场景：
    1.项目部分新业务没有开发完成
    2.涉及很多第三方接口，响应效率低
 -实现手段：
    概念：模拟的是后端
    前提：需要对应的api接口说明
 方式：
    1.如果你在团队编程比较厉害，有人会写后端，python flask/django，写了一个简易的后端给测试调试！
    2.如果使用现成工具 postman有这个功能，很多平台也有这个功能
    3.是否有一种方式，不需要写代码，也不需要去搭建代码，也不需要搭建什么环境，就可以实现！
Moco框架
 
mock服务搭建：
mock服务运行：
    目录下cmd  java -jar moco-runner-1.1.0-standalone.jar http -p 9090 -c test.json
    本地地址：http://localhost:9999/demo2

异步接口与同步接口