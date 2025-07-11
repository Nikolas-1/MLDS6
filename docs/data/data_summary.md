# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

Se cuenta con 21 columnas y 21613 filas, estos datos son de ventas de viviendas en la ciudad de seattle USA, todos estos datos a excepción de la fecha, la cual esta en datetime, son numericos. Las variables que más afectan el precio de venta son el numero de habitaciones, baños y metros cuadrados, las demas variables tienen baja correlación. Finalmente no se cuenta con valores faltantes en el dataset.

## Resumen de calidad de los datos

El dataset no tiene valores nulos o faltantes, por lo que no se tendra que imputar o aplicar tecnicas de llenado, por otro lado si se encontrarón valores atipicos en la columna de precio ya que la mayor parte de la distribución esta en un rango similar de precio, esto probablemente sea por la ubicación geografica de la vivienda ya que los factores sociales pueden influir, este preprocesamiento se tratara en su script correspondiente.

## Variable objetivo

La variable objetivo es el precio de las casas, como se menciono anteriormente la grafica tiene una distribución donde la mayor parte de los datos se concentran en la parte izquierda del grafico.

![alt text](image.png)

Por otro lado se grafico la tendencia del precio a lo largo del tiempo de acuerdo a la fecha de construcción de la vivienda y la fecha de venta de esta, y se obtuvo una grafica con rango de precios muy cercanos entre sí.

![alt text](image-1.png)

## Variables individuales

La siguiente figura corresponde a una matriz de correlación entre todas las variables del dataset, en esta se puede ver que las columnas que más afectan la variable objetivo son el numero de habitaciones, baños y el area.

Existen relaciones entre otras variables debido a que son de naturaleza similar, como lo podria ser el area construida y el area del sotano o azotea.

![alt text](image-2.png)

## Ranking de variables

Las variables más importantes en la predicción del precio de venta son:

1. Area construida
2. Numero de baños
3. Numero de Habitaciones

## Relación entre variables explicativas y variable objetivo

Como se puede ver en el anterior grafico, a medida que aumentamos el area o el numero de habitaciones/baños el precio tiende a aumentar, esta tendencia se ve fuertemente aplicada con el area donde se visualiza claramente como este precio aumenta muy cercano a una tendencia lineal.


![alt text](image-3.png)
