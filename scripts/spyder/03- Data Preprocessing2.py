# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 01:13:30 2019

@author: Bastolo
"""

import os
import pandas as pd
import numpy as np

# Leemos la data
cuad_data = pd.read_csv(os.getcwd() + "/historic data/cuad_data.csv", delimiter=";", ignore_index=True)

# Transformamos hora y fecha a datetime
cuad_data["Fecha"] = pd.to_datetime(cuad_data["Fecha"])
cuad_data["Hora"] = pd.to_datetime(cuad_data["Hora"])
cuad_data.dtypes

# Ordenamos por cuadrante y fecha
sorted_cuad_data = cuad_data.sort_values(by=["id_Cuadrante", "Fecha"])

sorted_cuad_data.dtypes
sorted_cuad_data.head()

# Añadimos las variables
sorted_cuad_data["Hora2"] = sorted_cuad_data["Hora"].dt.hour
sorted_cuad_data["Minuto"] = sorted_cuad_data["Hora"].dt.minute

# Guardamos
sorted_cuad_data.to_csv(os.getcwd() + "/historic data/cuad_data2.csv", index=False, sep=";")

# Leemos
sorted_cuad_data = pd.read_csv(os.getcwd() + "/historic data/cuad_data2.csv", delimiter = ";")

def add_velocities(data):
    #values = []
    values = pd.DataFrame()
    for index, row in data.iterrows():
        cuad, day, hour, minute = row.id_Cuadrante, row.year_day, row.Hora2, row.Minuto
        
        # Se obtienen las tuplas que tengan informacion del mismo cuadrante y de dias anteriores (a lo mas 30 dias)
        local_values = data.loc[(data["id_Cuadrante"] == cuad) & (day - data["year_day"] <= 30) & (day - data["year_day"] >= 0)]
        
        # Se elimina la tupla en estudio, asi como aquellas que se midieron en el mismo instante (hora y minuto)
        local_values = local_values.loc[(local_values["year_day"] != day) | ((local_values["year_day"] == day) & (local_values["Hora2"] == hour) & (local_values["Minuto"] < minute))]
        
        # Agrupamos por dia y obtenemos la media de las observaciones
        local_values = local_values.groupby("year_day")["Velocidad_Promedio"].mean().tolist()
        
        # Reordenamos para tener temporalidad bien definida
        local_values.reverse()
        
        # Caso 1: solo existe una medicion para ese cuadrante
        if(len(local_values) == 0):
            mean = row.Velocidad_Promedio # Se rellena con el valor de la unica medicion observada
        # Caso 2: No existen suficientes mediciones previas en el intervalo de 30 dias
        elif(len(local_values) < 30):
            mean = np.array(local_values).mean() # Se rellena con la media de las observaciones disponibles
            
        while(len(local_values) < 30):
            local_values.append(mean) # Rellenamos
        
        #values.append(np.array(local_values).reshape(1,-1))
        
        local_values = np.array(local_values).reshape(1, -1)
        values = values.append(pd.DataFrame(local_values)) # Transformamos a vector fila
        
    return values

values = add_velocities(sorted_cuad_data)

# Definicion de headers
headers = []
for i in range (1, 31):
    headers.append("v(n-" + str(i) +")")

# Guardamos
values.to_csv(os.getcwd() + "/historic data/features.csv", index=False, header=headers)

# Leemos 
values = pd.read_csv(os.getcwd() + "/historic data/features.csv")
values.head()
values.tail()

headers.append("Velocidad_Promedio")

# Concatenacion de los features
sorted_cuad_data2 = pd.concat([sorted_cuad_data, values], axis=1)
sorted_cuad_data2.head()
sorted_cuad_data2.tail()

sorted_cuad_data2.to_csv(os.getcwd() + "/historic data/cuad_data3.csv", index=False)




