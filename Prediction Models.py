# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:48:14 2019

@author: Bastolo
"""

import pandas as pd
import glob, os

# Obtenemos los archivos a importar
historic_files = glob.glob(os.path.join(os.getcwd()+ '/historic data/01-20190312T042227Z-001/01/Datos GPS/Datos GPS 200x200 (2018)', "*.csv"))

# Importamos los archivos con la data historica
historic_data_headers = ["id_Arco", "id_Cuadrante", "Nombre_Comuna", "Fecha", "Hora", "Velocidad_Promedio", "N_puntos", "N_vehiculos"]
historic_data = pd.DataFrame(columns=historic_data_headers)

for file in historic_files:
    data = pd.read_csv(file, delimiter=';')
    historic_data = historic_data.append(data)

historic_data.head(5)


"""
     Obteniendo prediccion básica utilizando promedios historicos por cuadrante
"""

# Dividimos data por arco-velocidad y cuadrante-velocidad
basic_prediction_data = historic_data[["id_Arco", "id_Cuadrante", "Velocidad_Promedio"]]
basic_prediction_data.head(5)

# Transformamos al tipo de dato correspondiente
basic_prediction_data["Velocidad_Promedio"] = pd.to_numeric(basic_prediction_data["Velocidad_Promedio"])

# Agrupamos por cuadrante (operacion mas basica)
basic_prediction_data.groupby("id_Cuadrante").mean()

# Agrupamos por cuadrante y arco
basic_prediction_data.groupby(["id_Cuadrante", "id_Arco"]).mean()

"""
    Obteniendo prediccion utilizando una red neuronal, implementacion rapida para probar funcionamiento
"""








