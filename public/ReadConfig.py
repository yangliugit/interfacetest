import os
import ConfigParser


proDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
conf_path = proDir + '\config\\'


class ReadConfig(object):
    def __init__(self, config_name):
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(conf_path + config_name)

    def get_bs(self, name):
        value = self.conf.get("BS", name)
        return value

    def get_mysql(self, name):
        value = self.conf.get("MYSQL", name)
        return value

    def get_vehicle(self, name):
        value = self.conf.get("VEHICLE", name)
        return value

    def get_interface_url(self, name):
        value = self.conf.get("INTERFACE_URL", name)
        return value

if __name__ == '__main__':
    c = ReadConfig('config.ini')
    print conf_path
    print c.get_interface_url('URL')
