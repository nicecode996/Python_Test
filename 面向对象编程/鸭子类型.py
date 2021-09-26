# !/usr/bin/env python3
# coding:utf-8


class Animal(object):
    def run(self):
        print('动物跑')


class Dog(Animal):
    def run(self):
        print('狗狗跑')


class Car:
    def run(self):
        print('汽车跑')


def go(animal):
    animal.run()


go(Animal())
go(Dog())
go(Car())
