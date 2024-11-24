import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functions.funcion import edad_meses, analis_antropometrico

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods
#     allow_headers=["*"],  # Allows all headers
# )

@app.get("/predict")
def predict(nombre,
    fecha_ingresada,
    genero_ingresado,
    talla_ingresada,
    peso_ingresado,
    ):

    # analisis = analis_antropometrico(genero_ingresado, 
    #                                  edad_meses(fecha_ingresada), 
    #                                  talla_ingresada, 
    #                                  peso_ingresado, 
    #                                  nombre)    

    return peso_ingresado

@app.get("/")
def root():
    return {
    'greeting': 'Hello'
    }