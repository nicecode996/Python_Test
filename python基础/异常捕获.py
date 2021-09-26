#! usr/bin/env python3
# coding=utf-8
# try:
#     num1 = int(input("输入一个整数:"))
#     num2 = int(input("输入一个整数:"))
#     print(num1/num2)
# except ValueError:
#     print("请输入数值型")
# except ZeroDivisionError:
#     print("除数不为0")
# else:
#     print("程序没有异常")

# x = 5
# if x > 1:
#     raise Exception("这是一个异常")
class MyException(Exception):
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2
raise MyException("JJJJ")
