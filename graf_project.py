import pandas as pd
import numpy as np
import math
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

#Leer el archivo e importar en df
dfniñas_menor_2_años = pd.read_excel("C:\\Users\\User\\Documents\\Ejercicio Python\\wfl-girls-zscore-expanded-table.xlsx")
dfniños_menor_2_años = pd.read_excel("C:\\Users\\User\\Documents\\Ejercicio Python\\wfl-boys-zscore-expanded-table.xlsx")   

dfniñas_menor_2_años.rename( columns={"Length": "Height"}, inplace=True)
dfniños_menor_2_años.rename( columns={"Length": "Height"}, inplace=True)
#print(dfniñas_menor_2_años.columns)

dfniñas_entre_2_y_5_años = pd.read_excel("C:\\Users\\User\\Documents\\Ejercicio Python\\wfh-girls-zscore-2-a-5-anios.xlsx")
dfniños_entre_2_y_5_años = pd.read_excel("C:\\Users\\User\\Documents\\Ejercicio Python\\wfh-boys-zscore-2-a-5-anios.xlsx")
#print(dfniñas_entre_2_y_5_años.columns)

dfniñas_mayor_6_años =  pd.read_excel("C:\\Users\\User\\Documents\\Ejercicio Python\\bmi-girls-z-who-2007-exp.xlsx")
dfniños_mayor_6_años =  pd.read_excel("C:\\Users\\User\\Documents\\Ejercicio Python\\bmi-boys-z-who-2007-exp.xlsx")


#plt.stackplot(dfniñas_entre_2_y_5_años["Height"], dfniñas_entre_2_y_5_años["SD4neg"], dfniñas_entre_2_y_5_años["SD1neg"],
 #             dfniñas_entre_2_y_5_años["SD0"], dfniñas_entre_2_y_5_años["SD1"], dfniñas_entre_2_y_5_años["SD2"],
  #             colors= ("red", "yellow", "green", "yellow"))
#plt.legend(["SD2neg","SD1neg","SD0","SD1","SD2",])

#plt.show()

#fig = px.line (dfniñas_entre_2_y_5_años, x= "Height", y= "SD0", )
#fig.show()


def grafico_crecimiento (df, peso, talla):
    fig = go.Figure()
    fig.add_trace(go.Line(x=df["Height"], y= df["SD3neg"], name= "SD3neg", hoverinfo='none',
                      line=dict(color='red', width=2)))
    fig.add_trace(go.Line(x=df["Height"], y= df["SD2neg"], name= "SD2neg", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='red', width=2) ))
    fig.add_trace(go.Line(x=df["Height"], y= df["SD1neg"], name= "SD1neg", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='yellow', width=2)))
    fig.add_trace(go.Line(x=df["Height"], y= df["SD0"], name= "SD0", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='green', width=2)))
    fig.add_trace(go.Line(x=df["Height"], y= df["SD1"], name= "SD1",  fill= 'tonexty', hoverinfo='none',
                      line=dict(color='green', width=2)))
    fig.add_trace(go.Line(x=df["Height"], y= df["SD2"], name= "SD2", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='yellow', width=2)))
    fig.add_trace(go.Line(x=df["Height"], y= df["SD3"], name= "SD3", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='red', width=2,) ))
    fig.add_trace(go.Scatter(fillpattern= dict(bgcolor= 'white')))
    fig.update_layout(title='Curva de Crecimiento OMS',
                   xaxis_title='Talla en cm',
                   yaxis_title='Peso en kg',
                   legend_title_text= 'Desviaciones Estándar')
    fig.add_trace(go.Scatter(x= talla, y= peso, name= "Usuario", mode='lines+markers', line= dict(color= 'black') ))

    return fig.show()
#fig.show()

analisis1= grafico_crecimiento (dfniñas_entre_2_y_5_años, [14], [110])  
print (analisis1)
#def analisis_BMI_mayores_5_años(df, edad, BMI)