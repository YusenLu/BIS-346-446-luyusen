# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 01:47:50 2023

@author: Kubers
"""

# Exersice 2.12
p=1000
r=0.07
for i in range(1,4):
    a=round(p*(1+r)**(10*i),2)
    print(f'Deposit at the end of {10*i} year will be {a}' )