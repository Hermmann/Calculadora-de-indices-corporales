import calculadora_indices as calc

print("Esta función va a calcular el IMC\n")

peso= float(input("Ingrese el peso de la persona: "))
altura= float(input("Ingrese la estatura de la persona: "))

print("El BMI es de: "calc.calcular_IMC(peso, altura))