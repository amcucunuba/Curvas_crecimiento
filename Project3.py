import pandas as pd
import numpy as np
import math
from datetime import datetime
from dateutil.relativedelta import relativedelta

dfniñas_mayor_6_años =  pd.read_excel("C:\\Users\\User\\Documents\\Ejercicio Python\\bmi-girls-z-who-2007-exp.xlsx")
dfniños_mayor_6_años =  pd.read_excel("C:\\Users\\User\\Documents\\Ejercicio Python\\bmi-boys-z-who-2007-exp.xlsx")

#Datos que el usuario debe ingresar
nombre = input("Ingrese el nombre de su bebé:  ")
fecha_ingresada = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
genero_ingresado = input("Ingrese el género, Femenino  F o Masculino M:  ")
talla_ingresada = float(input("Ingrese la talla en cm:  "))
peso_ingresado = float(input("Ingrese el peso en kg:  "))

def calcularBMI(p, a):
    return p / (a * a)

def analisis_BMI_mayores_5_años(df, edad, BMI):
    if  edad < 60 or edad > 215:
        print("Verifique los datos ingresados, fecha de nacimiento")
#filtro del df deacuerdo a la talla ingresa por el usuario, iterando la serie lista de pesos
    else:      
        filtro1= df[(df["Month"] == edad)]  
       #print(filtro1)  
        encontrar_BMI_lista = (filtro1.loc[:,['SD4neg','SD3neg','SD2neg', 'SD1neg', 'SD0','SD1', 'SD2','SD3','SD4']])
        diferencias = abs(encontrar_BMI_lista - BMI)
        BMI_minimo = diferencias.min(axis=1)
        columna_minima = list(diferencias.idxmin(axis=1))
        
        if columna_minima[0] == "SD4neg":
            interpretacion = "Delgadez Severa, Alerta!! Consulte su pediatra"
        elif columna_minima[0] == "SD3neg":
            interpretacion= "Delgadez Severa consulte su pediatra"
        elif columna_minima[0] == "SD2neg":
            interpretacion= "Delgadez, consulte su pediatra"
        elif columna_minima[0] == "SD1neg" or columna_minima[0] == "SD0":
            interpretacion = "Adecuado"
        elif columna_minima[0] == "SD1":
            interpretacion= "Riesgo de sobrepeso, esté alerta!!"
        elif columna_minima[0] == "SD2":
            interpretacion= "Sobrepeso, consulte su pediatra!!"
        else: 
            interpretacion= "Obesidad, consulte su pediatra!!"

        #print(f"El Indice de Masa Coporal se encuentra es {interpretacion}")
        #return 'Para', nombre, 'El peso', peso_ingresado, 'kg, para la talla', talla_ingresada, 'cm, se encuentra con', interpretacion

fecha_nacimiento = datetime.strptime(fecha_ingresada, "%d/%m/%Y")
edad = relativedelta(datetime.now(), fecha_nacimiento)
edad_uso = edad.years * 12

analisis_BMI_mayores_5_años(dfniñas_mayor_6_años, edad_uso, (calcularBMI(peso_ingresado, talla_ingresada)))