# -*- coding: utf-8 -*-
from public import MyDb
from public.Log import MyLog
import unittest
import datetime
from public import GetData
from public.Http import Http
import json


class TestInterface(unittest.TestCase):
    def setUp(self):
        self.log = MyLog().get_logger()
        self.log.info("Begin test!!!")
        self.mysql = MyDb.Mysql()

    def test_insert_one(self):
        sql = "insert into t_employee_info(name, sex, age, position, adress, description, update_time) values(%s, %s, %s, %s, %s, %s, %s)"
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print dt
        params = ('李俊', '男', 26, '测试工程师', '雨花台区安德门龙福山庄', '门户活动测试工作', dt)
        self.mysql.insert_one(sql, params)
        self.mysql.dispose()
        try:
            self.assertEqual(1, 2, msg="insert one Failed")
        except Exception as err:
            self.log.error(err)

    def test_get_one(self):
        sql = "select * from test.t_employee_info"
        a = self.mysql.get_one(sql)
        self.mysql.dispose()
        for k, value in a.items():
            print k, value

    def test_get_many(self):
        sql = "select * from test.t_employee_info"
        a = self.mysql.get_many(sql, 2)
        self.mysql.dispose()
        for i in a:
            for k, value in i.items():
                print k, value

    def test_update(self):
        sql = 'update test.t_employee_info set name = \'李四\' where id = 1'
        self.mysql.update(sql)
        self.mysql.dispose()

    def test_insert_many(self):
        sql = "insert into t_employee_info(name, sex, age, position, adress, description, update_time) values(%s, %s, %s, %s, %s, %s, %s)"
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print dt
        params = ('刘飞', '男', 26, '测试工程师', '雨花台区安德门龙福山庄', '门户活动测试工作', dt)
        self.mysql.insert_many(sql, params)
        self.mysql.dispose()

    def test_getdata_xls(self):
        for s in GetData.get_xls("test_case.xlsx", "mycase"):
            print s

    # def test_get_cookies(self):
    #     ht = Http()
    #     headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
    #                "Accept-Encoding": "gzip, deflate",
    #                "Accept-Language": "zh-CN,zh;q=0.8",
    #                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    #                              "Chrome/58.0.3029.81 Safari/537.36",
    #                'X-Requested-With': 'XMLHttpRequest',
    #                "Content-Type": "application/json;charset=UTF-8"
    #                }
    #     ht.set_headers(headers)
    #     ht.set_url("/icompaign/getVerifyCode")
    #     gr = ht.get()
    #     jsessionid = GetData.get_cookies(ht.url, "get", data=None)
    #     print gr.status_code
    #     print jsessionid
    #     cookies = {"JSESSIONID": jsessionid}
    #     ht.set_cookies(cookies)
    #
    #     ht.set_url("/icompaign/loginByPhone.view")
    #     data = {"phone": "18626330613", "code": "111111", "vCode": "4jjm"}
    #     data = json.dumps(data)
    #     ht.set_data(data)
    #     r = ht.post()
    #     print r.status_code
    #     print r.text

    def tearDown(self):
        self.log.info("End test!!!")

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestInterface("1"))
    unittest.TextTestRunner(verbosity=2).run(suite)
