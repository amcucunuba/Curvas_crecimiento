import pandas as pd
import numpy as np
import math
from datetime import datetime
from dateutil.relativedelta import relativedelta

#Leer el archivo e importar en df
dfniñas_menor_2_años = pd.read_excel("C:\\Users\\User\\Documents\\Ejercicio Python\\wfl-girls-zscore-expanded-table.xlsx")
dfniños_menor_2_años = pd.read_excel("C:\\Users\\User\\Documents\\Ejercicio Python\\wfl-boys-zscore-expanded-table.xlsx")   

#Cambiar el nombre de la columna de longitud a talla, como los demás df, solo
# para los df menores de 2 años.
dfniñas_menor_2_años.rename( columns={"Length": "Height"}, inplace=True)
dfniños_menor_2_años.rename( columns={"Length": "Height"}, inplace=True)

dfniñas_entre_2_y_5_años = pd.read_excel("C:\\Users\\User\\Documents\\Ejercicio Python\\wfh-girls-zscore-2-a-5-anios.xlsx")
dfniños_entre_2_y_5_años = pd.read_excel("C:\\Users\\User\\Documents\\Ejercicio Python\\wfh-boys-zscore-2-a-5-anios.xlsx")

dfniñas_mayor_6_años =  pd.read_excel("C:\\Users\\User\\Documents\\Ejercicio Python\\bmi-girls-z-who-2007-exp.xlsx")
dfniños_mayor_6_años =  pd.read_excel("C:\\Users\\User\\Documents\\Ejercicio Python\\bmi-boys-z-who-2007-exp.xlsx")

#Datos que el usuario debe ingresar
nombre = input("Ingrese el nombre de su bebé:  ")
fecha_ingresada = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
genero_ingresado = input("Ingrese el género, Femenino  F o Masculino M:  ")
talla_ingresada = float(input("Ingrese la talla en cm:  "))
peso_ingresado = float(input("Ingrese el peso en kg:  "))

#Definir la funcion de analisis de talla para menores de 5 años, 
# dando el df, talla y peso.
# La primer condición a evaluar es la talla, para evitar que el programa se estelle,


def analisis_talla_menores_5_años(df, cm, peso):
    if  cm < 45 or cm >120:
        print("Verifique los datos ingresados, fecha de nacimiento, talla en centimetros")
#filtro del df deacuerdo a la talla ingresada por el usuario, iterando la serie lista de pesos
    else:      
        filtro1= df[(df["Height"] == cm)]   
        encontrar_peso_lista = (filtro1.loc[:,['SD4neg','SD3neg','SD2neg', 'SD1neg', 'SD0','SD1', 'SD2','SD3','SD4']])
#Encontrar la diferencia de peso, entre el peso ingresado y el peso de la lista
#para encontrar el valor más cercano y retorna el nombre de la columna o SD
        diferencias = abs(encontrar_peso_lista - peso)
        peso_minimo = diferencias.min(axis=1)
        columna_minima = list(diferencias.idxmin(axis=1))
#Interpretación de la columna SD 
#La función busca para la talla ingresada, el peso más cercano en la lista de la serie de datos 
# y devuelve el nombre de la columna, que luego es interpretada de acuerdo a la ley 2121 de 2010.
        if columna_minima[0] == "SD4neg":
            interpretacion = "Desnutrición Global Severa, Alerta!! Consulte su pediatra"
        elif columna_minima[0] == "SD3neg":
            interpretacion = "Desnutrición Aguda Moderada, consulte su pediatra"
        elif columna_minima[0] == "SD2neg":
            interpretacion = "Desnutrición Aguda Moderada, consulte su pediatra"
        elif columna_minima[0] == "SD1neg":
            interpretacion = "Riesgo de desnutrición, consulte su pediatra"
        elif columna_minima[0] == "SD0" or columna_minima[0] == "SD1":
            interpretacion = "Adecuado peso para la talla"
        elif columna_minima[0] == "SD2":
            interpretacion = "Riesgo de sobrepeso, esté alerta!!"
        elif columna_minima[0] == "SD3":
            interpretacion = "Sobrepeso, consulte su pediatra!!"
        else: 
            interpretacion =  "Obesidad, consulte su pediatra!!"
        print (interpretacion)

