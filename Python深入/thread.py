#! usr/bin/env python3
# coding=utf-8
import _thread
import logging
import threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

"""基本概念：什么是进程？
    进行是执行中的程序
    拥有独立地址空间、内存、数据栈
    操作系统管理
    派生（fork或spawn）新进程
    进程间通信（ipc）方式共享信息
    进程可以并行执行
"""
"""什么是线程？
    同进程下执行，并共享相同的上下文
    线程间的信息共享和通信更容易
    多线程并发执行
    需要同步原语
"""
"""GIL锁保证只有一个线程执行
        _thread:提供了基本的线程和锁
        threading：提供了更高级别和、功能更全面的线程管理
        支持同步管理
        支持守护进程
"""


def loop0():
    logging.info("start loop0 at " + ctime())
    sleep(4)
    logging.info("end loop0 at " + ctime())


def loop1():
    logging.info("start loop1 at " + ctime())
    sleep(2)
    logging.info("end loop1 at " + ctime())


def main():
    logging.info("start all loop at " + ctime())
    # 普通方法未引用进程概念
    # loop0()
    # loop1()
    _thread.start_new_thread(loop0, ()) # 使用本方法记得加等待时间，否则主线程结束是子线程会被kill掉，此处loop0.1都是此线程，不守护线程
    _thread.start_new_thread(loop1, ())
    sleep(5)
    logging.info("end all loop at " + ctime())




loops = [2, 4]


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    logging.info("start loop" + str(nloop) + "at" + ctime())
    sleep(nsec)
    logging.info("end loop" + str(nloop) + "at" + ctime())
    # lock.release()


def main():
    logging.info("start all at" + ctime())
    # teread方法
    locks = []
    nloops = range(len(loops))
    for i in loops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in loops:
        _thread.start_new_thread(loop, (i, loops(i), locks[i]))
    for i in loops:
        while locks[i].locked():
            pass
            
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at" + ctime())



    # _thread不能守护线程，主线程执行完毕，子线程就被杀死了
    # _thread.start_new_thread(loop0(), ())
    # _thread.start_new_thread(loop1(), ())
    # sleep(6)
    # loop0()
    # loop1()
    
if __name__ == '__main__':
    main()

