import pandas as pd
import numpy as np
import math
from datetime import datetime
from dateutil.relativedelta import relativedelta
import plotly.graph_objects as go

#Calcular la edad del usurio y determinar que DF usar. 
#función para calcular la edad con la fecha de nacimiento que ingrese el usuario.
def edad_meses (fecha):
    fecha_nacimiento = datetime.strptime(fecha, "%d/%m/%Y")
    edad = relativedelta(datetime.now(), fecha_nacimiento)
#se multiplica por 12 (meses del año) porque los df estan con informacion en meses.
    edad_uso = edad.years * 12
    return edad_uso

# Esta funcion agrupa toda la información. Evalua inicialmente la edad y el género para evitar estrellarse.
# Luego con los datos entregados de genero y edad evalua cual es el df acorde a los valores ingresados
# Hace el analisis tomando talla, y peso
# Para el BMI se hace el calculo con el dato de peso y talla
# Por otro lado se ejecuta la grafica con las mismas variables 
def analis_antropometrico (genero, ed, talla, peso, nom):   
# Peso para la talla menores de 2 años    
    df_wfl_niñas_menor_2_años = pd.read_excel("wfl-girls-zscore-expanded-table-0-a-2-anios.xlsx")
    df_wfl_niños_menor_2_años = pd.read_excel("wfl-boys-zscore-expanded-table-0-a-2-anios.xlsx")   
# Cambiar el nombre de la columna de longitud a talla, como los demás df, solo
# para los df menores de 2 años.
    df_wfl_niñas_menor_2_años.rename( columns={"Length": "Height"}, inplace=True)
    df_wfl_niños_menor_2_años.rename( columns={"Length": "Height"}, inplace=True)
# Peso para la talla menores de 5 años
    df_wfh_niñas_entre_2_y_5_años = pd.read_excel("wfh-girls-zscore-2-a-5-anios.xlsx")
    df_wfh_niños_entre_2_y_5_años = pd.read_excel("wfh-boys-zscore-2-a-5-anios.xlsx")
# Peso para la edad de 0 a 5 años
    df_wfa_niñas_entre_0_y_5_años = pd.read_excel("wfa-girls-zscore-expanded-tables_0_a_5anios.xlsx")
    df_wfa_niños_entre_0_y_5_años = pd.read_excel("wfa-boys-zscore-expanded-tables_0_a_5_anios.xlsx")
# Cambio de unidad de medida en la edad, pasó de dias a meses 
# Cambio en el mombre de la columna    
    df_wfa_niñas_entre_0_y_5_años["Day"] = df_wfa_niñas_entre_0_y_5_años["Day"] / 30
    df_wfa_niñas_entre_0_y_5_años.rename( columns={"Day" : "Month"}, inplace= True)
    
    df_wfa_niños_entre_0_y_5_años["Day"] = df_wfa_niños_entre_0_y_5_años["Day"] / 30
    df_wfa_niños_entre_0_y_5_años.rename( columns={"Day" : "Month"}, inplace= True)

# Peso para la edad 5 a 10 años 
    df_wfa_niñas_entre_6_y_10_años = pd.read_excel("wfa-girls-z-who-2007-exp_5-a-10-anios.xlsx")
    df_wfa_niños_entre_6_y_10_años = pd.read_excel("wfa-boys-z-who-2007-exp_5-a-10-anios.xlsx")
# Talla para la edad 0 a 5 años 
    df_hfa_ninas_0_a_5_anios = pd.read_excel("hfa-girls-zscore-expanded-tables-0-a-5-anios.xlsx")
    df_hfa_ninos_0_a_5_anios = pd.read_excel("hfa-boys-zscore-expanded-tables-0-a-5-anios.xlsx")
# Cambio de unidad de medida en la edad, pasó de dias a meses 
# Cambio en el mombre de la columna    
    df_hfa_ninas_0_a_5_anios["Day"] = df_hfa_ninas_0_a_5_anios["Day"] / 30
    df_hfa_ninas_0_a_5_anios.rename( columns={"Day" : "Month"}, inplace= True)
    df_hfa_ninos_0_a_5_anios["Day"] = df_hfa_ninos_0_a_5_anios["Day"] / 30
    df_hfa_ninos_0_a_5_anios.rename( columns={"Day" : "Month"}, inplace= True)
# Talla para la edad 5 a 18 años
    df_hfa_ninas_5_a_18_anios = pd.read_excel("hfa-girls-z-who-2007-exp-5-a18-anios.xlsx")
    df_hfa_ninos_5_a_18_anios = pd.read_excel("hfa-boys-z-who-2007-exp-5-a-18anios.xlsx")
# BMI para la edad de 0 a 5 años 
    df_bmi_ninas_0_a_5_anios = pd.read_excel("bmifa-girls-zscore-expanded-tables_0a_5_anios.xlsx")
    df_bmi_ninos_0_a_5_anios = pd.read_excel("bmifa-boys-zscore-expanded-tables-0-5anios.xlsx")

