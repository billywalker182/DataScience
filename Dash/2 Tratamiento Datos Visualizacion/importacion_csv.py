import pandas as pd 

df = pd.read_csv("Info_pais.csv",encoding='ISO-8859-1',delimiter=";")

df_filtrado = df[df["Poblacion"]>150000000]

print(df_filtrado[["País","Poblacion"]])