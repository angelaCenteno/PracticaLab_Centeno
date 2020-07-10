# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:30:01 2020

@author: Angela
"""


numero = int(input("Ingresa un numero: "))
i = 0

while numero > 0:
    i = i + 1
    resto = numero % 10
    numero = int(numero / 10)
    print("%d" % (resto), end = "")