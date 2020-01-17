# -*- coding: utf-8 -*-
import os
import json
# from public.Http import Http
from xlrd import open_workbook
from public import ReadConfig
from public.Log import MyLog
import requests
import time
import StringIO
import gzip


CMP_STATUS = 0
conf = ReadConfig.ReadConfig("config.ini")
# ht = Http()
log = MyLog().get_logger()


def get_xls(xls_name, sheet_name):
    """
    获取excel表中执行的sheet数据，保存到列表中并返回
    :param xls_name:
    :param sheet_name:
    :return:
    """
    case_list = []
    xls_path = os.path.join(ReadConfig.proDir, "test_case_data", xls_name)
    xls = open_workbook(xls_path)
    sheet = xls.sheet_by_name(sheet_name)
    sheet_nrows = sheet.nrows
    for i in range(sheet_nrows):
        if sheet.row_values(i)[0] != u"caseName":  # 剔除首行
            case_list.append(sheet.row_values(i))
    return case_list


def get_json(response, key):
    """
    获取http响应，转化为json并根据key获取value
    :param response:
    :param key:
    :return:
    """
    return_json = response.json()
    json_value = return_json[key]
    return json_value


def gzdecode(data):
    """
    解压http请求前的数据
    :param data:
    :return:
    """
    compressedstream = StringIO.StringIO(data)
    gziper = gzip.GzipFile(fileobj=compressedstream)
    data2 = gziper.read()
    return data2


def get_cookies(url, method, data=None):
    session = requests.session()
    if method == 'get':
        session.get(url, data=data)
    elif method == 'post':
        session.post(url, data=data)
    cookies = requests.utils.dict_from_cookiejar(session.cookies)
    return cookies['JSESSIONID']


# def dict_cmp(src_data, dst_data):
#     """
#     传入json前需要json.loads()方法转换成dict
#     1.判断传入的参数，数据类型相同
#     2.判断类型为dict的情况，先进行长度对比，然后进行递归对比
#     3.list的情况，先进行长度对比，再进行递归对比
#     4.判断非dict/list的情况
#     :param src_data: dict/list
#     :param dst_data: dict/list
#     :return:
#     """
#     assert type(src_data) == type(dst_data), "type: %s != %s" % (type(src_data), type(dst_data))
#     if isinstance(src_data, dict):
#         assert len(src_data) == len(dst_data), "dict len %s != %s" % (len(src_data), len(dst_data))
#         for key in src_data:
#             assert key in dst_data, "key is not equal"
#             dict_cmp(src_data[key], dst_data[key])
#
#     elif isinstance(src_data, list):
#         assert len(src_data) == len(dst_data), "list len %s != %s" % (len(src_data), len(dst_data))
#         for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
#             dict_cmp(src_list, dst_list)
#
#     else:
#         assert src_data == dst_data, "value %s != %s" % (src_data, dst_data)


def dict_cmp(src_data, dst_data):
    """
    传入json前需要json.loads()方法转换成dict
    1.判断传入的参数，数据类型相同
    2.判断类型为dict的情况，先进行长度对比，然后进行递归对比
    3.list的情况，先进行长度对比，再进行递归对比
    4.判断非dict/list的情况
    :param src_data: dict/list
    :param dst_data: dict/list
    :return:
    """
    global CMP_STATUS
    if type(src_data) != type(dst_data):
        print "typeError: %s != %s" % (type(src_data), type(dst_data))
        CMP_STATUS += 1
    if isinstance(src_data, dict):
        if len(src_data) != len(dst_data):
            CMP_STATUS += 1
        for key in src_data:
            if key not in dst_data:
                CMP_STATUS += 1
            try:
                dict_cmp(src_data[key], dst_data[key])
            except KeyError:
                CMP_STATUS += 1

    elif isinstance(src_data, list):
        if len(src_data) != len(dst_data):
            CMP_STATUS += 1
        for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
            dict_cmp(src_list, dst_list)

    else:
        if src_data != dst_data:
            CMP_STATUS += 1
        else:
            pass
    if CMP_STATUS > 0:
        return False
    else:
        return True

if __name__ == '__main__':
    print get_xls("test_case.xlsx","mycase")
    # a = {'a': [1, 2, 3, 4], "c": {1: 'a', 2: 'b'}}
    # b = {'a': [1, 2, 3, 6], "c": {1: 'a', 2: 'b'}}
    # try:
    #     assert dict_cmp(a, b) is True, "dict is not equal"
    # except Exception as e:
    #     log.info(e)
