# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Predictor del precio de viviendas en King County. Guardado como `model.joblib`. En MLflow como `XGBRegressor_Final`.
- **Plataforma de despliegue:** Se usa Railway como plataforma para desplegar nuestra aplicación de FastAPI.
- **Requisitos técnicos:** 
  - Python 3.12.3
  - Librerías necesarias: 

  ```
  scikit-learn==1.7.0
  fastapi==0.116.1
  uvicorn==0.35.0
  xgboost==3.0.2
  numpy==2.3.1
  pandas==2.3.1
  joblib==1.5.1
  ```

- **Requisitos de seguridad:** no se implementaron mecanismos específicos de seguridad (omitiendo autenticación, autorización o cifrado de datos).
- **Diagrama de arquitectura:**
  
  ![Arquitectura](../images/diagrama_arquitectura.png)

## Código de despliegue

- **Archivo principal:** [deployment.py](../../scripts/deployment/deployment.py)
- **Rutas de acceso a los archivos:** 
  - [scripts/deployment/deployment.py](../../scripts/deployment/deployment.py)
  - [requirements.txt](../../requirements.txt)
  - [railway.json](../../railway.json)
  - [src/model.joblib](../../src/model.joblib)

- **Variables de entorno:** (lista de variables de entorno necesarias para el despliegue)

## Documentación del despliegue

- **Instrucciones de instalación:** 
  1. Clonar el repositorio del proyecto:
   ```
   git clone https://github.com/Nikolas-1/MLDS6.git
   cd MLDS6
   ```
  2. Crear y activar un entorno virtual (opcional):
  - En Linux
  ```
  python -m venv venv
  source venv/bin/activate
  ```
  - O en Windows:
  ```
  python3 -m venv venv
  venv\Scripts\activate
  ```
  3. Instalar las dependencias necesarias:
  ```
  pip install -r requirements.txt
  ```

- **Instrucciones de configuración:** 
  - Ejecuta:
  ```
  cd scripts/deployment/deployment.py
  uvicorn deployment:app --reload
  ```
- **Instrucciones de uso:** 
  - Una vez el servidor esté corriendo, abre tu navegador y visita http://127.0.0.1:8000/docs
  - Para probar el modelo:
    - Busca el endpoint POST /house_price.
    - Haz clic en "Try it out".
    - Ingresa los valores requeridos por el modelo en el formulario. Puedes ver [test.py](../../scripts/deployment/test.py) para una muestra de la estructura de la entrada.
    - Haz clic en "Execute" y verás la predicción como respuesta.