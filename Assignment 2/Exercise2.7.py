# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 23:14:48 2023

@author: Kubers
"""

# Excercise 2.8
#left align
A=[]
B=[['number','square','cube']]
for i in range(6):
    A+=[(i,i**2,i**3)]
C=B+A
for j in range(7):
    for i in range(3):
        if j==0 and i<2:
            print(C[j][i],end='\t\t')
        elif i<2:
            print(C[j][i],end='\t\t\t')
        else:
            print(C[j][i],end='\n')

#right align
for number in range(6):
    square = number ** 2
    cube = number ** 3
    if number!=0:
        print(f'{number:>10}{square:>10}{cube:>10}')
    else:
        print(f'{"number":>10}{"square":>10}{"cube":>10}')
    
    