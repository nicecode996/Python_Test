#!usr/bin/env python3
# coding=utf-8
# @author:MaXu
# @time:2021/9/5:19:21
# @sqxmm666@163.com
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Broswer():
    def setup_method(self):
        options = Options()
        Options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.chrome(Options=options)  # 如想取消复用就把Options=options删除即可
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        print(self.driver.get_cookies())
        sleep(5)
        # 获取cookies
        self.drvier.get("https://www.baidu.com")

        # 保存cookies
        db = shelve.open("cookies")
        cookies = db['cookie']
        db['cookies'] = self.driver.get_cookies()
        for cookie in cookies:
            if "expiry" in cookies.keys():
                cookie.pop("expiry")
            self.driver.add_cookies(cookies)

        sleep(5)
        db.close()
