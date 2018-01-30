# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

couleurs = ['bleu', 'vert', 'rose', 'orange']
print (couleurs)
couleurs[1]=15
print (couleurs)

x = 10
print("avant if")
if x>0:
    print("dans if")
print("après if")


#exercices 6.3

def F_to_C(Tf):
    """convertit une temperature de Fahrenheit en Celsius"""
    Tc = (Tf-32)*5/9
    return Tc

#Tf = float(input('entrez la température en Fahrenheit: '))
#while Tf<-459.67:
    #print("attention votre temperature est en dessous de zéro !!") 
    #Tf = float(input('entrez la température en Fahrenheit: '))
 
#print('la temperature en Celsius est ', F_to_C(Tf) )


def F_to_C_new(Tf):
    """ convertit une temperature de Fahrenheit en Celsius"""
    while Tf<-459.67:
        print("attention votre temperature est en dessous de zéro !!") 
        Tf = float(input('entrez la température en Fahrenheit: '))
    print('la temperature en Celsius est ')
    return F_to_C(Tf)


