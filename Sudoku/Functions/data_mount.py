import os
import numpy as np
import pandas as pd
import csv

class CSVfile(object):
    """docstring forCSVfile."""
    def __init__(self,pathfile='./',column=10):

        file = os.path.join(pathfile,'time_{0}_process.csv'.format(column))

        if not os.path.exists(file):
            with open(file,'w') as csvfile:
                writer = csv.DictWriter(csvfile,fieldnames=[column])
                writer.writeheader()

        self.file = file
        self.column = column

    def add_element(self,value):

        if not isinstance(value,str):
            value = str(value)

        with open(self.file,'a') as csvfile:
            writer = csv.writer(csvfile)
            #writer = csv.DictReader(csvfile,fieldnames=list(str(self.column)))
            writer.writerow([value])

    def get_data(self,type='DataFrame'):

        df = pd.read_csv(self.file)#,date_format=float())

        if type is 'array':
            return df.values

        return df
