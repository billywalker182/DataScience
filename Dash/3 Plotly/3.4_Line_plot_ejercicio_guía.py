#Importación de librerías
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

#Carga de datos
df_ventas = pd.read_csv(r'Ventas.csv',encoding = 'ISO-8859-1',delimiter=';')

#Definición de objeto de tipo lista "data": datos utilizados en el gráfico y el tipo de gráfico. Uso de diferentes trazas
trace0 = go.Scatter(x=df_ventas["Fecha"],
                    y=df_ventas["Total Venta Classic Cars"],
                    mode="lines",
                    name="Classic Cars")

trace1 = go.Scatter(x=df_ventas["Fecha"],
                    y=df_ventas["Total Venta Motorcycles"],
                    mode="lines",
                    name="MotorCycles")


data = [trace0, trace1]

#Definición de objeto "layout": diseño del gráfico como título, nombres de ejes,...
layout = go.Layout(title="SP500 Line Plot",
                    xaxis=dict(title="Fecha"),
                    yaxis=dict(title="Total Ventas"))

#Creación de objeto "Figure" de Plotly a partir de los objetos data y layout creados previamente
fig = go.Figure(data=data,layout=layout)
#Generación del plot a partir de la figura definida y nombre del fichero de salida HTML
pyo.plot(fig,filename="Ejercicio_Line_Plot.html")
