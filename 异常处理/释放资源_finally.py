# !/usr/bin/env python3
# coding:utf-8


import datetime as dt


def read_date_from_file(filename):
    try:
        file = open(filename)
        in_date = file.read()
        in_date = in_date.strip()
        date = dt.datetime.strptime(in_date, '%Y-%m-%d')
        return date
    except ValueError as e:
        print('处理ValueError异常')
    except FileNotFoundError as e:
        print('处理FileNotFound异常')
    except OSError as e:
        print('处理OSError异常')
    finally:
        file.close()


date = read_date_from_file('readme.txt')
print('日期 = {0}'.format(date))
