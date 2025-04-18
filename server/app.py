# server/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Charger modèle
model = joblib.load("model.pkl")

# Définir le schéma d'entrée
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# API
app = FastAPI()

@app.post("/predict")
def predict(data: IrisInput):
    X = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(X)[0]
    return {"prediction": int(prediction)}
