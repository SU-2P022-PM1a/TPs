#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:10:50 2018

@author: Louis CHRISTIENNE 3670026
"""
from __future__ import division
import math


def convert_F_to_C( tempF ) :
    """ temperature in Farenheit ( < -459.67) --> temperature in Celcius"""
    return (tempF - 32.0) * 5/9


def dice_result():
    n = 0
    s = 0
    while not( n <= 18 and n >= 3):
        n = int(input("Enter an integrer between 3 and 18 : "))
    for d1 in range(1,7):
        for d2 in range(1,7):
            for d3 in range(1,7):
                if (d1+d2+d3) == n:
                    s += 1
    print" There are {:d} ways to obtain {:d} with 3 dices.".format(s, n)
    return 0


def minMaxMoy (listIn):
    mini = maxi = moy = listIn[0]
    for elem in listIn[1:]:
        if elem < mini:
            mini = elem
        if elem > maxi:
            maxi = elem
        moy += elem
    moy /= len(listIn)
    print "minimum : {:d} maximum : {:d} average : {:.2f}".format(mini, maxi, moy)
    return 0

   
def pi_approx(p):
    pi = 0.0
    for i in range(1,p+1):
        if i%2 == 0:
            pi -= 1/(2*i-1)
        else:
            pi+= 1/(2*i-1)
    return pi*4
    

def perimeter(a,b):
    return 2*(a+b)


def sphere(r):
    return [4*math.pi*r*r, 4/3*math.pi*r*r*r]
    

def factorielle(n):
    #n == 0 :
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact


def syracuse(n):
    i = 0
    #if error infinite loop == 1M$
    while n != 1:
        if n%2 == 0:
            n /= 2
        else :
            n = (n*3) + 1
        i += 1
    return i
    

def heaviside(table):
    tableOut = list()
    for i in table:
        if i >= 0:
            tableOut.append(1)
        else:
            tableOut.append(0)
    return tableOut


tempF = input("Enter a temperature in Farenheit : ")
if tempF < -459.63 :
    print "ERROR : temperature under absolute zero"
else:
    print "Your temperature converted to Celcius : ", (tempF - 32.0) * 5/9
    
print convert_F_to_C(232)

dice_result()

a = [10, 18, 14, 20, 12, 16]
minMaxMoy(a)
a.extend([23,3,4])
minMaxMoy(a)
print a

for i in range(1,10):
    print pi_approx(i)
    
print "the permieter of a square 2 meters long is : ",perimeter(2,2)

print "A sphere with a radius of 1 have a surface of : ",sphere(1)[0], " and a volume of : ", sphere(1)[1]

print " 4! = ",factorielle(4)

print "Syracuse(321) :",syracuse(321)

#C'est marrant j'ai pas fait exprès pour le syracuse(321)=4!

x = list()
for i in range(100):
    x.append(-1 + i/49.5)
print x
print heaviside(x)