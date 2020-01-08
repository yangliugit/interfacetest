import os
import logging
import time
from public import ReadConfig
# import threading


class MyLog(object):
    def __init__(self):

        self.resultPath = os.path.join(ReadConfig.proDir, "results")

        if not os.path.exists(self.resultPath):
            os.mkdir(self.resultPath)

        self.logPath = os.path.join(self.resultPath, time.strftime('%Y%m%d%H', time.localtime(time.time())))

        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)

        self.logger = logging.getLogger()

        # avodi handlers duplicate
        if not self.logger.handlers:

            self.logger.setLevel(logging.INFO)

            fh = logging.FileHandler(os.path.join(self.logPath, "output.log"))

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(funcName)s'
                                          ' - %(levelname)s - %(message)s')

            fh.setFormatter(formatter)

            self.logger.addHandler(fh)

    # @classmethod
    # def get_log(cls):
    #     return cls().logger

    def get_logger(self):
        return self.logger

    def get_result_path(self):
        html_path = self.resultPath + '\\result.html'
        f = open(html_path, 'w')
        f.close()
        return html_path

    # def info(self, msg):
    #     self.logger.info(msg)
    #
    # def warning(self, msg):
    #     self.logger.warning(msg)
    #
    # def error(self, msg):
    #     self.logger.error(msg)
    #
    # def debug(self, msg):
    #     self.logger.debug(msg)

if __name__ == '__main__':
    lp = MyLog()
    print lp.get_result_path()