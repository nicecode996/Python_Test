# !/usr/bin/env python3
# coding:utf-8

# 几何图形
class Figure:
    def draw(self):
        print('绘制Figure')


# 椭圆形
class Ellipse(Figure):
    def draw(self):
        print('绘制Ellipse')


# 三角形
class Triangle(Figure):
    def draw(self):
        print('绘制Triangle')


f1 = Figure()  # 未发生多态
f1.draw()

f2 = Ellipse()  # 发生多态
f2.draw()

f3 = Triangle()  # 发生多态
f3.draw()

print(isinstance(f1, Triangle))
print(isinstance(f2, Triangle))
print(isinstance(f3, Triangle))
print(isinstance(f2, Figure))  # F2是Figure的实例因此表达式返回True

print(issubclass(Ellipse, Triangle))  # 函数判断Ellipse是否是Triangle的子类
print(issubclass(Ellipse, Figure))
print(issubclass(Triangle, Ellipse))
