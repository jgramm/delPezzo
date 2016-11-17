# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 16:53:55 2016

@author: James
"""

def readAll(fileName, delim=","):
    labels = []
    data = []    
    with open(fileName, "r") as f:
        line = f.readline().rstrip()
        tempLabels = line.split(",")
        
        for label in tempLabels:
            labels.append(label[1:-1])
        
        while line:
        dat = {}
        for i in range(len(labels)):
                r = line.split(",").rstrip()
                dat[labels[i]] = r[i]
        data.append(dat)
        

    return (labels, data)
    

        