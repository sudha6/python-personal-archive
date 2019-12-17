#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: Sudha
Source:
    
'''

# Import necessary modules

import xlrd


def startpy():
    loc = "Mark_sample.xlsx" 
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    print(sheet.cell_value(0,1))
    print(sheet.nrows)
    print('\t')


    for i in range (sheet.nrows):
        #print (sheet.row(i))
        for j in range (sheet.ncols):

         print (sheet.cell_value(i,j))
        print('\t')





if __name__ == '__main__':
    startpy()