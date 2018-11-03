import os
import sys
import time
import numpy as np
import pandas as pd
from check import debug
from multiprocessing import Process

#for use 'from Functions.multiprocess import *'
__all__ = ['debug',
           'create_lines',
           'control_process',
           'child_proc',
           'father_proc']


#Function with bug
def create_lines(q,event,read_msg):
    while True:
        np.random.seed()
        line_rdm = np.random.randint(1,10,size=(1,3))
        if len(np.unique(line_rdm)) == 3:
            q.put(line_rdm)
            debug('processo pra criar')
            event.clear()
            debug('passei do wait')
            print read_msg.poll()
            debug('passei da mensagem')
            if read_msg.poll() is 'finished':
                debug('acabou?')
                break


#Function with bug
def control_process(q,event,send_msg,lock):
    time.sleep(0.1)
    while True:
        debug(q.qsize())
        while not q.qsize() == 3:pass
        lock.acquire()
        list_tmp = []
        while not q.empty():
            list_tmp.append(q.get())

        print list_tmp
        if len(np.unique(list_tmp)) == 9:
            debug('consegui')
            #q.put(list_tmp)
            send_msg.send_bytes('finished')
            send_msg.close()
            event.set()
            debug('acabou')
            break
        else:
            debug(u'nao consegui')
            event.set()
        lock.release()

def child_proc(q):
    np.random.seed()
    line_rdm = np.random.randint(1,10,size=(1,3))
    if len(np.unique(line_rdm)) == 3:
         q.put(line_rdm)

def father_proc(q,q_sudoku):
    while True:
        list_process = [Process(target=child_proc,args=(q,)) for i in range(3)]
        for process in list_process:
            process.start()
        for process in list_process:
            process.join()

        list_tmp = []
        while not q.empty():
            list_tmp.append(q.get())

        if len(np.unique(list_tmp)) == 9:
            q_sudoku.put(list_tmp)
            break
