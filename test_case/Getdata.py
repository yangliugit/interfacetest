import paramunittest
from public import GetData
import unittest
from public.Log import MyLog
import time

inscase = GetData.get_xls("test_case.xlsx", "mycase")
log = MyLog().get_logger()


@paramunittest.parametrized(*inscase)
class Getdata(unittest.TestCase):
    def setParameters(self, caseName, method, vehicleIds, cmdCode, cmdVal, sendTitle, paramCode, paramName, Id):
        self.caseName = caseName
        self.method = method
        self.vehicleIds = vehicleIds
        self.cmdCode = cmdCode
        self.cmdVal = cmdVal
        self.sendTitle = sendTitle
        self.paramCode = paramCode
        self.paramName = paramName
        self.Id = Id

    def setUp(self):
        print "begin test-------------"

    def test_getdata(self):
        time.sleep(1)
        print "caseName:%s \n method:%s \n vehicleIds:%s \n cmdCode:%s \n cmdVal:%s \n sendTitle:%s \n paramCode:%s \n paramName:%s \n Id:%s \n " % (self.caseName, self.method, self.vehicleIds, self.cmdCode, self.cmdVal, self.sendTitle,self.paramCode, self.paramName, self.Id)
        self.assertEqual(1, 2, msg="woshiguyide")
        # try:
        #     self.assertEqual(1, 2, msg="woshiguyide")
        # except Exception as e:
        #     log.error(str(e))

    def tearDown(self):
        print "end test-------------"
