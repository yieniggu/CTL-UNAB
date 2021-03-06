# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:48:22 2019

@author: Bastolo
"""
print("\nIniciando Script 00_13_19_19_1.py ...\n")

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("temporal_cuad_data_30.csv")

new_dataset = dataset.loc[(dataset["Hora2"] >= 6) & (dataset["Hora2"] <= 20)]

# Definicion de las columnas a ocupar
headers = ["id_Cuadrante", "week_day", "year_day", "year_week", "Hora2", "Minuto"]

# Ocupando las 7 mediciones
for i in range (1, 8):
    headers.append("v(n-" + str(i) +")")
    
# Obtenemos los valores de interes
X = new_dataset[headers].values
y = new_dataset[["Velocidad_Promedio"]].values

# Holdout
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, 
                                                    random_state=123 )

"""
# Normalizacion
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_tes2 = sc.transform(X_test)
"""

def coeff_determination(y_test, y_pred):
    from keras import backend as K
    SS_res =  K.sum(K.square( y_test-y_pred ))
    SS_tot = K.sum(K.square( y_test - K.mean(y_test) ) )
    return ( 1 - SS_res/(SS_tot + K.epsilon()) )

l1_bias = np.loadtxt("weights/00_13_19_19_1/bias1.csv", delimiter=",")
l1_weights = np.loadtxt("weights/00_13_19_19_1/weights1.csv", delimiter=",")
l2_bias = np.loadtxt("weights/00_13_19_19_1/bias2.csv", delimiter=",")
l2_weights = np.loadtxt("weights/00_13_19_19_1/weights2.csv", delimiter=",")
l3_bias = np.loadtxt("weights/00_13_19_19_1/bias3.csv", delimiter=",").reshape(-1)
l3_weights = np.loadtxt("weights/00_13_19_19_1/weights3.csv", delimiter=",").reshape(-1, 1)

ANN_Baseline = Sequential()
ANN_Baseline.add(Dense(19, input_dim=13, activation="sigmoid"))
ANN_Baseline.add(Dense(19, activation="sigmoid"))
ANN_Baseline.add(Dense(1, activation="linear"))

ANN_Baseline.layers[0].set_weights([l1_weights, l1_bias])
ANN_Baseline.layers[1].set_weights([l2_weights, l2_bias])
ANN_Baseline.layers[2].set_weights([l3_weights, l3_bias])

# MSE como metrica de evaluacion de la red
ANN_Baseline.compile(loss='mse', optimizer='adam', metrics=['mse', 'mae', coeff_determination])
    
history = ANN_Baseline.fit(X_train, y_train, epochs=1200, verbose=2, batch_size=30, validation_split=0.1)

layers = ANN_Baseline.layers
weights1 = layers[0].get_weights()[0]
bias1 = layers[0].get_weights()[1]
weights2 = layers[1].get_weights()[0]
bias2 = layers[1].get_weights()[1]
weights3 = layers[2].get_weights()[0]
bias3 = layers[2].get_weights()[1]

np.savetxt("weights/00_13_19_19_1/weights1.csv", weights1, delimiter=",", fmt="%s")
np.savetxt("weights/00_13_19_19_1/bias1.csv", bias1, delimiter=",", fmt="%s")
np.savetxt("weights/00_13_19_19_1/weights2.csv", weights2, delimiter=",", fmt="%s")
np.savetxt("weights/00_13_19_19_1/bias2.csv", bias2, delimiter=",", fmt="%s")
np.savetxt("weights/00_13_19_19_1/weights3.csv", weights3, delimiter=",", fmt="%s")
np.savetxt("weights/00_13_19_19_1/bias3.csv", bias3, delimiter=",", fmt="%s")

# Plot de mse
plt.figure(figsize=(10, 8))
plt.plot(history.history['mean_squared_error'])   #training
plt.plot(history.history['val_mean_squared_error']) #validation
plt.title('MSE')
plt.ylabel("Mse")
plt.yticks(np.arange(0, 900, 100))
plt.xlabel('Epoch')
plt.legend(['train', 'validation'], loc ='upper right')
plt.savefig("Mse4.png")
plt.show()
    
# Metrics evaluation
mse_train = history.history["mean_squared_error"][-1]
y_predict = ANN_Baseline.predict(X_test)

from sklearn.metrics import mean_squared_error
mse_test = mean_squared_error(y_test, y_predict)

from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_predict)

metrics_data = np.array([mse_train, mse_test, r2]).reshape(1, -1)

metrics = pd.DataFrame(metrics_data, columns=["mse_train", "mse_test", "r2"])
metrics.to_csv("00_13_19_19_1_metrics.csv")

print("\n\nScript ejecutado correctamente...")