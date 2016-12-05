# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:55:32 2016

@author: James
"""
from Utils import *
from DataHandling import *
from Computation import *
from Params import *

def main():
    fileName = dataDir + 'h4.csv'
    data = readCytable(fileName)
    rows = evalData(data)
    
    count = 0
    for row in rows:
        print(count)
        for i in range(7):
            k2 = getK2('D' + str(i+1), row)
            eul = euler('D' + str(i+1), row)
            print(k2, eul, int(9-k2), int(eul-3))
            if(9-k2 == eul-3):
                print('FUCK YEAH WE FOUND ONE')
                print(count, 'D' + str(i+1))
        count += 1
    
    #fileName = query(searchTerms)
    #preprocessFile(fileName)
#    divisors = getDivisors(data)
    
    

if __name__ == "__main__": main()