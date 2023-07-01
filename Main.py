import pandas as pd
import numpy as np
import math
from datetime import datetime
from dateutil.relativedelta import relativedelta
from Funcion import analis_crecimiento
from Funcion import edad_meses



#Datos que el usuario debe ingresar
nombre = input("Ingrese el nombre de su bebé:  ")
fecha_ingresada = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
genero_ingresado = input("Ingrese el género, Femenino  F o Masculino M:  ")
talla_ingresada = float(input("Ingrese la talla en cm:  "))
peso_ingresado = float(input("Ingrese el peso en kg:  "))


analis_crecimiento (genero_ingresado, edad_meses(fecha_ingresada), talla_ingresada, peso_ingresado, nombre)    
