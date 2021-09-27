# !/usr/bin/env python3
# coding:utf-8


import datetime as dt


def read_date_from_file(filename):
    try:
        in_date = open(filename)
        in_date = in_date.strip()
        date = dt.datetime.strptime(in_date, '%Y-%m-%d')
        return date
    except (ValueError, OSError) as e:
        print('调用任意方法处理......')
        print(e)
