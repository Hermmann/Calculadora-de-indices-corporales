# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:46:47 2022

@author: herma
"""

import calculadora_indices as calc

print("Esta función sirve para calcular el rango de consumo de calorias para adelgazar\n")

peso= float(input("Ingrese el peso de la persona: "))
altura= float(input("Ingrese la estatura de la persona: "))
edad= int(input("Ingrese la edad de la persona: "))
valor_genero= float(input("el género de la persona es masculino debe ser 5  y en caso de ser femenino debe ser -161: "))



print(calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero))