# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:07:10 2019

@author: Bastolo
"""


import pandas as pd
import numpy as np

# Leemos la data
cuad_data = pd.read_csv("temporal_cuad_data_h.csv")

cuad_data.head()

def add_velocities(data):
    #values = []
    values = pd.DataFrame()
    for index, row in data.iterrows():
        cuad, day, hour = row.id_Cuadrante, row.year_day, row.Hora2
        
        print("Analizando tupla: " + str(index) + "- Cuadrante: " + str(cuad))
        
        # Se obtienen las tuplas que tengan informacion del mismo cuadrante y de dias anteriores (a lo mas 30 dias)
        local_values = data.loc[(data["id_Cuadrante"] == cuad) & (day - data["year_day"] <= 30) & (day - data["year_day"] >= 0)]
        
        # Se elimina la tupla en estudio, asi como aquellas que se midieron en el mismo instante (hora y minuto)
        local_values = local_values.loc[(local_values["year_day"] != day) | ((local_values["year_day"] == day) & (local_values["Hora2"] == hour))]
        
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

values = add_velocities(cuad_data).reset_index()
values = values.iloc[:, 1:]

# Definicion de headers
headers = []
for i in range (1, 31):
    headers.append("v(n-" + str(i) +")")

values.columns = headers

# Guardamos
values.to_csv("features_h.csv", index=False)

# Concatenacion de los features
cuad_data2 = pd.concat([cuad_data, values], axis=1)
cuad_data2.head()
cuad_data2.tail()

cuad_data2.to_csv("temporal_cuad_data_30_h.csv", index=False)
