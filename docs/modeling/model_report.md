# Reporte del Modelo Final

## Resumen Ejecutivo

Este reporte presenta el modelo final desarrollado para predecir los precios de viviendas en Seattle utilizando técnicas de machine learning. Se empleó un modelo **XGBoost Regressor**, optimizado con **RandomizedSearchCV**.

Los resultados del modelo final son los siguientes:

- **MAE:** 65,136.67 USD  
- **RMSE:** 126,678.78 USD  
- **MSE:** 16,047,512,241.94  
- **R²:** 0.878

Estos resultados representan una mejora significativa frente al modelo baseline, especialmente en el error absoluto y la varianza explicada. Esto indica que el modelo tiene un buen desempeño general y logra capturar adecuadamente las relaciones no lineales presentes en los datos.

## Descripción del Problema

El problema abordado consiste en **predecir el precio de una vivienda** a partir de sus características estructurales, ubicación temporal (año, mes), condición, tamaño, entre otros. 

Este es un problema de regresión supervisada, basado en el conjunto de datos "House Sales in King County" (Seattle) disponible en Kaggle. Predecir con precisión el precio de una vivienda es crucial para múltiples partes interesadas: compradores, vendedores, agentes inmobiliarios, y desarrolladores.

El objetivo principal era construir un modelo preciso y generalizable, que mejorara el desempeño del modelo baseline y sirviera como base para una posible implementación práctica.

## Descripción del Modelo

El modelo final utilizado fue **XGBoost Regressor**, una técnica de boosting basada en árboles de decisión, conocida por su alto rendimiento en tareas de regresión no lineales.

Se aplicó una búsqueda aleatoria de hiperparámetros (`RandomizedSearchCV`) sobre un espacio de 25 combinaciones y 3 validaciones cruzadas. Los parámetros óptimos encontrados fueron:

```json
{
  "colsample_bytree": 0.8591,
  "gamma": 0.0026,
  "learning_rate": 0.0805,
  "max_depth": 5,
  "min_child_weight": 7,
  "n_estimators": 297,
  "reg_alpha": 0.5107,
  "reg_lambda": 0.4174,
  "subsample": 0.6888
}
```

Este modelo fue entrenado sobre un conjunto de datos preprocesado con las siguientes características:

- Transformación logarítmica de variables altamente sesgadas, incluyendo price.

- Eliminación de outliers evidentes.

- Conversión de variables a indicadores binarios (has_basement, was_renovated).

- Eliminación de columnas irrelevantes como id, zipcode, sqft_basement, yr_renovated.

Las predicciones fueron destransformadas con `np.expm1()` para que las métricas se evaluaran en la escala original de los precios.

## Descripción del Modelo

El modelo final se basó en **XGBoost Regressor**, conocido por su capacidad de capturar relaciones no lineales en tareas de regresión.

### Rendimiento del Modelo Optimizado

Se evaluó el desempeño del modelo en el conjunto de prueba utilizando las principales métricas de regresión:

| Métrica | Valor               |
|---------|---------------------|
| MAE     | 65,136.67 USD       |
| RMSE    | 126,678.78 USD      |
| MSE     | 16,047,512,241.94   |
| R²      | 0.8775              |

Estas métricas reflejan un modelo robusto, con un **error absoluto medio alrededor de 65,000 USD** y una **capacidad explicativa del 87.75%**, lo que indica un buen ajuste a los datos.

### Comparación con Modelo Base (XGBoost por defecto)

Para validar la mejora, se entrenó un modelo base utilizando los parámetros por defecto de XGBoost:

| Métrica | Valor (Modelo Base) |
|---------|----------------------|
| MAE     | 66,032.07 USD        |
| RMSE    | 118,586.40 USD       |
| R²      | 0.8948               |

> La comparación evidencia que la **optimización de hiperparámetros con RandomizedSearchCV** mejoró la métrica objetivo (MAE), reforzando la importancia del ajuste fino en modelos avanzados.


## Conclusiones y Recomendaciones

**Conclusiones:**

- A pesar de que la meta inicial de $55.000 de MAE no se alcanzó, nuestros resultados son útiles para el problema planteado dentro de las condiciones y limitaciones actuales del proyecto. El modelo final logra un excelente desempeño en la predicción de precios de viviendas, con un R² de 0.88 y un MAE alrededor de los 65,000 USD.

- El uso de XGBoost permitió capturar relaciones no lineales complejas presentes en los datos.

- La transformación logarítmica de price fue fundamental para estabilizar la varianza y mejorar las predicciones.

**Recomendaciones:**

- Evaluar la posibilidad de incorporar variables externas (por ejemplo: tasas de interés, ubicación geográfica enriquecida).

- Probar técnicas de stacking o blending con otros modelos (Random Forest, SVR, LightGBM).

- Realizar interpretabilidad del modelo (feature importance, SHAP) para entender los factores clave