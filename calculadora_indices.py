def calcular_IMC(peso:float, altura:float) -> float:
    
    BMI = round(peso/(altura)**2, 2)
    
    
    return BMI
    

def calcular_porcentaje_grasa(peso:float, altura:float, edad:int,
                              valor_genero: float):
        
    por_Grasa_Corp= 1.2*calcular_IMC(peso, altura)+ 0.23*edad-5.4-valor_genero
    
    return(round(por_Grasa_Corp,2))
    


def calcular_calorias_en_reposo(peso:float, altura:float, edad:int,
                                valor_genero: float):
    TMB= (10*peso) + (6.25*altura) - (5*edad) + valor_genero
   
    return(round(TMB,2))
    

def calcular_calorias_en_actividad(peso:float, altura:float, edad:int,
                        valor_genero: float, valor_actividad:float):
    TMBactividad= calcular_calorias_en_reposo(peso, altura, edad, valor_genero)*valor_actividad 
    
    return(round(TMBactividad,2))
   

def consumo_calorias_recomendado_para_adelgazar(peso:float, altura:float, edad:int,
                        valor_genero: float)->  str:
    xxx= calcular_calorias_en_reposo(peso, altura, edad, valor_genero) - calcular_calorias_en_reposo(peso, altura, edad, valor_genero)*0.20
    
    zzz= calcular_calorias_en_reposo(peso, altura, edad, valor_genero) - calcular_calorias_en_reposo(peso, altura, edad, valor_genero)*0.15
    
    return("Para adelgazar es recomendado que consumas entre: "+str(round(xxx,2))+" y " +str(round(zzz,2))+ " calorías al día.")

". Siendo XXX el rango inferior y ZZZ el rango superior."
    

