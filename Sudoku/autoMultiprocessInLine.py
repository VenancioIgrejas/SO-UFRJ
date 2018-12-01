import os
import sys
import time
import argparse
import subprocess
#configurate argsv for enter the program

parser = argparse.ArgumentParser(description='Program for run the file multiprocessInLine.py N times for generate the result in csv file format')

parser.add_argument('-n', '--number_of_run',
		type=int, default=1,
		help='number of times that run the program')

parser.add_argument('-p', '--number_of_process',
		type=int, default=1,
		help='number of process for run parallel the program')

args = parser.parse_args()

list_coringa = []

#if you want run only one process in the program comment the line with respective of list_corring variable
#list_coringa = range(3000, 11000, 1000)


#run n times the current program

#coringa for run N times M process, make more easy to construnct the CSV file with results

if list_coringa: # if list is not empy, do this
    for iprocess in list_coringa:
        if iprocess is 0:
            iprocess = iprocess + 1 # not exist 0 process, but 1 exist ..... serial program
        print 'start program with {0} number of process'.format(iprocess)
        for irun in range(args.number_of_run):
            print('start program {0} of {1}'.format(irun, args.number_of_run))
            subprocess.call(['python', 'multiprocessInLine.py','-n',str(iprocess)])

    sys.exit()



for irun in range(args.number_of_run):
    print('start program {0} of {1}'.format(irun+1,args.number_of_run))
    subprocess.call(['python', 'multiprocessInLine.py','-n',str(args.number_of_process)])

print('finished run {0} programs'.format(args.number_of_run))