# Cambio de unidad de medida en la edad, pasó de dias a meses 
# Cambio en el mombre de la columna    
    df_bmi_ninas_0_a_5_anios["Day"] = df_bmi_ninas_0_a_5_anios["Day"] / 30
    df_bmi_ninas_0_a_5_anios.rename( columns={"Day" : "Month"}, inplace= True)
    df_bmi_ninos_0_a_5_anios["Day"] = df_bmi_ninos_0_a_5_anios["Day"] / 30
    df_bmi_ninos_0_a_5_anios.rename( columns={"Day" : "Month"}, inplace= True)
# BMI para la edad de 5 a 18 años 
    df_bmi_niñas_mayor_6_años =  pd.read_excel("bmi-girls-z-who-2007-exp-5-a-18-anios.xlsx")
    df_bmi_niños_mayor_6_años =  pd.read_excel("bmi-boys-z-who-2007-exp-5-a18-anios.xlsx")    
    
# Evaluación de genero   
    if genero != "M" and genero != "F":
        print ("Verifique el género ingresado")
# Inicia el analisis de datos    
    elif genero == 'M' and ed <24:
        return (analisis_peso_talla_menores_5_años((df_wfl_niños_menor_2_años), talla, peso, nom), 
                grafico_crecimiento_1(df_wfl_niños_menor_2_años[talla], [peso],nom),
                analisis_crecimiento (df_hfa_ninos_0_a_5_anios, ed, talla, nom, 1),
                analisis_crecimiento (df_wfa_niños_entre_0_y_5_años, ed, peso, nom, 2),
                analisis_crecimiento (df_bmi_ninos_0_a_5_anios, ed, (calcularBMI(peso, talla)), nom, 3))
    elif genero == 'M'and ed > 24 and ed <59:
        return (analisis_peso_talla_menores_5_años(df_wfh_niños_entre_2_y_5_años, talla, peso, nom), 
                grafico_crecimiento_1(df_wfh_niños_entre_2_y_5_años, [talla],[peso], nom ),
                analisis_crecimiento (df_hfa_ninos_0_a_5_anios, ed, talla, nom, 1),
                analisis_crecimiento (df_wfa_niños_entre_0_y_5_años, ed, peso, nom, 2),
                analisis_crecimiento(df_bmi_ninos_0_a_5_anios, ed, (calcularBMI(peso, talla)), nom,3))
    elif genero == 'M'and  ed > 60 and ed < 215:
        return (analisis_crecimiento(df_bmi_niños_mayor_6_años, ed, (calcularBMI(peso, talla)), nom, 3),
                grafico_crecimiento2(df_bmi_niños_mayor_6_años,[ed],[(calcularBMI(peso, talla))], nom),
                analisis_crecimiento (df_hfa_ninos_5_a_18_anios, ed, talla, nom, 1),
                analisis_crecimiento (df_wfa_niños_entre_6_y_10_años, ed, peso, nom, 2))
    elif genero == 'F'and ed < 24:
        return (analisis_peso_talla_menores_5_años(df_wfl_niñas_menor_2_años, talla, peso, nom),
                grafico_crecimiento_1(df_wfl_niñas_menor_2_años,[talla], [peso], nom),
                analisis_crecimiento (df_hfa_ninas_0_a_5_anios, ed, talla, nom, 1),
                analisis_crecimiento (df_wfa_niñas_entre_0_y_5_años, ed, peso, nom, 2),
                analisis_crecimiento(df_bmi_ninas_0_a_5_anios, ed, (calcularBMI(peso, talla)), nom, 3))
    elif genero == 'F'and ed > 24 and ed <59:
        return (analisis_peso_talla_menores_5_años(df_wfh_niñas_entre_2_y_5_años, talla, peso, nom),
                grafico_crecimiento_1(df_wfh_niñas_entre_2_y_5_años, [talla], [peso], nom),
                analisis_crecimiento (df_hfa_ninas_0_a_5_anios, ed, talla, nom, 1),
                analisis_crecimiento (df_wfa_niñas_entre_0_y_5_años, ed, peso, nom, 2),
                analisis_crecimiento(df_bmi_ninas_0_a_5_anios, ed, (calcularBMI(peso, talla)), nom, 3))
    elif genero == 'F'and  ed > 60 and ed < 215:
        return (analisis_crecimiento(df_bmi_niñas_mayor_6_años, ed, (calcularBMI(peso, talla)), nom, 3),
               grafico_crecimiento2(df_bmi_niñas_mayor_6_años, [ed], [(calcularBMI(peso, talla))],nom),
               analisis_crecimiento (df_wfa_niñas_entre_6_y_10_años, ed, peso, nom, 2),
               analisis_crecimiento (df_hfa_ninas_5_a_18_anios, ed, talla, nom, 1))


# Definir la funcion de analisis de talla para menores de 5 años, 
# dando el df, talla y peso.
# La primer condición a evaluar es la talla, para evitar que el programa se estelle,

