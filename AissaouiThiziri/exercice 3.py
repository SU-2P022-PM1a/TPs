# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:08:54 2018

@author: 3673029
"""

def minMaxMoy(liste):
    """ définis le minimum le maximum et la moyenne des éléments d'une lise"""
    min=liste[0]
    max=liste[0]
    l=len(liste)
    somme=0
    for i in range(0,l):
        if liste[i]<min:
            min=liste[i]
        if liste[i]>max:
            max=liste[i]
        somme=somme+liste[i]
        
    return min, max, somme/l
    