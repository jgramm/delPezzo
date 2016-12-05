# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 06:30:59 2016

@author: James
"""

import utils

def euler(diStr, row):
    """ Computes the Euler characteristic of the divisor represented by 
        diStr for the given row """
    jVals = diStrToJVals(diStr, row)
    
    c2 = row['chern2']
    euler = 0
    
    for a in jVals:
        for b in c2:
            euler += a[0] + b[0] * tensor[a[1]-1][b[1]-1][b[2]-1]

    return euler
    
    
def getK2(diStr, row):
    #print(diStr, row)
    jVals = diStrToJVals(diStr, row)
    #DInd = int(diStr[1])
    
    k2 = 0
    tensor = row['tensor'] 
    for a in jVals:
        for b in jVals:
            for c in jVals:
                k2 += a[0] * b[0] * c[0] * tensor[a[1]-1][b[1]-1][c[1]-1]
                
    return k2