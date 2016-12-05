# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:54:10 2016

@author: James
"""

import utils

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