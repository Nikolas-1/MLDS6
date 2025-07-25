import joblib
import numpy as np
import pandas as pd

# Cargar modelo
model = joblib.load("src\model.joblib")  # Ajusta la ruta si es necesario

# Simular entrada
input_data = [[
    3,          # bedrooms
    2.0,        # bathrooms
    1.0,        # floors
    0,          # waterfront
    0,          # view
    3,          # condition
    7,          # grade
    7.5,        # log_sqft_above
    1990,       # yr_built
    47.5112,    # lat
    -122.257,   # long
    7.3,        # log_sqft_living15 (ejemplo)
    8.1,        # log_sqft_lot15 (ejemplo)
    5,          # month (ej: mayo)
    0,          # has_basement (ej: no)
    0           # was_renovated (ej: no)
]]

# Nombres en el mismo orden que el modelo espera
input_df = pd.DataFrame(input_data, columns=[
    "bedrooms", "bathrooms", "floors", "waterfront", "view",
    "condition", "grade", "log_sqft_above", "yr_built", "lat", "long",
    "log_sqft_living15", "log_sqft_lot15", "month", "has_basement", "was_renovated"
])

# Hacer predicción
log_pred = model.predict(input_df)[0]
pred = float(np.expm1(log_pred))  # deslogaritmizar

print(f"Predicción del modelo: ${pred:,.2f}")

#---------------------------------------------------------------------------------
# PROBAR API DESDE REQUEST
#---------------------------------------------------------------------------------

import requests
import os

#model_url = os.path.join("https://mlds6-production-0dfb.up.railway.app", "house_price")
model_url = "https://mlds6-production-0dfb.up.railway.app/house_price"

data = {
    "bedrooms": 3,
    "bathrooms": 2.0,
    "floors": 1.0,
    "waterfront": 0,
    "view": 0,
    "condition": 3,
    "grade": 7,
    "log_sqft_above": 7.5,
    "yr_built": 1990,
    "lat": 47.5112,
    "long": -122.257,
    "log_sqft_living15": 7.6,
    "log_sqft_lot15": 8.3,
    "month": 7,
    "has_basement": 0,
    "was_renovated": 0
}

response = requests.post(model_url, json=data)

print("Status code:", response.status_code)
print("Respuesta del modelo:", response.json())