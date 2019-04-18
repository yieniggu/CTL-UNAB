# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:06:38 2019

@author: Bastolo
"""

import pandas as pd
import glob, os

# Obtenemos los archivos a importar
historic_files = glob.glob(os.path.join(os.getcwd()+ '/historic data/01-20190312T042227Z-001/01/Datos GPS/Datos GPS 200x200 (2018)', "*.csv"))

# Importamos los archivos con la data historica
headers = ["id_Arco", "id_Cuadrante", "Nombre_Comuna", "Fecha", "Hora", "Velocidad_Promedio", "N_puntos", "N_vehiculos"]
historic_data = pd.DataFrame(columns=headers)

for file in historic_files:
    data = pd.read_csv(file, delimiter=';')
    historic_data = historic_data.append(data)

historic_data.head(5)

# Ordenamos data por cuadrante para procesarla
sorted_data = historic_data.sort_values(by="id_Cuadrante")
sorted_data = pd.read_csv(os.getcwd() + "/historic data/full sorted data.csv")
#sorted_data.head(20)

# Muestra para realizar prubeas
#sample_data = pd.read_csv(historic_files[0], delimiter=";")
#ss_data = sample_data.sort_values(by=["id_Cuadrante", "Fecha", "Hora"])

# Funcion que añade columnas clave a utilizar como variables de entrada:
# - Dia de la semana
# - Dia del año
# - Semana del año
# - Velocidad promedio en n-t, donde t representa a lo sumo 30 dias anteriores a n
def add_key_columns(data):
    temp_df = data
    
    #Definimos un timedelta para la comparacion
    diff = pd.Timedelta("30 days")
    
    temp_df["week_day"] = temp_df["Fecha"].dt.weekday
    temp_df["year_day"] = temp_df["Fecha"].dt.dayofyear
    temp_df["year_week"] = temp_df["Fecha"].dt.weekofyear
    
    # Arreglo de velocidades en n-t
    values = []
    for index, row in temp_df.iterrows():
        date = row.Fecha 
        value = temp_df.loc[(temp_df["Fecha"] - date <= diff) & (temp_df["Fecha"] - date >= pd.Timedelta(0))]["Velocidad_Promedio"].mean()
        values.append(value)
    
    temp_df["mean_v(n-t)"] = values # Agregamos la columna
    return temp_df


# Funcion para dividir y guardar la data por cuadrantes
def divide_by_cuad(data):
    # Convertir fechas a datetime
    data["Fecha"] = pd.to_datetime(data["Fecha"])
    
    # Ordenamos la data por cuadrantes, fecha y hora    
    sorted_data = data.sort_values(by=["id_Cuadrante", "Fecha", "Hora"])
    
    # Definimos los cuadrantes existentes en la data
    cuads = sorted_data["id_Cuadrante"].unique()
     
    # Iteramos por las tuplas agrupando la data por cuadrante
    for cuad in cuads:
        cuad_data = sorted_data.loc[sorted_data["id_Cuadrante"] == cuad]
        cuad_data = add_key_columns(cuad_data)
        cuad_data.to_csv(os.getcwd() +
                         "/historic data/by region/Cuad_" + str(cuad) + ".csv", index=False, sep=";")
  
# Leemos la data ordenada por cuadrante y la vamos dividiendo
sorted_data.to_csv(os.getcwd() + "/historic data/full sorted data.csv", index=False)
divide_by_cuad(sorted_data)