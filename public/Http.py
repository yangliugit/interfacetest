# -*- coding: utf-8 -*-
import requests
from public import ReadConfig
from public.Log import MyLog
import json

conf = ReadConfig.ReadConfig("config.ini")


class Http(object):

    def __init__(self):
        self.scheme = conf.get_bs("SCHEME")
        self.ip = conf.get_bs("IP")
        self.port = conf.get_bs("PORT")
        self.timeout = conf.get_bs("TIMEOUT")
        self.log = MyLog().get_logger()
        self.headers = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0
        self.s = requests.session()

    def set_url(self, url):
        """
        接口路径及名称
        :param url:
        :return:
        """
        self.url = "%s://%s:%s%s" % (self.scheme, self.ip, self.port, url)

    def set_headers(self, header):
        """

        :param header:
        :return:
        """
        self.headers = header

    def set_data(self, data):
        """

        :param data: JSON/params
        :return:
        """
        self.data = data

    def get(self):
        """
        GET请求
        :return:
        """
        try:
            response = self.s.get(self.url, headers=self.headers, timeout=float(self.timeout))
            return response
        except Exception as e:
            self.log.error(e)
            return None

    def post(self):
        """
        POST请求
        :return:
        """
        try:
            response = self.s.post(self.url, data=self.data, headers=self.headers, timeout=float(self.timeout))
            return response
        except Exception as e:
            self.log.error(e)
            return None

    def set_cookies(self, c):
        """

        :param c: 获取的jsessionID
        :return:
        """
        requests.utils.add_dict_to_cookiejar(self.s.cookies, c)

if __name__ == '__main__':
    ht = Http()
    headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
               "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
               'X-Requested-With': 'XMLHttpRequest',
               "Content-Type": "application/json;charset=UTF-8"
               }
    ht.set_headers(headers)
    ht.set_url("/icompaign/getVerifyCode")
    gr = ht.get()
    print gr.status_code
    cookies = {"JSESSIONID": gr.cookies['JSESSIONID']}
    ht.set_cookies(cookies)

    ht.set_url("/icompaign/loginByPhone.view")
    data = {"phone": "18626330613", "code": "111111", "vCode": "4jjm"}
    data = json.dumps(data)
    ht.set_data(data)
    r = ht.post()
    print r.status_code
    print r.text
