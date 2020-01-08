#coding=utf_8
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner


class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url="http://www.baidu.com"

    def test_baidu_search(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    print(1111111111)
    testunit=unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))

    #定义报告存放路径
    fp=open(r'd:\result.html','wb')

    #定义测试报告
    runner=HTMLTestRunner(stream=fp,
                          title=u'百度搜索测试报告',
                          description=u'用例执行情况：')

    runner.run(testunit)#运行测试用例
    fp.close()#关闭报告文件