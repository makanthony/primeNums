# -*- coding: utf-8 -*-
"""
Nov 30 2022

Anthony Mak
"""

numCap = 1000 #only looking for numbers under 1000
numPrimes = 0 #counts the number of primes
currNum = 2 #testing with 1 will give false negatives and 0 will break the program (unless python handles imaginary numbers? unneccessary fort this anyways though)
print (f'Prime numbers up to {numCap}: ') #should put the primes in a list and print all at once maybe ill go back and add that later

while currNum <= numCap: 
    prime = 1
    testNum = 2
    
    while testNum < currNum:
        if currNum % testNum == 0:
            prime = 0
            break
        testNum +=1
        
    if prime == 1:
        print(currNum)
        numPrimes += 1
        
    currNum += 1
    
print (f'There were {numPrimes} primes under {numCap}') #