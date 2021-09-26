# !/usr/bin/env python3
# coding:utf-8


# __srt__()方法

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        template = 'Person [name={0},age{1}]'
        s = template.format(self.name, self.age)
        return s


person = Person('Tony', 18)
print(person)


# 对象比较方法
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        template = 'Person [name{0},age{1}]'
        s = template.format(self.name, self.age)
        return s

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False


p1 = Person('Tony', 18)
p2 = Person('Tony', 18)

print(p1 == p2)
