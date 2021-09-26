#! usr/bin/env python3
# coding=utf-8


import os

print(os.getcwd())

print(os.path.abspath(__file__))

# 定义路径
maxu = os.path.dirname(os.path.abspath(__file__))
# 路径拼接
print(os.path.join(maxu, 'yaml.xls'))

try:
    data_path = os.path.join(maxu, 'maxu1.doc')
    print(os.mkdir(data_path))
finally:
    data_path = os.path.join(maxu, 'maxu1.doc')
    print(os.mkdir(data_path))


# 判断是否是一个文件夹
print(os.path.isdir(maxu))
print(os.path.isdir('maxu1.doc'))
# 判断是否是一个文件

print(os.path.isfile(maxu))

print(os.path.abspath('for.py'))

print(os.path.exists("maxu1.doc"))
if not os.path.exists("maxu1.doc"):
    os.mkdir("maxu1.doc")
if not os.path.exists("maxu1.doc/maxu2021.txt"):
    f = open("maxu1.doc/maxu202", "w")
    f.write("hello word")
    f.close()

dir_name = os.path.abspath(__file__)
maxu.doc = os.path.join(dir_name, 'maxu1.doc' )
f = open(maxu.doc)
print(f)

f = open('maxu/maxu.txt', 'rt')
print(f.read())
