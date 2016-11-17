# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 17:36:14 2016

@author: James
"""

def readCytable(fileName, delim=","):
    """ reads a cytable downloaded from Ross's site, and returns a dictionary,
        returns a list of dictionaries (data) where the keys are given in 
        the list labels. probably do not need to return labels, but oh well"""
    
    labels = []
    data = []
    
    ## open file    
    with open(fileName, "r") as f:
        ## rstrip cuts off trailing /n        
        line = f.readline().rstrip()
        tempLabels = line.split(delim)
        
        ## cut out open/close quotes
        for label in tempLabels:
            labels.append(label[1:-1])
        
        line = f.readline().rstrip()
        
        ## iterate through lines turning each row into a dictionary
        while line:
            
            dat = {}
            r = line.split(delim)
            
            for i in range(len(labels)):
                dat[labels[i]] = r[i]
            data.append(dat)
            
        line = f.readline().rstrip()
        
        
    return (labels, data)