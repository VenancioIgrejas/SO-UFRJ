#import library
import os
import sys
import time
import numpy as np
import pandas as pd
from multiprocessing import Process,Queue,Event,Pipe, Lock

from Functions.check import timer
from Functions.multiprocess import *


q = Queue(3)
q_answer = Queue()
event = Event()
send,read = Pipe()
lock = Lock()


# list_process = [Process(target=create_lines,args=(q,event,read)) for i in range(3)]
# list_process.append(Process(target=control_process,args=(q,event,send,lock)))
# for process in list_process:
#    process.start()
#
# for process in list_process:
#    process.join()



# work but with the same time if it wasn't parallel
with timer('processo terminado'):
    p = Process(target=father_proc,args=(q,q_answer))
    p.start()
    p.join()

    mt = q_answer.get()

# print the answer

list_df = [pd.DataFrame(mt[i]) for i in range(3)] # transform each line of mt in DataFrame and put in list

sudoku = pd.concat(list_df).values # transform the list of Dataframe in Dataframe matrix and return as np.array

print(sudoku)
