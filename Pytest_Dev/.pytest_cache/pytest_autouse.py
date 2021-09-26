#! usr/bin/env python3
# coding=utf-8


import pytest


@pytest.fixture(autouse=True)
def open():
    print("打开浏览器")


def test_search1():
    print("test_search1")
    raise NameError
    pass

def test_search2():
    print("")
