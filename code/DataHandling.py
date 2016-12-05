# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:14:03 2016

@author: James

THIS FILE IS A MASSIVE SECURITY RISK, 
AS ALL INPUTS TO EVAL ARE COMPLETELY UNSANITIZED
USE AT YOUR OWN RISK

"""


def evalData(data):
    """ Takes in an unprocessed string version of all the data and spits out
        a list of dictionaries corresponding to each row of data """
    rows = []
    
    for datum in data:
        rows.append(evalRow(datum))
    
    return rows
    
    
    
def evalRow(datum):
    """ Finish me """
    row = {}
    row['id'] = evalID(datum)
    row['tensor'] = evalTensor(datum)
    row['divs'] = evalDivs(datum)
    row['toric'] = evalToric(datum)
    row['chern2'] = evalChern2(datum)
    
    
    return row

def evalDivs(datum):
    """ Returns dictionary of {Ji, Dk} """
    divs = datum['Basis from Toric Divisors']
    divs = divs[1:-1].replace('{', '[\'').replace('}', '\']')
    divs = eval(divs)
    
    divisors = {}
    
    for d in divs:
        s = d[0].split(',')
        divisors[s[0]] = s[1]
    
    return divisors
 
   
def fracStringToFloat(fracStr):
    """ If string is a fraction (represented as a/b), returns the float value 
        of the fraction, otherwise, returns the string as a float """
    s = fracStr.split('/')
    
    if (len(s) == 1):
        return float(s[0])
    else:
        #print(len(s))
        
        return float(s[0]) / float(s[1])        
    
    
def evalChern2(datum):
    """ parses the Chern Class basis into a set of tuples, where the first
        index is the coefficient, and the other two are the J indices """
    comps = datum['CY 2nd Chern Class (Basis)'].split('+')

    basis = []    
    print(comps)
    for v in comps:
        vi = v.split('*')
        
        if (len(vi) == 1):
            #print(vi[0])
            jIndP = vi[0].index('J') + 1
            basis.append((1, int(vi[0][jIndP]), int (vi[0][jIndP])))
        
        elif ((len(vi) == 2) and (vi[0][0] == 'J')):
            jInd0P = vi[0].index('J') + 1
            jInd1P = vi[1].index('J') + 1
            basis.append((1, int(vi[0][jInd0P]), int(vi[1][jInd1P])))

        elif (len(vi) == 2):
            jIndP = vi[1].index('J') + 1
            basis.append((fracStringToFloat(vi[0]), int(vi[1][jIndP]), int(vi[1][jIndP])))

        else:
            print(len(vi), vi)
            jInd1P = vi[1].index('J') + 1
            jInd2P = vi[2].index('J') + 1
            basis.append((fracStringToFloat(vi[0]), int(vi[1][jInd1P]), int(vi[2][jInd2P])))
    
    return basis

def evalID(datum):
    """ returns polytope id as an int """
    return int(datum['Polytope ID #'])



def evalToric(datum):
    """ Returns dictionary of {Di, Ak Jk} """    
    
    divs = datum['Toric from Basis Divisors']
    divs = divs[1:-1].replace('{', '[\'').replace('}', '\']')
    divs = eval(divs)
    
    divisors = {}
    for d in divs:
        s = d[0].split(',')
        divisors[s[1]] = s[0]
        
    return divisors


def evalTensor(datum):
    """ Parses Tensor Basis as a 3 tuple of 3 tuples of 3 tuples"""
    tijk = datum['CY Intersection Tensor (Basis)']
    t = tijk.replace("{","(").replace("}", ")")
    t = eval(t)    
    
    return t
    


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
        
        #print(len(labels))
        ## iterate through lines turning each row into a dictionary
        while line:
            #print(line)        
            
            dat = {}
            r = line.split(delim)
            
            for i in range(len(labels)):
                dat[labels[i]] = r[i]
            data.append(dat)
            
            line = f.readline().rstrip()
        
        
    return data
