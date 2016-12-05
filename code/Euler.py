# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:54:22 2016

@author: James
"""

import utils.py

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


