
import pytest
from page.base_driver import BaseDriver
'''
uuid和appium_port   主要是给driver传这两个参数
'''

def pytest_addoption(parser):#给pytest命令行设置一个自定义的参数
    parser.addoption('--cmdport',action='store',default=4723,help='这是指定appium的端口号')
    parser.addoption('--cmduuid', action='store', default='127.0.0.1:62001', help='这是指定appium连接的uuid')

@pytest.fixture(scope='class')
def driver(request):
    appium_port = request.config.getoption("--cmdport")
    uuid = request.config.getoption("--cmduuid")
    driver = BaseDriver.start_driver\
            (appPackage='com.douban.frodo',
             appActivity='com.douban.frodo.activity.SplashActivity',
             uuid=uuid,appium_port=appium_port)
    return driver