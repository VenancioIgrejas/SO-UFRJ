import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0,'/home/venancio/Dropbox/UFRJ/7periodo/SisOper/trabalho/SO-UFRJ/Sudoku/Functions')

from Functions.check import check_sudoku,timer

#inicialize matriz
with timer('calculating matrix'):
    flag = False
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        sudoku = np.random.randint(1,10,size=(3,3))
        print sudoku
        if check_sudoku(sudoku):
            break
