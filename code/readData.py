# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 17:36:14 2016

@author: James
"""

def readCytable(fileName, delim="\t"):
    """ reads a cytable downloaded from Ross's site, and returns a dictionary,
        returns a list of dictionaries (data) where the keys are given in 
        the list labels. probably do not need to return labels, but oh well.
        Have to deal with issue where csv files have tabs inside the strings 
        I assume this is why we have double quotes inside singles. """
    
    labels = []
    data = []
    
    ## open file    
    with open(fileName, "r") as f:
        ## rstrip cuts off trailing /n        
        line = f.readline().rstrip()
        tempLabels = line.split(delim)
        
        ## cut out open/close quotes
        for label in tempLabels:
            labels.append(label)
        
        line = f.readline().rstrip()
        
        print(len(labels))
        ## iterate through lines turning each row into a dictionary
        while line:
            print(line)        
            
            dat = {}
            r = line.split(delim)
            
            for i in range(len(labels)):
                dat[labels[i]] = r[i]
            data.append(dat)
            
            line = f.readline()#.rstrip()
        
        
    return (labels, data)
