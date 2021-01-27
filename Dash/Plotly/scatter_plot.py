import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df_iris = pd.read_csv(r"iris_dataset.csv",encoding="ISO-8859-1",delimiter=",")

data1 = [go.Scatter(x = df_iris["longitud_sépalo"],
                    y = df_iris["anchura_sépalo"],
                    mode = "markers"
)]

layout1 = go.Layout(title = "Iris Scatter Plot",
                    xaxis = dict(title = "Longitud Sépalo"),
                    yaxis = dict(title = "Anchura Sépalo")
)

fig = go.Figure(data=data1,layout=layout1)

pyo.plot(fig,filename="plot_iris.html")