import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df_sp500 = pd.read_csv(r"SP500_data_.csv",encoding="ISO-8859-1",delimiter=",")

traza1 = go.Scatter(x=df_sp500["Date"],
                    y=df_sp500["Close"],
                    mode="lines+markers",
                    name="Cierre")

traza2 = go.Scatter(x=df_sp500["Date"],
                    y=df_sp500["Open"],
                    mode="lines+markers",
                    name="Apertura")

layout = go.Layout(title="SP500 Line Plot",
                    xaxis=dict(title="Fecha"),
                    yaxis=dict(title="SP500 valor"))

data = [traza1,traza2]

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig,filename="Line_plot.html")