#Para los niños mayores de 5 años, se calcula el indice de masa corporal (BMI) a partir del peso y la talla ingresada
#el primer paso de la función es calcular el BMI, porque es necesario para evaluar el crecimiento.

def calcularBMI(p, a):
    return p / (a * a)

#Antes de hacer el analisis, se verifica la edad 
def analisis_BMI_mayores_5_años(df, edad, BMI):
    if  edad < 60 or edad > 215:
        print("Verifique los datos ingresados, fecha de nacimiento")
#filtro del df deacuerdo a la EDAD ingresa por el usuario, iterando la serie lista de BMI
#La función busca para la edad ingresada, el BMI más cercano en la lista de la serie de datos 
# y devuelve el nombre de la columna, que luego es interpretada de acuerdo a la ley 2121 de 2010.
    else:      
        filtro1= df[(df["Month"] == edad)]  
        encontrar_BMI_lista = (filtro1.loc[:,['SD4neg','SD3neg','SD2neg', 'SD1neg', 'SD0','SD1', 'SD2','SD3','SD4']])
        diferencias = abs(encontrar_BMI_lista - BMI)
        BMI_minimo = diferencias.min(axis=1)
        columna_minima = list(diferencias.idxmin(axis=1))
        
        if columna_minima[0] == "SD4neg":
            interpretacion2 = "Delgadez Severa, Alerta!! Consulte su pediatra"
        elif columna_minima[0] == "SD3neg":
            interpretacion2 = "Delgadez Severa consulte su pediatra"
        elif columna_minima[0] == "SD2neg":
            interpretacion2 = "Delgadez, consulte su pediatra"
        elif columna_minima[0] == "SD1neg" or columna_minima[0] == "SD0":
            interpretacion2 = "Adecuado"
        elif columna_minima[0] == "SD1":
            interpretacion2 = "Riesgo de sobrepeso, esté alerta!!"
        elif columna_minima[0] == "SD2":
            interpretacion2 = "Sobrepeso, consulte su pediatra!!"
        else: 
            interpretacion2 = "Obesidad, consulte su pediatra!!"
        
        print (interpretacion2)

#Calcular la edad del bebé y determinar que DF usar. 
#función para calcular la edad con base en la fecha de nacimiento que ingrese el usuario.
fecha_nacimiento = datetime.strptime(fecha_ingresada, "%d/%m/%Y")
edad = relativedelta(datetime.now(), fecha_nacimiento)
#se multiplica por 12 (meses del año) porque los df estan con informacion en meses.
edad_uso = edad.years * 12


#la funcion que agrupa toda la información, evalua inicialmente la edad y el género para evitar estrellarse.

def analis_edad (genero, ed):   
    if genero != "M" and "F" and ed > 216:
        print ("Verifique el género ingresado y/o la fecha de nacimiento")
    elif genero == 'M' and ed <24:
        return (analisis_talla_menores_5_años(dfniños_menor_2_años, talla_ingresada, peso_ingresado))
    elif genero == 'M'and ed > 24 and ed <59:
        return (analisis_talla_menores_5_años(dfniños_entre_2_y_5_años, talla_ingresada, peso_ingresado))
    elif genero == 'M'and  ed > 60 and ed < 215:
        return (analisis_BMI_mayores_5_años(dfniños_mayor_6_años, edad_uso, (calcularBMI(peso_ingresado, talla_ingresada))))
    elif genero == 'F'and ed < 24:
        return (analisis_talla_menores_5_años(dfniñas_menor_2_años, talla_ingresada, peso_ingresado))
    elif genero == 'F'and ed > 24 and ed <59:
        return (analisis_talla_menores_5_años(dfniñas_entre_2_y_5_años, talla_ingresada, peso_ingresado))
    elif genero == 'F'and  ed > 60 and ed < 215:
        return(analisis_BMI_mayores_5_años(dfniñas_mayor_6_años, edad_uso, (calcularBMI(peso_ingresado, talla_ingresada))))
        

analis_edad(genero_ingresado, edad_uso)
