#import library
import os
import sys
import time
import numpy as np
import pandas as pd
import argparse

#configurate argsv for enter the program

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-n', '--number_of_process',
		type=int, default=1,
		help='number of process for run parallel the program')

from multiprocessing import Process, Queue, Event, Pipe, Lock

from Functions.check import timer, check_sudoku
from Functions.multiprocess import *
from Functions.data_mount import CSVfile

args = parser.parse_args()

count = 0
q_answer = Queue()
number_of_process = args.number_of_process


t_start = time.time()
list_tmp = []

while True:

    list_process = [Process(target=father_proc,args=(q_answer,)) for i in range(number_of_process)]
    for process in list_process:
        process.start()
    for process in list_process:
        process.join()

    while not q_answer.empty():
        list_tmp.append(q_answer.get())

    count=count+1

    if list_tmp:
        break


t_finish = time.time()
duration = t_finish - t_start
print "process done in {0} with {1} batch process".format(duration, count)

csv = CSVfile('./Results',number_of_process)

csv.add_element(duration)

# print the answer

#list_df = [pd.DataFrame(list_tmp) for i in range(3)] # transform each line of mt in DataFrame and put in list

list_df = pd.DataFrame(list_tmp[0])
sudoku = list_df.values#pd.concat(list_df).values # transform the list of Dataframe in Dataframe matrix and return as np.array

print(sudoku)
