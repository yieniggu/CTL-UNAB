# Prediccion utilizando Redes Neuronales Artificiales

En esta seccion se pretende establecer un baseline basico para la prediccion de velocidades utilizando la data historica. A continuación se presentaran diferentes configuraciones tanto para las capas ocultas como para las de entrada. No así la de salida. Cada una de las arquitecturas sera analizada graficamente y evaluada utilizando MSE para entrenamiento y testeo, ademas del coefiente de correlacion (r2) en algunas de ellas.

### Capas de entrada y output (tres primeros ejemplos)
La capa de entrada (Input Layer) constará, para la mayor parte de los casos de esta sección, de las siguientes variables:

+ Cuadrante: Representado por su id.
+ Dia de la semana: Representado numericamente de 0 a 6, empezando por el dia lunes.
+ Dia del año: Representado numericamente de 1 a 365, empezando por el 1 de enero.
+ Semana del año: Representado numericamente de 1 a 52, empezando por la primera semana de enero.
+ Velocidades medias de los dias anteriores:
  + Caso mas simple: velocidades medias representadas por una variable que consiste en los promedios de las mediciones previas.

**La capa de salida constara de una neurona con activacion lineal, la cual entregara la velocidad media calculada por la red para la entrada entregada.**


### Primera Configuración [5 - 5 - 4 - 1]

El código de esta sección se puede encontrar [aqui](https://github.com/yieniggu/CTL-UNAB/blob/master/scripts/spyder/02-%20Baseline.py) (Lineas 53 - 74 del codigo)

#### Configuracion
+ Capas ocultas: 2; 5 y 4 unidades respectivamente.
+ Numero de epocas: 100
+ Numero de batches: 100
+ Tiempo medio por epoca: 35s
+ Funcion de activación capas ocultas: sig

#### Plot de mse
![alt text](https://github.com/yieniggu/CTL-UNAB/blob/master/src/Baselines/Mse1.png "MSE configuracion 1")

**Mse train: 255.82**;
**Mse test: 253.6**

### Segunda Configuración [5 - 10 - 8 - 1]
El código de esta sección se puede encontrar [aqui](https://github.com/yieniggu/CTL-UNAB/blob/master/scripts/spyder/02-%20Baseline.py) (Lineas 78 - 100 del codigo)

### Configuracion
+ Capas ocultas: 2; 10 y 8 unidades respectivamente.
+ Numero de epocas: 100
+ Numero de batches: 100
+ Tiempo medio por epoca: 37s
+ Funcion de activación capas ocultas: sig

#### Plot de mse
![alt text](https://github.com/yieniggu/CTL-UNAB/blob/master/src/Baselines/Mse2.png "MSE configuracion 2")

**Mse train: 255.76**;
**Mse test: 253.73**

### Capas de entrada y output 

+ Cuadrante: Representado por su id.
+ Dia de la semana: Representado numericamente de 0 a 6, empezando por el dia lunes.
+ Dia del año: Representado numericamente de 1 a 365, empezando por el 1 de enero.
+ Semana del año: Representado numericamente de 1 a 52, empezando por la primera semana de enero.
+ Hora del dia: Representada numericamente desde 0 a 23
+ Minuto de la hora: Representada numericamente en intervalos de 15 minutos (0-15-30-45)
+ Velocidades medias de los dias anteriores:
  + Caso mas simple: velocidades medias representadas por una variable que consiste en los promedios de las mediciones previas.
  + Caso medio: velocidades medias representadas por tantas variables como mediciones previas por dia se deseen considerar.
  + Caso ideal: velocidades medias previas representadas por un vector que contiene la velocidad media en ese instante del dia.

### Tercera Configuracion [36 - 19 - 19 - 1]
El código de esta sección se puede encontrar [aqui](https://github.com/yieniggu/CTL-UNAB/blob/master/scripts/spyder/02-%20Baseline.py) (Lineas 104 - 154 del codigo)

### Configuracion
+ Capas ocultas: 2; 19 unidades cada una.
+ Numero de epocas: 500
+ Numero de batches: 100
+ Tiempo medio por epoca: 37s
+ Funcion de activación capas ocultas: sig

#### Plot de mse
![alt text](https://github.com/yieniggu/CTL-UNAB/blob/master/src/Baselines/Mse3.png)

**Mse train: 265.96**;
**Mse test: 265.18**

### Cuarta Configuración [13 - 15 - 17 - 15 - 1]
El código de esta sección se puede encontrar [aqui](https://github.com/yieniggu/CTL-UNAB/blob/master/scripts/raw/fully%20connecteds/01_13_15_17_15_1.py) 

### Configuracion
+ Capas ocultas: 3; 15, 17, y 15 unidades respectivamente.
+ Numero de epocas: 100
+ Numero de batches: 30
+ Tiempo medio por epoca: 93s
+ Funcion de activación capas ocultas: relu

#### Plot de mse
![alt text](https://github.com/yieniggu/CTL-UNAB/blob/master/src/Baselines/Mse_13_15_17_15_1.png)

**Mse train: 264.946**;
**Mse test: 263.73**;
**r2 score: 0.669**

**Consideraciones: La base de datos ha sido reducida para tomar en cuenta los datos cuyas mediciones se encuentren en la ventana de tiempo que incluya, al menos, 2% del total de ejemplos. Asimismo, para esta configuración se consideraron solamente las 7 mediciones previas registradas.**

### Quinta Configuración [9 - 12 - 15 - 12 - 1]
El código de esta sección se puede encontrar [aqui](https://github.com/yieniggu/CTL-UNAB/blob/master/scripts/raw/fully%20connecteds/02_9_12_15_12_1.py) 

### Configuracion
+ Capas ocultas: 3; 12, 17, y 15 unidades respectivamente.
+ Numero de epocas: 100
+ Numero de batches: 30
+ Tiempo medio por epoca: 93s
+ Funcion de activación capas ocultas: tanh

#### Plot de mse
![alt text](https://github.com/yieniggu/CTL-UNAB/blob/master/src/Baselines/Mse_9_12_15_12_1.png)

**Mse train: 277.38**;
**Mse test: 275.94**;
**r2 score: 0.653**

**Consideraciones: La base de datos ha sido reducida para tomar en cuenta los datos cuyas mediciones se encuentren en la ventana de tiempo que incluya, al menos, 2% del total de ejemplos. Asimismo, para esta configuración se consideraron solamente las 3 mediciones previas registradas.**


