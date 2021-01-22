import os
'''
目的：通过item_path.py获取整个工程的绝对路径
DIR_NAME
D:\company\auto\20201012\lesson13\lesson13_1
'''
ABS_PATH = os.path.abspath(__file__)

DIR_NAME = os.path.dirname(ABS_PATH)
