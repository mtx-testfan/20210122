import configparser
import os

from item_path import DIR_NAME


class IniHelper(object):
    def __init__(self):
        '''
        具体的配置文件在哪一个文件夹里面
        '''
        self.source_folder = 'pageElement'



    def get_source_file(self,filename):
        '''
         获取读取完init文件的config
        :param filename: 文件名字
        :return: config
        '''
        try:
            config = configparser.ConfigParser()
            file_path = DIR_NAME+'/'+self.source_folder+'/'+ filename
            config.read(file_path, encoding='utf-8')
            return config
        except Exception as e:
            print('read config file error：'+str(e))

    def get_value(self,filename,section,key):
        '''

        :return:
        '''
        try:
            config = self.get_source_file(filename)
            value = config.get(section,key)
            return value
        except Exception as e:
            print('get value fail：' + str(e))


if __name__ == '__main__':
    print(IniHelper().get_value('doubanPage.ini', 'Button', '我的'))

