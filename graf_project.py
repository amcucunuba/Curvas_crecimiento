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

fig = go.Figure()

fig.add_trace(go.Line(x=dfniñas_entre_2_y_5_años["Height"], y= dfniñas_entre_2_y_5_años["SD3neg"], name= "SD3neg",
                      line=dict(color='red', width=2, dash= 'dash')))

fig.add_trace(go.Line(x=dfniñas_entre_2_y_5_años["Height"], y= dfniñas_entre_2_y_5_años["SD2neg"], name= "SD2neg",
                      line=dict(color='red', width=2) ))

fig.add_trace(go.Line(x=dfniñas_entre_2_y_5_años["Height"], y= dfniñas_entre_2_y_5_años["SD1neg"], name= "SD1neg",
                      line=dict(color='yellow', width=2)))

fig.add_trace(go.Line(x=dfniñas_entre_2_y_5_años["Height"], y= dfniñas_entre_2_y_5_años["SD0"], name= "SD0",
                      line=dict(color='green', width=2)))

fig.add_trace(go.Line(x=dfniñas_entre_2_y_5_años["Height"], y= dfniñas_entre_2_y_5_años["SD1"], name= "SD1",
                      line=dict(color='yellow', width=2)))

fig.add_trace(go.Line(x=dfniñas_entre_2_y_5_años["Height"], y= dfniñas_entre_2_y_5_años["SD2"], name= "SD2",
                      line=dict(color='red', width=2)))

fig.add_trace(go.Line(x=dfniñas_entre_2_y_5_años["Height"], y= dfniñas_entre_2_y_5_años["SD3"], name= "SD3",
                      line=dict(color='red', width=2, dash= 'dash') ))
fig.add_trace(go.Scatter(x= [90, 93,97], y= [11, 13, 12], name= "Usuario", mode='lines+markers', line= dict(color= 'black', hoverinfo='skip') ))

fig.add_trace(go.Scatter(fillpattern= dict(bgcolor= 'white')))
#fig.add_trace(go.Scatter(x= [95], y= [15], name= "Usuario", marker= dict(color= 'green', size=[8]), line= dict(color=None)))
fig.update_layout(title='Curva de Crecimiento OMS',
                   xaxis_title='Edad en meses',
                   yaxis_title='Peso en kg',
                   legend_title_text= 'Desviaciones Estándar')

fig.show()