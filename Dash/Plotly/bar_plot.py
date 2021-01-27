#Importación de librerías
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

#Carga de datos
df_med = pd.read_excel(r'Medallas_olímpicas.xlsx')

#Ordenar descendentemente por la columna total
df_med = df_med.sort_values(by="Total",ascending=False)

#Definición de objeto de tipo lista "data" con 1 única traza basada en el total de medallas
#data = [go.Bar(x=df_med["País"],
                #y=df_med["Total"])]

#Definición de objeto de tipo lista "data" con 3 trazas, 1 para cada tipo de medallas
trace0 = go.Bar(x=df_med["País"],
                y=df_med["Oro"],
                name = "Oro",
                marker={"color":"#FFD700"})

trace1 = go.Bar(x=df_med["País"],
                y=df_med["Plata"],
                name = "Plata",
                marker={"color":"#C0C0C0"})

trace2 = go.Bar(x=df_med["País"],
                y=df_med["Bronce"],
                name = "Bronce",
                marker={"color":"#CD7F32"})

data = [trace0,trace1,trace2]


layout = go.Layout(title="Medalllas olimpicas por país",
                    xaxis=dict(title="País"),
                    yaxis=dict(title="Total de Medallas"),
                    barmode="stack")

#Creación de objeto "Figure" de plotly a partir de los objetos data y layout creados previamente
fig = go.Figure(data=data,layout=layout)
#Generación de plot a partir de la figura definida y nombre del fichero de salida HTML
pyo.plot(fig,filename="Bar_Plot.html")

