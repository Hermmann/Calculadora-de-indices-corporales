# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:45:52 2022

@author: herma
"""

import calculadora_indices as calc

print("Esta función sirve para calcular el porcentaje de grasa\n")

peso= float(input("Ingrese el peso de la persona: "))
altura= float(input("Ingrese la estatura de la persona: "))
valor_genero= float(input("el género de la persona es masculino debe ser 10.8 y en caso de ser femenino debe ser 0: "))

edad= int(input("Ingrese la edad de la persona: \n"))



print("El porcentaje de grasa es: " 
      +str(calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero))+"%")