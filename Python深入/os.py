#! usr/bin/env python3
# coding=utf-8
import os

os.mkdir("maxu3")
print(os.listdir("./"))
os.removedirs("maxu")
print(os.getcwd())
'''
print(os.path.exists("maxu"))
if not os.path.exists("maxu"):
    os.mkdir("maxu")
if  not os.path.exists("maxu/maxu.txt"):
    f = open("maxu/maxu.txt","w")
    f.write("hello word")
    f.close()
'''
# 读取文件测试
f = open('maxu/maxu.txt', 'rt')
print(f.read())