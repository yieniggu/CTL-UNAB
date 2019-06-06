# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:12:05 2019

@author: Bastolo
"""

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Red neuronal considerando hora y minuto del dia
dataset = pd.read_csv(os.getcwd()+ "/historic data/cuad_data3.csv")

# Definicion de las columnas a ocupar
headers = ["id_Cuadrante", "week_day", "year_day", "year_week", "Hora2", "Minuto"]

# Ocupando las 30 mediciones
for i in range (1, 31):
    headers.append("v(n-" + str(i) +")") 
    
# Obtenemos los valores de interes
X = dataset[headers].values
y = dataset[["Velocidad_Promedio"]].values

# Holdout
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, 
                                                    random_state=123 )

# Normalizacion
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

ANN_Baseline = Sequential()
ANN_Baseline.add(Dense(20, input_dim=36, activation="sigmoid"))
ANN_Baseline.add(Dense(20, activation="sigmoid"))
ANN_Baseline.add(Dense(1, activation="linear"))

history= ANN_Baseline.fit(X_train, y_train, epochs=100, verbose=2, batch_size=40, validation_split=0.1)

# Plot de mse
plt.figure(figsize=(10, 8))
plt.plot(history.history['mean_squared_error'])   #training
plt.plot(history.history['val_mean_squared_error']) #validation
plt.title('MSE')
plt.ylabel("Mse")
plt.yticks(np.arange(200, 900, 100))
plt.xlabel('Epoch')
plt.legend(['train', 'validation'], loc ='upper right')
plt.savefig("Mse2.png")
plt.show()
    
# Metrics evaluation
mse_train = history.history["mean_squared_error"][-1]
y_predict = ANN_Baseline.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score
mse_test = mean_squared_error(y_test, y_predict)

r2 = r2_score(y_test, y_predict)

metrics_data = np.array([mse_train, mse_test, r2]).reshape(1, -1)

metrics = pd.DataFrame(metrics_data, columns=["mse_train", "mse_test", "r2"])
metrics.to_csv("metrics/03_36_20_20_1_metrics.csv")

