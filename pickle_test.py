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

import pickle

def startpy():


    a = {'name' : 'Sudha', 'age' : '19'}
    #c="Welcome to programming... :P"

    file_Name = "commands.txt"
    # open the file for writing
    fileObject = open(file_Name,'wb') 

    # this writes the object a to the
    # file named 'testfile'
    pickle.dump(a,fileObject)   
    #pickle.dump(c,fileObject)

    # here we close the fileObject
    fileObject.close()
    # we open the file for reading
    fileObject = open(file_Name,'rb')  
    # load the object from the file into var b
    b = pickle.load(fileObject)  
    print(b)
    print(b['age'])



if __name__ == '__main__':
    startpy()