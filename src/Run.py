# -*- coding: utf-8 -*-
import os
import unittest
from public.Log import MyLog
from public import ReadConfig
import HTMLTestRunner


class RunTest(object):
    def __init__(self):
        self.log = MyLog().get_logger()
        self.result_path = MyLog().get_result_path()
        self.case_list_file = os.path.join(ReadConfig.conf_path, "caselist.txt")
        self.case_file = os.path.join(ReadConfig.proDir, "test_case")
        self.case_list = []

    def get_case_list(self):
        with open(self.case_list_file) as f:
            for case in f.readlines():
                dcase = case.replace('\n', '')
                if not dcase.startswith('#') and dcase != '':
                    self.case_list.append(dcase)

        return self.case_list

    def get_case_suite(self):
        self.get_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.case_list:
            discover = unittest.defaultTestLoader.discover(self.case_file, pattern=case + ".py", top_level_dir=None)
            suite_module.append(discover)

        # length jugment have problem
        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        try:
            suite = self.get_case_suite()
            print ("suite:", suite)
            if suite is not None:
                self.log.info("*************TEST START*************")
                f = open(self.result_path, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='Test Report', description='Test Description', verbosity=2)
                runner.run(suite)
                f.close()
            else:
                self.log.info("Have no test case!")
        except Exception as e:
            self.log.error(str(e))
        finally:
            self.log.info("*************TEST END***************")


if __name__ == '__main__':
    runa = RunTest()
    runa.run()
