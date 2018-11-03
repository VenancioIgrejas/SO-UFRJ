import pandas as pd
import numpy as np
import time
from contextlib import contextmanager

@contextmanager
def timer(name):
    t0 = time.time()
    yield
    print('[{0}] done in {1} s'.format(name,time.time() - t0))


def check_sudoku(sudoku):
    """ Function for check if matriz is sudoku (only have number from 1 to 9 in
        the matriz without replacement)

        :input: (numpy.array [3x3])
        :return: (bool) if the matriz it's in Sudoku form
    """

    #list_of_number_avaliable = range(1,10)

    #sum_list = sum(list_of_number_avaliable) #will be 45

    #sum_all_element_sudoku = sudoku.sum() # need to be equal 45

    if len(np.unique(sudoku)) == 9 :
        return True
    return False

def debug(msg='defaul'):
    print "{0}".format(msg)
