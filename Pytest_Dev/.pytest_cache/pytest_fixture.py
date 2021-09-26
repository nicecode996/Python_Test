#! usr/bin/env python3
# coding=utf-8
import pytest


@pytest.fixture()
def login():
    print("这是一个登陆方法")


def test_case1(login):
    print(1, '要登陆')
    pass


def test_case2():
    print(2, '不要登录')
    pass


def test_case3(login):
    print(3, '要登陆')
    pass


if __name__ == '__main__':
    # pytest.main()
    pytest(['-v', '-s'], '--html = report.html - -self - contained - html')
