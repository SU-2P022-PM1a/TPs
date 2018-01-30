# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:09:44 2018

@author: 3673029
"""

def dés(n):
    """donne le nombre de façons s de faire n en lançant 3 dès"""
    while n<3 or n>18:
        n=int(input('ENTRE 3 ET 8!!! '))
    s=0
    for i in range(1,7):
        for k in range(1,7):
            for m in range(1,7):
                if (i+k+m)==n:
                    s=s+1
    print("le nombre de façons s de faire n en lançant 3 dès est")
    return s
    
n=int(input('Entrez un nombre entre 3 et 18 '))
dés(n)

