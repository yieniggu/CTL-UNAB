# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 13:25:53 2019

@author: Bastolo
"""

import pandas as pd

dataset = pd.read_csv("temporal_cuad_data_30.csv")

dataset.dtypes
dataset["Fecha"] = pd.to_datetime(dataset["Fecha"])

dataset["Fecha"].dtypes

min_date = min(dataset["Fecha"])
max_date = max(dataset["Fecha"])

rango = max_date - min_date

n_cuad = len(dataset["id_Cuadrante"].unique())
n_arc = len(dataset["id_Arco"].unique())

min_dataset = dataset.loc[(dataset["Nombre_Comuna"] == "Santiago") | (dataset["Nombre_Comuna"] == "Providencia") | (dataset["Nombre_Comuna"] == "Las Condes")]

n_cuad_min = len(min_dataset["id_Cuadrante"].unique())

print("hello: ", min_date)

rango_int = rango.days

total_data = n_cuad*344*96

dataset.shape[0]

# ========================================================================================================

dataset2 = dataset.iloc[:, :14]
dataset2.Fecha = pd.to_datetime(dataset2.Fecha)
dataset2.dtypes
dataset2.columns

dataset3 = dataset2[['id_Cuadrante', 'Velocidad_Promedio', "year_week", "week_day", "Nombre_Comuna", 'year_day', 'Hora2']]
dataset3.columns

medias = dataset3.groupby(["id_Cuadrante", "year_day", "year_week","week_day", "Nombre_Comuna", "Hora2"])["Velocidad_Promedio"].mean()
medias2 = pd.DataFrame(medias.reset_index())

medias2.to_csv("temporal_cuad_data_h.csv", index=False)