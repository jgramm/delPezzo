# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 03:06:20 2016

@author: James
"""

def getSymbolicDivisors(datum):
    """ gets the toric divisors out of a CY polytope in terms of J_i """
    
    divisors = []
    
    ## Di are toric divisors, Ji are basis divisors
    toric = datum['Toric from Basis Divisors'] 
    ## remove brackets    
    toric = toric.translate({ord(c): None for c in '{}'})
    splitToric = toric.split(',')
    
    for i in range(len(splitToric)):
        if (i%2) = 1:
            divisors.append(splitToric[i])
    
    return divisors
    
    
def getExplicitDivisors(datum):
    """ gets an explicit expression for the toric divisors from the 
        CY Polytope"""
        
    symbs = getSymbolicDivisors(datum)
    
    