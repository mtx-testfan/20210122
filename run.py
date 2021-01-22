import multiprocessing
import os
import subprocess

import pytest


def start_appium_server():
    print(os.system('appium'))
    env_dist = os.environ
    print('env_dist的值', env_dist)

def main():

    p = multiprocessing.Process(target=start_appium_server)
    p.start()
    print(f'p线程执行了cmd启动appium-server的命令:{type(p)}')

    pytest.main(['-sv', './case/test_douban.py', '--alluredir=./reports/mtx', '--clean-alluredir','--cmdport=4723','--cmduuid=127.0.0.1:62001'])
    # subprocess: 把在终端操作的命令行转移到python文件中操作,shell=True 接收这个命令，并以shell脚本的形式运行
    subprocess.call('allure generate ./reports/mtx -o ./reports/html/ --clean', shell=True)
    p.join()
    p.terminate()


if __name__ == '__main__':
    main()