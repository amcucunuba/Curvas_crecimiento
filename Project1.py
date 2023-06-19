import pandas as pd
import numpy as np
import math
#Leer el archivo e importar en df
dfniñas = pd.read_excel("C:\\Users\\User\\Documents\\Ejercicio Python\\wfl-girls-zscore-expanded-table.xlsx")
dfniños = pd.read_excel("C:\\Users\\User\\Documents\\Ejercicio Python\\wfl-boys-zscore-expanded-table.xlsx")

#Solitar peso, talla y genero al usuario 
talla_ingresada = float(input("Ingrese la talla en cm:  "))
peso_ingresado = float(input("Ingrese el peso en kg:  "))
#género_ingresado = (input("Ingrese el genero Femenino (F) o Masculino (M): "))

#Extraer de la talla la parte decimal y la parte entera, para aproximar dentro de la serie de datos del df.
talla_parte_decimal, talla_parte_entera = math.modf(talla_ingresada)

#función que evalua la parte decimal diferente de 0.5, para buscar el dato más cercano
# Primero se multiplica y divide en 2
# la función round redondea un numero decimal al entero más cercano
# luego se concatena a la parte entera 
# Si es igual a 0.5, concatena a la parte entera.
if talla_parte_decimal != 0.5: 
    aprox = talla_parte_decimal * 2
    talla_parte_decimal_aprox = round(aprox) / 2
    talla_aproximada = talla_parte_decimal_aprox + talla_parte_entera
else: 
    talla_aproximada= talla_parte_entera + 0.5

#Filtro del df con la talla aproximada, me entrega la seride datos basado en 
# la fila correspondiente a la talla
filtro1= dfniñas[(dfniñas[0:] == talla_aproximada)]    
print(filtro1)
#lista de pesos del df friltrado 
encontrar_peso_lista = (filtro1.loc[:,['SD3neg','SD2neg', 'SD1neg', 'SD0','SD1', 'SD2','SD3','SD4']])

# determinar las difrencias de peso,para eso se resta el peso ingresado a cada uno de los pesos de la lista
#con la función abs se mantienen valores absolutos
# luego con la funcion .min devuelve el mínimo valor de la lista
# la funcion .idxmin me devuelve el nombre de la columna
diferencias = abs(encontrar_peso_lista - peso_ingresado)
peso_minimo = diferencias.min(axis=1)
columna_minima = list(diferencias.idxmin(axis=1))

#Esta función me devuelve la interpretación del nombre la columna.
#Es un evaluación de iguales
if columna_minima[0] == "SD3neg":
    interpretacion = "Desnutrición Aguda Severa, consulte su pediatra"
elif columna_minima[0] == "SD2neg":
    interpretacion= "Desnutrición Aguda Moderada, consulte su pediatra"
elif columna_minima[0] == "SD1neg":
    interpretacion = "Riesgo de desnutrición, consulte su pediatra"
elif columna_minima[0] == "SD0" or columna_minima[0] == "SD1":
    interpretacion= "Adecuado"
elif columna_minima[0] == "SD2":
    interpretacion= "Riesgo de sobrepeso, esté alerta!!"
elif columna_minima[0] == "SD3":
    interpretacion= "Sobrepeso, consulte su pediatra!!"
else: 
    interpretacion= "Obesidad, consulte su pediatra!!"



#Esta función le permite ver al usuario la interpretación en la curva de crecimiento.

if peso_ingresado :
    print(f"El peso {peso_ingresado}kg para la talla {talla_ingresada}cm, se encuentra con {interpretacion}")
else:
    print(f"No se encontró el peso {peso_ingresado} para la talla {talla_ingresada}ingresada en ninguna columna")


