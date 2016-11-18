# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 11:01:20 2016

@author: James
"""
from sympy.diffgeom import WedgeProduct
from sympy import *
from sympy.geometry import *

def intersect(div1, div2):
    """ TODO: calculates the intersection of two toric divisors 
        TODO: make sure to handle null/trivial intersections properly """
    return Intersection(div1, div2)

def getCurves(divisors):
    """ gets all curve classes, a representation of which can be formed by 
        intersecting all divisors, pairwise 
        TODO: make sure to handle null/trivial intersections properly """
    
    curves = []    
    for i in range(len(divisors)):
        for j in range(i, len(divisors)):
            
            curves.append(intersect(divisors[i], divisors[j]))
            
            