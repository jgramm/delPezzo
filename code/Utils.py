# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 03:34:26 2016

@author: James
"""

def parseStr(str):
    
    j = str.split('*')

    if (len(j) == 1):
        if(j[0] == '-'):
            coeff = -1
        else:
            coeff = 1
        jIndP = j[0].index('J') + 1
        jVal = (coeff, int(j[0][jIndP]))
    
    else :
        jIndP = j[1].index('J') + 1
        jVal = (int(j[0]), int(j[1][jIndP]))
    
    return jVal
            
            
            

def diStrToJVals(diStr, row):
    """ Returns a list of 2 tuples (Ai i) with i representing the index of J
        and Ai representing its leading coefficient """    
    
    Js = row['toric'][diStr]    
    jVals = []
    
    lastInd = 0
    for i in range(len(Js)):
        if(i != 0 and Js[i] == '-' or Js[i] == '+'):
            jVals.append(parseStr(Js[lastInd:i]))
            lastInd = i
                
        #elif(Js[i] = '+'):
        #    jVals.append(parseStr(Js[lastInd:i]))
        #    lastInd = i
            
    return jVals