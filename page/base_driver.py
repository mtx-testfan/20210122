# appium_port  多设备 不同设备对应不同服务
from appium import webdriver
class BaseDriver():
    @staticmethod
    def start_driver(appPackage,appActivity,uuid='127.0.0.1:62001',appium_port='4723'):
        caps = {}
        caps["platformName"] = 'Android'  # 指定测试平台
        caps['deviceName'] = 'Phone'  # 安卓中可以随意填一个,但是必传
        caps['appPackage'] = appPackage  # 包名
        caps['appActivity'] = appActivity  # 启动界面名
        caps['noSign'] = True  # 跳过重签名
        caps['unicodeKeyboard'] = True  # appium会为手机安装一个用来做自动化的输入法,①可以输入中文和特殊符号②不会弹出键盘区域,挡住屏幕
        caps['resetKeyboard'] = True  # 自动把输入法还原
        caps['uuid'] = uuid


        driver = webdriver.Remote(f'http://localhost:{appium_port}/wd/hub', caps)
        driver.implicitly_wait(10)
        return driver


if __name__ == '__main__':
    dev = BaseDriver().start_driver(appPackage='com.douban.frodo',appActivity='com.douban.frodo.activity.SplashActivity')
    print(dev)
# caps['appPackage'] = 'com.douban.frodo'  # 包名
# caps['appActivity'] = 'com.douban.frodo.activity.SplashActivity'  # 启动界面名