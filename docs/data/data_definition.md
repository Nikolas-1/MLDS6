# Definición de los datos

## Origen de los datos

Los datos se encuentran disponibles en [Kaggle](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction/data), han sido descargados directamente desde allí y se han agregado al repositorio. Consisten en un archivo en formato CSV, conformado por 21 campos y 21613 registros, el cual ocupa 2.4 MB.

## Especificación de los scripts para la carga de datos

El script de carga de los datos se puede encontrar [aquí](../../scripts/data_acquisition/main.py). Los datos son cargados mediante la función `read_csv` de la librería `pandas`.

## Referencias a rutas o bases de datos origen y destino

A continuación se especifica la ruta de origen y destino para los datos.

### Rutas de origen de datos

Los datos originales se encuentran en la ruta: [`src/kc_house_data.csv`](../../src/kc_house_data.csv). Como se mencionó anteriormente, están estructurados en una archivo CSV.

El script de preprocesamiento se puede encontrar [aquí](../../scripts/preprocessing/main.py). A continuación, se describe el proceso de transformación y limpieza aplicado a los datos:

- Remover:
  - El identificador del identificador `id`. 
  - Se considera además remover la variable `zipcode`, pues se cuenta con otra información geográfica como `lat` y `long`.

- Extracción de características `year` y `month` a partir de la variable `date`

- Eliminar registros con valores atípicos y posiblemente erroneos en las siguientes variables:
  - `bedrooms`: se excluyen registros que contienen los valores 0 o 33 en este campo.
  - `bathrooms`: se excluyen registros que contienen 0 en este campo.

- Aplicar la transformación logarítmica `np.log1p()` a variables con fuerte sesgo positivo (o a la derecha):
  - `price`: Nuestra variable **objetivo**. En este caso es necesario hacer _back-transform_ a las predicciones.
  - `sqft_living`
  - `sqft_lot`
  - `sqft_above`
  - `sqft_living15`
  - `sqft_lot15`

- Se transforman a variable binaria:
  - `sqft_basement`: 0 sin sótano, 1 con sótano
  - `yr_renovated` (cambio a `was_renovated`):  0 sin renovar, 1 renovada

- Las siguientes variables se mantienen sin modificaciones:
  - `floors`
  - `waterfront`
  - `view`
  - `condition`
  - `grade`
  - `yr_built`
  - `lat`
  - `long`

  Finalmente, guardamos los cambios realizados en [`src/preprocessed.csv`](../../src/preprocessed.csv). Se está haciendo seguimiento con DVC.