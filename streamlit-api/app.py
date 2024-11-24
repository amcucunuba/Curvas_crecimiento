import streamlit as st
import datetime
import requests
import pandas as pd
#from Main import analis_antropometrico
from funcion import edad_meses, analis_antropometrico

st.markdown("""
    # Baby Growth Chart Calculator
    ## The first five years
""")

st.text("""Fill out your baby's details""")

with st.form('growth'):

    nombre = st.text_input("Enter the baby’s name")
    fecha_ingresada = st.date_input("Birth day", format="DD/MM/YYYY")
    genero_ingresado = st.selectbox("It's a girl or a boy? ", ("F", "M"))
    talla_ingresada = st.number_input("Heigth in cm:  ", min_value=40.0, step=float(0.1))
    talla_ingresada
    peso_ingresado = st.number_input("Weigth in kilograms  ", min_value=2.0,  step=float(0.1))
    peso_ingresado

    growth = st.form_submit_button("Track your baby's growth")

st.text("La edad en meses es", (edad_meses(fecha_ingresada)))
analisis = analis_antropometrico(genero_ingresado, edad_meses(fecha_ingresada), talla_ingresada, peso_ingresado, nombre)    
