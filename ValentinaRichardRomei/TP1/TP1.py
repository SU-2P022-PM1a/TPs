# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import math

a=2
b=7.2*math.log(math.e/45.12)-2*math.pi
c=b**a
c

b=2*2
b
a=b+5
a


a=1
b=2
a,b=b,a
print(a, b)


variable_x=10
variable_x

type(a)

x=10
y=10.0
z=x
y=2.5e4
y
y=2.5e16
y

int("300")
str(300)
float(10)
int(3.99)
bool(1)
bool(-12345)

tf=189
tc=(tf-32)*5/9
tc

suite=[["a","b"],["c","d"]]
suite [1][0]

list_1=list(range(4,8,3))
list_1

nombres=[17,38,10,25,72]
nombres.sort()
nombres
nombres.append(12)
nombres.reverse()
nombres.remove(38)
nombres

nombres.index(17)
nombres[0]=11
nombres[1:3]=[14,17,2]
nombres.pop()
nombres

truc=[]
machin=[0.0]*5
truc
machin
list_1=list(range(4))
list_1
list_2=list(range(4,8))
list_2
list_3=list(range(2,9,2))
list_3

chose=list(range(6))
chose
3 in chose
6 in chose

x=-10
print("Avant if")
if x>0:
        print("Dans if")
else:
    print ("non")
print("Après if")

x=0
if x>0:
    print("positif")
elif x<0:
    print("négatif")
    

tf=189

T_in_F=float(input('entrer température en fahrenheit: '))
if T_in_F <-459.67:
    print("erreur")
else :
    tc=(T_in_F-32)*5/9
    print(tc)


2000

for i in range(5):
    print(i)
print ("après la boucle for, i=", i )

i=0
while i<5:
    print(i)
    i=i+1
print ("après la boucle while, i=", i)


chaine = input("Entrer votre message avec input:\n")
print ("vous avez entre:",chaine,type(chaine))

def hello():
    print("bonjour")
    
hello()

def afficheAddMul (a,b):
    """calcule et affiche la somme et le produit"""
    somme=a+b
    produit=a*b
    print("la somme de", a,"et",b,"est",somme,"et le produit",produit)
    
a=1
b=2.5
afficheAddMul(a,b)

def cube (z):
    """retourne le cube de largument"""
    return z**3

x=2
y=cube(x)
print("cube de",x,"est",y)

x=5.0
print("cube de",x,"est",cube(x))