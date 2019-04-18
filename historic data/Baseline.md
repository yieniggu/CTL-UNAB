# Prediccion utilizando Redes Neuronales Artificiales

En esta seccion se pretende establecer un baseline basico para la prediccion de velocidades utilizando la data historica. A continuación se presentaran diferentes configuraciones para las capas ocultas, no asi para las de entrada y salida. Cada una de las arquitecturas sera analizada graficamente y evaluada utilizando MSE para entrenamiento y testeo.

### Capas de entrada y output
La capa de entrada (Input Layer) constará, para todos los casos de esta sección, de las siguientes variables:

+ Cuadrante: Representado por su id.
+ Dia de la semana: Representado numericamente de 0 a 6, empezando por el dia lunes.
+ Dia del año: Representado numericamente de 1 a 365, empezando por el 1 de enero.
+ Semana del año: Representado numericamente de 1 a 52, empezando por la primera semana de enero.
+ Velocidades medias de los 30 dias anteriores.

**La capa de salida constara de una neurona con activacion lineal, la cual entregara la velocidad media calculada por la red para la entrada entregada.**


### Primera Configuración [5 - 5 - 4 - 1]

El código de esta sección se puede encontrar [aqui](https://github.com/yieniggu/CTL-UNAB/blob/master/02-%20Baseline.py) (Lineas 53 - 74 del codigo)

#### Configuracion
+ Capas ocultas: 2; 5 y 4 unidades respectivamente.
+ Numero de epocas: 100
+ Numero de batches: 100
+ Tiempo medio por epoca: 35s

#### Plot de mse
![alt text](https://github.com/yieniggu/CTL-UNAB/blob/master/src/Baselines/Mse1.png "MSE configuracion 1")

**Mse train: 255.82**;
**Mse test: 253.6**
