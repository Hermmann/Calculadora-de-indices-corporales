# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:46:30 2022

@author: herma
"""

import calculadora_indices as calc

print("Esta función sirve para calcular las calorias en actividad\n")

peso= float(input("Ingrese el peso de la persona: "))
altura= float(input("Ingrese la estatura de la persona: "))
edad= int(input("Ingrese la edad de la persona: \n"))
valor_genero= float(input("el género de la persona es masculino debe ser 5 y en caso de ser femenino debe ser -161: "))




print("Valor que depende de la actividad física semanal:"
"• 1.2: poco o ningún ejercicio"
"• 1.375: ejercicio ligero (1 a 3 días a la semana)"
"• 1.55: ejercicio moderado (3 a 5 días a la semana)"
"• 1.725: deportista (6 -7 días a la semana)"
"• 1.9: atleta (entrenamientos mañana y tarde)\n")

valor_actividad= float(input("Ingrese el valor de actividad: "))


print("las calorias en reposo son: " 
      +str(calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)) +" cal")