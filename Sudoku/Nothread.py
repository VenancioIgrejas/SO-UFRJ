import os
import sys
from conf import conf_env
import numpy as np
import pandas as pd

# function for using function in Functions folder 
conf_env()

from Functions.check import check_sudoku,timer

#inicialize matriz
with timer('calculating matrix'):
    flag = False
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        rdw_mt = np.random.randint(1,10,size=(3,3))
        print rdw_mt
        if check_sudoku(rdw_mt):
            break
