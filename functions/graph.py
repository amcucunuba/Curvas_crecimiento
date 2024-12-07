
import pandas as pd
import numpy as np
import math
from datetime import datetime
from dateutil.relativedelta import relativedelta
import plotly.graph_objects as go

df_bmi_ninas_0_a_5_anios = pd.read_excel("bmifa-boys-zscore-expanded-tables-0-5anios.xlsx")
df_wfa_niñas_entre_0_y_5_años = pd.read_excel("wfa-girls-zscore-expanded-tables_0_a_5anios.xlsx")



def grafico_crecimiento2 (df, edad, IMC, usuario):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Month"], y= df["SD3neg"], name= "SD3neg", hoverinfo='none',
                      line=dict(color='red', width=2)))
    fig.add_trace(go.Scatter(x=df["Month"], y= df["SD2neg"], name= "SD2neg", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='red', width=2) ))
    fig.add_trace(go.Scatter(x=df["Month"], y= df["SD1neg"], name= "SD1neg", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='yellow', width=2)))
    fig.add_trace(go.Scatter(x=df["Month"], y= df["SD0"], name= "SD0", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='green', width=2)))
    fig.add_trace(go.Scatter(x=df["Month"], y= df["SD1"], name= "SD1",  fill= 'tonexty', hoverinfo='none',
                      line=dict(color='green', width=2)))
    fig.add_trace(go.Scatter(x=df["Month"], y= df["SD2"], name= "SD2", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='yellow', width=2)))
    fig.add_trace(go.Scatter(x=df["Month"], y= df["SD3"], name= "SD3", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='red', width=2,) ))
    fig.add_trace(go.Scatter(fillpattern= dict(bgcolor= 'white')))
    fig.update_layout(title='Curva de Crecimiento OMS',
                   xaxis_title='Edad en meses',
                   yaxis_title='Indice de Masa Corporal',
                   legend_title_text= 'Desviaciones Estándar')
    fig.add_trace(go.Scatter(x= edad, y= IMC, name= usuario, mode='lines+markers', line= dict(color= 'black'), 
                             hovertemplate= '<br>Edad: %{x} meses <br>IMC: %{y}'))
    return fig.show()

grafico_crecimiento2 (df_bmi_ninas_0_a_5_anios, [40], [14], "Ana" )







def analisis_peso_edad (df, edad, BMI, usuario):
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
            interpretacion2 = "Delgadez Severa. Consulte su pediatra"
        elif columna_minima[0] == "SD2neg":
            interpretacion2 = "Delgadez. Consulte su pediatra"
        elif columna_minima[0] == "SD1neg" or columna_minima[0] == "SD0":
            interpretacion2 = "Adecuado IMC para la edad"
        elif columna_minima[0] == "SD1":
            interpretacion2 = "Riesgo de sobrepeso, esté alerta!!"
        elif columna_minima[0] == "SD2":
            interpretacion2 = "Sobrepeso. Consulte su pediatra!!"
        else: 
            interpretacion2 = "Obesidad. Consulte su pediatra!!"
        
        print (usuario, interpretacion2)
