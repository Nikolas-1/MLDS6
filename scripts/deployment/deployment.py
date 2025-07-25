# Cargamos las librerias

from pydantic import BaseModel
from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd
import os

class ApiInput(BaseModel):
    bedrooms: int
    bathrooms: float
    floors: float
    waterfront: int
    view: int
    condition: int
    grade: int
    log_sqft_above: float
    yr_built: int
    lat: float
    long: float
    log_sqft_living15: float
    log_sqft_lot15: float
    month: int
    has_basement: int
    was_renovated: int

class ApiOutput(BaseModel):
    predicted_price: str


app = FastAPI()

# Carga del modelo
#model = joblib.load("src\model.joblib")
model_path = os.path.join("src", "model.joblib")
model = joblib.load(model_path)

@app.post("/house_price", response_model=ApiOutput)
async def predict_price(data: ApiInput):
    # Convertir input en DataFrame
    input_data = [[
        data.bedrooms, data.bathrooms, data.floors, data.waterfront,
        data.view, data.condition, data.grade, data.log_sqft_above,
        data.yr_built, data.lat, data.long, data.log_sqft_living15,
        data.log_sqft_lot15, data.month, data.has_basement, data.was_renovated
    ]]

    input_df = pd.DataFrame(input_data, columns=[
    "bedrooms", "bathrooms", "floors", "waterfront", "view",
    "condition", "grade", "log_sqft_above", "yr_built", "lat", "long",
    "log_sqft_living15", "log_sqft_lot15", "month", "has_basement", "was_renovated"
    ])

    # Hacer predicción
    log_pred = model.predict(input_df)[0]
    pred = float(np.expm1(log_pred))  # deslogaritmizar

    pred_text = f"Predicción del modelo: ${pred:,.2f}"

    return ApiOutput(predicted_price=pred_text)


# Poner esto en anaconda prompt
# cd C:\Users\nikol\Documents\GitHub\MLDS6                  Cambiar a la carpeta root
# uvicorn scripts.deployment.deployment:app --reload        Correr el script desde ahí