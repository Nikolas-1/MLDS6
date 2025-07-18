# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline entrenado para predecir el precio de casas en Seattle, utilizando un modelo de regresión lineal.

## Descripción del modelo

El modelo baseline implementado es una regresión lineal (`LinearRegression` de `sklearn`). Se entrenó sobre datos preprocesados, con transformaciones logarítmicas aplicadas a varias variables, incluyendo la variable objetivo `price`, con el fin de mejorar la distribución y reducir la influencia de valores atípicos.

Se eliminó la versión con PCA para este reporte, ya que no aportó mejoras en versiones anteriores y fue descartada en esta etapa.

## Variables de entrada

Las variables de entrada utilizadas incluyen una selección de características estructurales y temporales de las viviendas. Luego del preprocesamiento, se descartaron tres variables consideradas colineales o no informativas para esta versión del modelo:

Variables utilizadas:

- bedrooms
- bathrooms
- floors
- waterfront
- view
- condition
- grade
- has_basement
- log_sqft_above
- log_sqft_living15
- log_sqft_lot15
- month
- was_renovated

> Variables descartadas: `log_sqft_living`, `log_sqft_lot`, `year`.

## Variable objetivo

La variable objetivo (`target`) es:

- `log_price`: Precio de la casa transformado con logaritmo natural con `np.log1p(price)`.

Las predicciones fueron luego destransformadas con `np.expm1()` para ser evaluadas en la escala original de precios en dólares.

## Evaluación del modelo

### Métricas de evaluación

Se utilizaron las siguientes métricas de regresión:

- **MAE (Mean Absolute Error)**: Error absoluto promedio.
- **RMSE (Root Mean Squared Error)**: Raíz del error cuadrático medio.
- **MSE (Mean Squared Error)**: Error cuadrático medio.
- **R² (R-squared)**: Coeficiente de determinación.

### Resultados de evaluación

| Modelo             | MAE         | RMSE         | MSE               | R²        |
|--------------------|-------------|--------------|--------------------|-----------|
| Linear Regression  | 106,937.11  | 175,858.13   | 30,926,084,016.41  | 0.764     |

> Las métricas fueron calculadas después de destransformar las predicciones (`np.expm1`) para que estén en la misma escala que los precios reales.

## Análisis de los resultados

- El error absoluto promedio de **$106,937** sugiere que el modelo aún tiene margen de mejora, pero mejora significativamente con respecto al baseline sin transformación logarítmica.
- Un R² de **0.76** indica que el modelo explica aproximadamente el 76% de la varianza en los datos de prueba.
- La transformación logarítmica de la variable objetivo ayudó a estabilizar la varianza y mejorar la capacidad predictiva del modelo lineal.
- El modelo puede beneficiarse de técnicas más avanzadas como regularización (Ridge/Lasso), modelos no lineales, tuning de hiperparámetros y mejores estrategias de selección de variables.

## Conclusiones

- El modelo baseline con regresión lineal y variable objetivo log-transformada ofrece un rendimiento razonable, explicando más del 75% de la variabilidad.
- A pesar de las mejoras con el logaritmo, aún existen errores promedio altos en valores absolutos, por lo que se sugiere explorar modelos más complejos.
- En siguientes iteraciones se puede aplicar PCA correctamente, usar ingeniería de variables adicional o modelos como Random Forest, XGBoost o redes neuronales.

## Referencias

- Dataset: [Kaggle - House Sales in King County, USA](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction)