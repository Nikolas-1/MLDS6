# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline entrenado para predecir el precio de casas en Seattle utilizando un modelo de regresión lineal.

## Descripción del modelo

El modelo baseline implementado es una regresión lineal (`LinearRegression` de `sklearn`). Se entrenó tanto con los datos originales como con una versión transformada mediante Análisis de Componentes Principales (PCA), con el objetivo de evaluar si la reducción de dimensionalidad mejora el rendimiento.

Este modelo sirve como línea base para comparar otros modelos más complejos como Random Forest, XGBoost, SVR, etc.

## Variables de entrada

Las variables de entrada utilizadas incluyen características estructurales y temporales de las viviendas:

- bedrooms
- bathrooms
- log_sqft_living
- log_sqft_lot
- floors
- waterfront
- view
- condition
- grade
- log_sqft_above
- has_basement
- log_sqft_living15
- log_sqft_lot15
- year
- month
- was_renovated

> Algunas variables fueron transformadas logarítmicamente para reducir la influencia de valores extremos, y se incluyeron variables binarias derivadas como `has_basement` y `was_renovated`.

## Variable objetivo

La variable objetivo (`target`) del modelo es:

- `price`: Precio de venta de la casa en dólares.

## Evaluación del modelo

### Métricas de evaluación

Se utilizaron las siguientes métricas de evaluación de regresión:

- **MAE (Mean Absolute Error)**: Error absoluto promedio.
- **RMSE (Root Mean Squared Error)**: Raíz cuadrada del error cuadrático medio.
- **MSE (Mean Squared Error)**: Error cuadrático medio.

### Resultados de evaluación

| Modelo               | MAE         | RMSE         | MSE               |
|----------------------|-------------|--------------|--------------------|
| Linear Regression    | 129,833.46  | 214,466.98   | 45,996,086,350.58  |
| Linear Regression + PCA | 129,833.46  | 214,466.98   | 45,996,086,350.58  |

> Nota: PCA no mejoró el desempeño en este caso. Ambos modelos obtuvieron los mismos resultados, lo que sugiere que la reducción de dimensionalidad no tuvo un impacto significativo en la regresión lineal aplicada.

## Análisis de los resultados

- El error promedio de aproximadamente **$129,833 USD** indica que el modelo baseline tiene un desempeño limitado para una tarea de regresión en precios de vivienda.
- **PCA no aportó mejoras**, lo cual puede indicar que la mayoría de la información relevante ya estaba contenida en las variables originales o que Linear Regression no se beneficia fuertemente de la reducción de dimensionalidad.
- Este modelo sirve como punto de partida. Se espera que modelos más complejos (como Random Forest, XGBoost o redes neuronales) logren mejoras sustanciales.

## Conclusiones

- El modelo baseline establece un rendimiento inicial para futuras comparaciones.
- Las métricas indican que hay espacio para mejorar significativamente la precisión.
- Se recomienda explorar modelos no lineales y con mayor capacidad de aprendizaje.
- Además, se pueden explorar técnicas de feature engineering, selección de variables y ajuste de hiperparámetros.

## Referencias

- Dataset: [Kaggle - House Sales in King County, USA](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction)
- Documentación de `scikit-learn` y `PCA`