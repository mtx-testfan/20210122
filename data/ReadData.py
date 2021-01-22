#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: ReadData.py
# @Author: Bull
# ---
# 用来读取数据文件
import yaml

class elements_data():
    @staticmethod#静态方法效率更高
    def read(filename:str):
        #相对路径会根据运行脚本的路径,发生变化.所以这里用绝对路径来表示
        path = r'D:\company\autopre\20201012\appcode\appframe\data\\'
        with open(path+filename) as f:
            data = yaml.full_load(f)
        return data

if __name__ == '__main__':
    print(elements_data.read('douban.yml'))