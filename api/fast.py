import sys
import os
import pandas as pd
from fastapi import FastAPI
from datetime import datetime
from dateutil.relativedelta import relativedelta
from fastapi.middleware.cors import CORSMiddleware
from funcion import edad_meses, analis_antropometrico

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = FastAPI()

@app.get("/predict")
def predict(nombre,
    fecha_ingresada,
    genero_ingresado,
    talla_ingresada,
    peso_ingresado,
    ):

    fecha_nacimiento = datetime.strptime(fecha_ingresada, "%d/%m/%Y")
    edad = relativedelta(datetime.now(), fecha_ingresada)
    #se multiplica por 12 (meses del año) porque los df estan con informacion en meses.
    edad_uso = edad.months

    analisis = analis_antropometrico (genero_ingresado, edad_uso, talla_ingresada, peso_ingresado, nombre)
        
    return analisis

@app.get("/")
def root():
    return {
    'Hello': 'Hello'
    }