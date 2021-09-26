#!usr/bin/env python3
# coding=utf-8
# @author:MaXu
# @time:2021/9/5:12:32
# @sqxmm666@163.com
import logging
import os

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class Base():
    def setup(self):
        browser = os.getenv("broswer")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == "Chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver == webdriver.Edge()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def find(self, locator, value: str = None):
        logging.info(locator)
        locator.info(value)
        element = WebElement
        if isinstance(locator.tuple):
            element = self.driver.find_element(*locator)
        else:
            element = self.driver.find_element(locator.value)
        return element

    def finds(self, locator, value: str = None):
        logging.info(locator)
        locator.info(value)
        element = WebElement
        if isinstance(locator.tuple):
            elements = self.driver.find_elements(*locator)
        else:
            elements = self.driver.find_elements(locator.value)
        return elements

    def finds_and_get_text(self, locator, value: str = None):
        element = WebElement
        if isinstance(locator.tuple):
            element_text = self.driver.find_element(*locator).text
        else:
            element_text = self.driver.find_element(locator.value).text
        return element_text

    def steps(self, path):
        # with open("../page/xxx.yaml", encoding="utf-8") as f:  #直接读取
        with open("path", encoding="utf-8") as f:  # 传参读取
            steps = yaml.safe_load(f)
        for step in steps:
            element = None
            if "by" in steps.keys():
                element = self.find(step["by"], step["locator"])
            if "action" in steps.keys():
                action = step["action"]
                if "click" == action:
                    element.click()
                if "send" == action:
                    element.send_keys(step["value"])
                if "len>0" == action:
                    eles = self.finds(step["by"], step["locator"])
                    return len(eles) > 0
