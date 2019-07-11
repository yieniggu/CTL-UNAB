# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:12:58 2019

@author: Bastolo
"""

import pandas as pd

# Leemos la data
cuad_data = pd.read_csv("temporal_cuad_data_h.csv")
cuad_data.head()

# Se obtienen mediciones en Santiago, Las Condes y Providencia
cuad_data2 = cuad_data.loc[(cuad_data["Nombre_Comuna"] == "Santiago") |
        (cuad_data["Nombre_Comuna"] == "Las Condes") | (cuad_data["Nombre_Comuna"] == "Providencia")]

# Se obtienen mediciones entre 7 y 18 horas
cuad_data3 = cuad_data2.loc[(cuad_data2["Hora2"] >= 7) & (cuad_data2["Hora2"] <= 18)]

# Total de cuadrantes en las 3 comunas: 1638
len(cuad_data3["id_Cuadrante"].unique())

# Dia de la primera medicion
cuad_data3["year_day"].min()

# Dia de la ultima medicion
cuad_data3["year_day"].max()

cuad_data3.to_csv("stgo_provi_lcdes.csv", index=False)