# interfaceTest
---
## Moudles
1. config  
  框架配置文件。存储接口信息、MySQL配置等信息
  
2. public  
  公共模块。提供各类方法封装，目前有：
    - `GetData.get_xls(xls_name, sheet_name)` 读取excel数据并返回
    - `GetData.get_json(response, key)` 根据响应获取键为key的值
    - `GetData.gzdecode(data)` 解压http请求前数据
    - `GetData.get_cookies(url, method, data=None)` 获取cookies
    - `GetData.dict_cmp(src_data, dst_data)` 比对两个json串，返回Boolean
    - Http() 待测项目HTTP请求类，包含一系列http请求参数设置和方法
    - MyLog() 项目日志类，提供日志存储和测试结果存储功能
    - Mysql() 数据库类封装，提供数据库增删改查功能
    - ReadConfig() 配置读取类
    
3. src  
  用例执行模块。其中根据unittest包加载测试套，HTMLTestRunner包执行测试套
  
4. test_case  
  测试用例编写模块，继承unittest编写测试类。 其中，可以根据paramunittest包序列化测试参数。
  
5. test_case_date  
  待序列化的测试用例，例如接口测试用例excel
  
6. results  
  测试结果保存路径。包含执行日志和执行结果

