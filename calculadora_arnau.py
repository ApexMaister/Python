#coding: utf-8

import os

os.system('clear')


print "Que desea hacer el amo?"
print " "
print "S-  Sortir de la Calculadora"
print "1-  Sumar"
print "2-  Restar"
print "3-  Multiplicar"
print "4-  Dividir"

print " "

ordre = raw_input("Escull una opcio:  ")

if ( ordre >= "1" and <= "4" or ( ordre == "s") or ( ordre == "S")

else
    print "Incorrecte"

if ordre == "1" :

    numero1 = input("Posa el 1er numero que vols sumar :   ")

    numero2 = input("Posa l altre num que vols sumar:  ")


    os.system('clear')


    print numero1 + numero2


if ordre == "2" :

    numero1 = input("Posa el 1er numero que vols restar :   ")

    numero2 = input("Posa l altre num que vols restar:  ")


    os.system('clear')


    print numero1 - numero2




if ordre == "3" :


    numero1 = input("Posa el 1er numero que vols Multiplicar :   ")

    numero2 = input("Posa l altre num que vols Multiplicar:  ")


    os.system('clear')


    print numero1 * numero2



if ordre == "4" :


    numero1 = input("Posa el 1er numero que vols Dividir :   ")

    numero2 = input("Posa l altre num que vols Dividir:  ")


    os.system('clear')


    print numero1 / numero2


if ordre == "S":

    exit
