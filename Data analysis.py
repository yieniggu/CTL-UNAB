# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 01:23:31 2019

@author: Bastolo
"""

import pandas as pd
import os, glob
import matplotlib.pyplot as plt
import numpy as np


# Se obtienen los archivos con data historica y secuencial
historic_files = glob.glob(os.path.join(os.getcwd()+ '/historic data/01-20190312T042227Z-001/01/Datos GPS/Datos GPS 200x200 (2018)', "*.csv"))
sequential_files = glob.glob(os.path.join(os.getcwd()+ '/02-20190312T042607Z-001/02/Datos GPS/Detalle GPS', "*.csv"))

historic_data_headers = ["id_Arco", "id_Cuadrante", "Nombre_Comuna", "Fecha", "Hora", "Velocidad_Promedio", "N_puntos", "N_vehiculos"]
historic_data = pd.DataFrame(columns=historic_data_headers)


for file in historic_files:
    data = pd.read_csv(file, delimiter=';')
    historic_data = historic_data.append(data)

historic_data.head(5)

""" 
    Analisis de data historica
"""


#====================== Analisis de Cuadrantes =================

# Obtenemos la data de los cuadrantes
uni_data = historic_data["id_Cuadrante"]

uni_data.plot.hist(grid=True, bins=7, rwidth=0.9, color='#607c8e')
plt.title('Cuadrantes visitados')
plt.xlabel('id Cuadrante')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.75)

# =================== Analisis de comunas ==================
uni_data = historic_data["Nombre_Comuna"]

from collections import Counter
counter = Counter(uni_data)

df = pd.DataFrame.from_dict(counter, orient='index')
df.plot(kind='bar')
plt.grid(axis='y', alpha=0.75)
plt.ylabel('Frequencia')
plt.title("Comunas transitadas")

# ================== Analisis de Fecha ==========================
# Transformamos las fechas a datetime
historic_data["Fecha"] = pd.to_datetime(historic_data["Fecha"])    

# Obtenemos la data de las fechas
uni_data = historic_data["Fecha"]

# Agrupamos los datos por mes y ploteamos
uni_data.groupby(uni_data.dt.month).count().plot(kind="bar")
plt.grid(axis='y', alpha=0.75)
plt.ylabel('Frequencia')
plt.xlabel("Mes")
plt.title("Transito de flota por mes")

# =================== Analisis por hora del dia ====================
# Transformamos las horas a datetime
historic_data["Hora"] = pd.to_datetime(historic_data["Hora"])

# Transformamos las horas a datetime
historic_data["Hora"] = pd.to_datetime(historic_data["Hora"])

# Obtenemos los datos por hora
uni_data = historic_data["Hora"]

# Agrupamos los datos por hora y ploteamos
uni_data.groupby(uni_data.dt.hour).count().plot(kind="bar")
plt.grid(axis='y', alpha=0.75)
plt.ylabel('Frequencia')
plt.xlabel("Hora del dia")
plt.title("Transito de flota por hora")

# ============== Analisis de velocidades =================================
# Obtenemos los datos de velocidades
uni_data = historic_data["Velocidad_Promedio"]

# Ploteo de las velocidades
uni_data.plot.hist(grid=True, bins=5, rwidth=0.9, color='#607c8e')
plt.title("Velocidades medidas")
plt.xlabel('Velocidad promedio')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.75)