def analisis_peso_talla_menores_5_años(df, cm, peso, usuario):
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
            interpretacion = "Desnutrición Aguda Moderada, Alerta!! Consulte su pediatra"
        elif columna_minima[0] == "SD2neg":
            interpretacion = "Desnutrición Aguda Moderada, Alerta!! Consulte su pediatra"
        elif columna_minima[0] == "SD1neg":
            interpretacion = "Riesgo de desnutrición. Consulte su pediatra"
        elif columna_minima[0] == "SD0" or columna_minima[0] == "SD1":
            interpretacion = "Adecuado peso para la talla"
        elif columna_minima[0] == "SD2":
            interpretacion = "Riesgo de sobrepeso, esté alerta!!"
        elif columna_minima[0] == "SD3":
            interpretacion = "Sobrepeso. Consulte su pediatra!!"
        else: 
            interpretacion =  "Obesidad. Consulte su pediatra!!"
        print (usuario, interpretacion)


#Para los niños se calcula el indice de masa corporal (BMI) a partir del peso y la talla ingresada
#el primer paso de la función es calcular el BMI, porque es necesario para evaluar el crecimiento.

def calcularBMI(p, a):
    return p / ((a * 0.01) * (a * 0.01))

#Antes de hacer el analisis, se verifica la edad 
def analisis_crecimiento (df, edad, indicador, usuario, tipo_analisis):
    abc = 0
    if tipo_analisis == 1:
        abc = "Talla" 
    elif tipo_analisis == 2:
        abc = "Peso"
    else:
        abc = "IMC"


    if  edad > 215:
        print("Verifique los datos ingresados, fecha de nacimiento")
#filtro del df deacuerdo a la EDAD ingresa por el usuario, iterando la serie lista del indicador antropometrico
# Puede ser, talla, peso o BMI
# La función busca para la edad ingresada, el BMI más cercano en la lista de la serie de datos 
# y devuelve el nombre de la columna, que luego es interpretada de acuerdo a la ley 2121 de 2010.
    else:      
        filtro1= df[(df["Month"] == edad)]  
        encontrar_indicador_lista = (filtro1.loc[:,['SD4neg','SD3neg','SD2neg', 'SD1neg', 'SD0','SD1', 'SD2','SD3','SD4']])
        diferencias = abs(encontrar_indicador_lista - indicador)
        BMI_minimo = diferencias.min(axis=1)
        columna_minima = list(diferencias.idxmin(axis=1))
        
        if columna_minima[0] == "SD4neg" or columna_minima[0] == "SD3neg" :
            interpretacion2 = "Alerta!! Consulte su pediatra"
        elif columna_minima[0] == "SD2neg":
            interpretacion2 = "Riesgo !. Consulte su pediatra"
        elif columna_minima[0] == "SD1neg" or columna_minima[0] == "SD0":
            interpretacion2 = "Adecuado para la edad"
        elif columna_minima[0] == "SD1":
            interpretacion2 = "Riesgo, esté alerta!!"
        else: 
            interpretacion2 = "Alerta Consulte su pediatra!!"
        
        print (f" {usuario} tiene {abc} {interpretacion2}")


#funcion para la grafica menores de 5 años
def grafico_crecimiento_1 (df, talla, peso, usuario):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Height"], y= df["SD3neg"], name= "SD3neg", hoverinfo='none',
                      line=dict(color='red', width=2)))
    fig.add_trace(go.Scatter(x=df["Height"], y= df["SD2neg"], name= "SD2neg", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='red', width=2) ))
    fig.add_trace(go.Scatter(x=df["Height"], y= df["SD1neg"], name= "SD1neg", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='yellow', width=2)))
    fig.add_trace(go.Scatter(x=df["Height"], y= df["SD0"], name= "SD0", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='green', width=2)))
    fig.add_trace(go.Scatter(x=df["Height"], y= df["SD1"], name= "SD1",  fill= 'tonexty', hoverinfo='none',
                      line=dict(color='green', width=2)))
    fig.add_trace(go.Scatter(x=df["Height"], y= df["SD2"], name= "SD2", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='yellow', width=2)))
    fig.add_trace(go.Scatter(x=df["Height"], y= df["SD3"], name= "SD3", fill= 'tonexty', hoverinfo='none',
                      line=dict(color='red', width=2,) ))
    fig.add_trace(go.Scatter(fillpattern= dict(bgcolor= 'white')))
    fig.update_layout(title='Curva de Crecimiento OMS',
                   xaxis_title='Talla en centimetros (cm)',
                   yaxis_title='Peso en kilogramos (kg)',
                   legend_title_text= 'Desviaciones Estándar')
    fig.add_trace(go.Scatter(x= talla, y= peso, name= usuario, mode='lines+markers', line= dict(color= 'black'),
                              hovertemplate= '<br>Edad: %{x} meses <br>Peso: %{y} kg'))
    return fig.show() 

#funcion para la grafica mayores de 5 años
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

