# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:02:43 2019

@author: Bastolo
"""

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leemos la data desde csv
cuad_data = pd.read_csv(os.getcwd() + "/historic data/cuad_data.csv", delimiter=";")

# Ordenamos por cuadrante y fecha
sorted_cuad_data = cuad_data.sort_values(by = ["id_Cuadrante", "Fecha"])
sorted_cuad_data.head()

# Obtenemos los valores de interes
X = sorted_cuad_data[["id_Cuadrante", "week_day", "year_day", "year_week", "mean_v(n-t)"]].values
y = sorted_cuad_data[["Velocidad_Promedio"]].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, 
                                                    random_state=123 )

# Normalizacion
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# k-fold cross validation
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score

def build_classifier(input_layer_dim = 5, h1=4, h2=5):
    # Modelamiento de la red X=5, Z1=4, Z2=4, Y=1
    ANN_Baseline = Sequential()
    ANN_Baseline.add(Dense(h1, input_dim=input_layer_dim, activation="sigmoid"))
    ANN_Baseline.add(Dense(h2, activation="sigmoid"))
    ANN_Baseline.add(Dense(1, activation="linear"))
    
    # MSE como metrica de evaluacion de la red
    ANN_Baseline.compile(loss='mse', optimizer='adam', metrics=['mse'])
    
    return ANN_Baseline

# First baseline construction
Ann_Baseline = build_classifier()
history= Ann_Baseline.fit(X_train, y_train, epochs=500, verbose=2, batch_size=100, validation_split=0.1)

# Plot de mse
plt.figure(figsize=(10, 8))
plt.plot(history.history['mean_squared_error'])   #training
plt.plot(history.history['val_mean_squared_error']) #validation
plt.title('MSE')
plt.ylabel("Mse")
plt.yticks(np.arange(200, 900, 100))
plt.xlabel('Epoch')
plt.legend(['train', 'validation'], loc ='upper right')
plt.savefig("Mse.png")
plt.show()

# Metrics evaluation
mse_train = history.history["mean_squared_error"][-1]
y_predict = Ann_Baseline.predict(X_test)

from sklearn.metrics import mean_squared_error
mse_test = mean_squared_error(y_test, y_predict)


Ann_Baseline = build_classifier(5, 10, 8)
history= Ann_Baseline.fit(X_train, y_train, epochs=100, verbose=2, batch_size=100, validation_split=0.1)

# Plot de mse
plt.figure(figsize=(10, 8))
plt.plot(history.history['mean_squared_error'])   #training
plt.plot(history.history['val_mean_squared_error']) #validation
plt.title('MSE')
plt.ylabel("Mse")
plt.yticks(np.arange(200, 900, 100))
plt.xlabel('Epoch')
plt.legend(['train', 'validation'], loc ='upper right')
plt.savefig("Mse.png")
plt.show()

# Metrics evaluation
mse_train = history.history["mean_squared_error"][-1]
y_predict = Ann_Baseline.predict(X_test)

from sklearn.metrics import mean_squared_error
mse_test = mean_squared_error(y_test, y_predict)





# Cross validation
ANN_Baseline = KerasClassifier(build_classifier, batch_size=100, epochs=100, validation_split=0.1, verbose=2)
errors =  cross_val_score(estimator = ANN_Baseline, X = X_train, y = y_train, cv=10, n_jobs=-1)

