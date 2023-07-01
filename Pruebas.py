
import pandas as pd
import numpy as np
import math
from datetime import datetime
from dateutil.relativedelta import relativedelta
import plotly.graph_objects as go

df_bmi_ninas_0_a_5_anios = pd.read_excel("bmifa-boys-zscore-expanded-tables-0-5anios.xlsx")

def grafico_crecimiento2 (df, edad, IMC, usuario):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Day"], y= df["SD3neg"], name= "SD3neg", hoverinfo='none',
                      line=dict(color='red', width=2)))
    fig.add_trace(go.Scatter(x=df["Day"], y= df["SD2neg"], name= "SD2neg", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='red', width=2) ))
    fig.add_trace(go.Scatter(x=df["Day"], y= df["SD1neg"], name= "SD1neg", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='yellow', width=2)))
    fig.add_trace(go.Scatter(x=df["Day"], y= df["SD0"], name= "SD0", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='green', width=2)))
    fig.add_trace(go.Scatter(x=df["Day"], y= df["SD1"], name= "SD1",  fill= 'tonexty', hoverinfo='none',
                      line=dict(color='green', width=2)))
    fig.add_trace(go.Scatter(x=df["Day"], y= df["SD2"], name= "SD2", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='yellow', width=2)))
    fig.add_trace(go.Scatter(x=df["Day"], y= df["SD3"], name= "SD3", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='red', width=2,) ))
    fig.add_trace(go.Scatter(fillpattern= dict(bgcolor= 'white')))
    fig.update_layout(title='Curva de Crecimiento OMS',
                   xaxis_title='Edad en meses',
                   yaxis_title='Indice de Masa Corporal',
                   legend_title_text= 'Desviaciones Estándar')
    fig.add_trace(go.Scatter(x= edad, y= IMC, name= usuario, mode='lines+markers', line= dict(color= 'black'), 
                             hovertemplate= '<br>Edad: %{x} meses <br>IMC: %{y}'))
    return fig.show()

grafico_crecimiento2 (df_bmi_ninas_0_a_5_anios, [3 *360], [14], "Ana")
