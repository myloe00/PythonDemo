"""
@File:    config.py
@Author:  myloe
@Date:    2020/11/12 21:14
@Desc:
"""
import threading
import configparser


class ConfFile:
    """
    提供通过获取对象属性的方式去获取配置文件中的配置项
    """

    _instance_lock = threading.Lock()

    def __init__(self, file='./config.ini', default_section='default'):
        self.default_section = default_section
        conf = configparser.ConfigParser()
        conf.read(file, encoding='utf-8')

        for key in conf.sections():
            inner_attr = {}
            for param in conf[key]:
                inner_attr[param] = conf[key][param]
            attr_list = key.split('.')
            tmp_attr = None
            self.build_attr(attr_list, len(attr_list), tmp_attr ,inner_attr,key)
            # if len(attr_list) == 3:
            #     tmp_attr = type('tmp_attr', (object,), inner_attr)
            #     tmp_attr = type(attr_list[2], (object,), {attr_list[2]:tmp_attr})
            #     tmp_attr = type(attr_list[1], (object,), {attr_list[1]:tmp_attr})
            #     setattr(self,attr_list[0],tmp_attr)
            # elif len(attr_list) == 2:
            #     tmp_attr = type('tmp_attr', (object,), inner_attr)
            #     tmp_attr = type(attr_list[1], (object,), {attr_list[1]:tmp_attr})
            #     setattr(self,attr_list[0],tmp_attr)
            # else:
            #     tmp_attr = type('tmp_attr', (object,), inner_attr)
            #     setattr(self, key, tmp_attr)

    def build_attr(self, attr_list, length, tmp_attr,inner_attr,key):
        if length == 1:
            if not tmp_attr:
                tmp_attr = type(attr_list[0], (object,), inner_attr)
            setattr(self, attr_list[0], tmp_attr)
            return tmp_attr
        else:
            if tmp_attr is None:
                tmp_attr = type(attr_list[length-1], (object,), inner_attr)
            tmp_attr = type(attr_list[length-2], (object,), {attr_list[length-1]:tmp_attr})
            # setattr(self, attr_list[length-2], tmp_attr)
            return self.build_attr(attr_list, length - 1, tmp_attr,inner_attr,key)
            # setattr(self,attr_list[0],tmp_attr)



    def __getattribute__(self, attr):
        # 如果没有提供section时，前往default_section中搜索属性
        try:
            result_attr = super().__getattribute__(attr)
        except AttributeError:
            return super().__getattribute__(self.default_section)().__getattribute__(attr)
        return result_attr

    def __new__(cls, *args, **kwargs):
        if not hasattr(ConfFile, "_instance"):
            with ConfFile._instance_lock:
                if not hasattr(ConfFile, "_instance"):
                    ConfFile._instance = object.__new__(cls)
        return ConfFile._instance

if __name__ == '__main__':
    config = configparser.ConfigParser()
    print("- Empty config %s" % config.sections())

    print("- Load config file")
    config.read("./config.ini")
    config
    x = ConfFile()
    print(x.param1)
