#! usr/bin/env python3
# coding=utf-8
import pytest


def setup_module():
    print("这是setup_moudle方法")  # 模块


def teardown_module():
    print("这是teardown_module方法")


def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")


def test_login():
    print("这是一个外部方法")


class TestDemo():
    def setup_class(self):
        print("setup_class")

    def setup_method(self):
        print("setup_method")

    def teardown_method(self):
        print("teardown_method")

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def teardown_class(self):
        print("teardown_class")

    def test_one(self):
        print("开始执行第一条测试用例")
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print("开始执行第二条测试用例")
        b = 'test'
        assert 'test' == b

    def test_three(self):
        print("开始执行第二条测试用例")

        assert 'maxu' in 'maxuzui'


if __name__ == '__main__':
    pytest.main("-v -x TestDemo")
