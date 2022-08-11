# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:46:14 2022

@author: herma
"""

import calculadora_indices as calc

print("Esta función sirve para calcular las calorias en reposo\n")

peso= float(input("Ingrese el peso de la persona: "))
altura= float(input("Ingrese la estatura de la persona: "))
valor_genero= float(input("el género de la persona es masculino debe ser 5  y en caso de ser femenino debe ser -161: "))

edad= int(input("Ingrese la edad de la persona: "))

print("las calorias en reposo son: " 
      +str(calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)) +" cal")

