# -*- coding: utf-8 -*-
__author__ = 'qxwang'

#Entropy of information
import string, sys, os
import re
import math
import numpy as np

dict = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

#dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', \
#        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

notProtein = ['B', 'J', 'O', 'U', 'X', 'Z']

file_path0 = '/home/qxwang/workspace/PythonDemo/file'
matchSquence0 = r'^S\w{7}\s\d'

file_path_animal = '/home/qxwang/workspace/PythonDemo/animal.txt'
file_path_plant = '/home/qxwang/workspace/PythonDemo/plants.fasta'
matchSquence1 = r'>gi*'

MAX_DATA_ROW = 1000

def nonlin(x,deriv=False):
    if(deriv==True):
        return  x*(1-x)
   
    return  1/(1+np.exp(-x))

# judge whether aset contain the character which is not in seq or not
def containAny(seq,aset):
    for c in seq:
        if c in aset:
            return True
    return False

def data2Matrix(file_path, matchSquence, MAX_DATA_ROW):
    
    datafile = open(file_path)
    
    aline = datafile.readline()
    proteaseSeq = {}
    seqStart = 0
    seqKey = aline.strip('\n')
    seqValue = ''
    
    Data_Len = 0
    count_N = 0
    while aline:
        
        if re.match(matchSquence, aline) and seqStart:
            Data_Len += 1
            seqKey = aline.strip('\n')
            seqValue = ''
#            count_N += 1
        else:
            if not seqStart:
                seqStart = 1
                continue
            else:
                seqValue += aline.strip('\n')
    
        aline = datafile.readline()
    
        if re.match(matchSquence, aline) or not aline:
            proteaseSeq[seqKey] = seqValue
        
#        if count_N ==MAX_DATA_ROW:
#            break
            
    datafile.close()
    print Data_Len
    numProtein = len(dict)
    row = 0
    entropyMatrix = np.zeros( (MAX_DATA_ROW, numProtein) )
    
    for seqKeyName in proteaseSeq:
        pro_tmp_str = proteaseSeq[seqKeyName]
        if containAny(notProtein,pro_tmp_str):
            continue
        else:
            pro_tmp_len = len(pro_tmp_str)
            #    print pro_tmp_len
            #    print pro_tmp_str
            count_N += 1
            for order in range(numProtein):
                pro = pro_tmp_str.count( dict[order] )/float(pro_tmp_len)
                if pro == 0.0:
                    entropyMatrix[row, order] = 0.0
                else:
                    entropyMatrix[row, order] = -pro*math.log(pro)
            
            row += 1
            
            if count_N ==MAX_DATA_ROW:
                break
        
    return entropyMatrix
    
def createData():
    # generate a input data file ------- Demo---
    if  os.path.exists('./testdata_tmp'):
        os.remove('./testdata_tmp')
        print 'remove the file successfully!'
        
        f = file('testdata_tmp','a+')
    else:
        f = file('testdata_tmp','a+')
    
    data_YES = data2Matrix(file_path_animal,matchSquence1,MAX_DATA_ROW)
    data_NO  = data2Matrix(file_path_plant,matchSquence1,MAX_DATA_ROW)
        
    row0, col0 = np.shape(data_YES)
    row1, col1 = np.shape(data_NO)
    print row0,row1,col0,col1
    
    row = row0
    for i in range(row/2):
        for j in range(col0):
            f.write(str(data_YES[i][j])+' ')
        f.write('1.0')
        f.write('\n')
    
        for j in range(col1):
            f.write(str(data_NO[i][j])+' ')
        f.write('-1.0')
        f.write('\n')
        
    for i in range(row/2):
        for j in range(col0):
            f.write(str(data_YES[row/2+i][j])+' ')
  
        f.write('1.0')
        f.write('\n')
    
        for j in range(col1):
            f.write(str(data_NO[row/2+i][j])+' ')
        
        f.write('-1.0')
        f.write('\n')
    
    f.close()

