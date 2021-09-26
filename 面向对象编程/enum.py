# !/usr/bin/env python3
# coding:utf-8
import enum


# 未限制枚举类
class WeekDays(enum.Enum):
    Monday = 1
    TUESDAY = 2
    WEDENESDAY = 3
    THURSDAY = 4
    FRIDAY = 10


day = WeekDays.FRIDAY
print(day)
print(day.name)
print(day.value)


# 限制枚举类
@enum.unique
class WeekDays(enum.IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEENDSDAY = 3
    THURSDAY = 4
    FRIDAY = 5


day = WeekDays.FRIDAY
print(day)
print(day.value)
print(day.name)



