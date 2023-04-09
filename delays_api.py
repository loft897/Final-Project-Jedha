from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
import pickle
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from airports import list_airports



# Création de l'application FastAPI
app = FastAPI()




# Chargement des modèles
with open("./ml_models/classifier.pkl", "rb") as f:
    classifier = pickle.load(f)

with open("./ml_models/regressor.pkl", "rb") as f:
    regressor = pickle.load(f)

# Définition de la structure des données d'entrée
class Flight(BaseModel):
    MONTH: int
    CARRIER_NAME: str
    CRS_DEP_TIME: int
    DEP_TIME: float
    ARR_TIME: float
    ARR_DELAY_NEW: float
    CRS_ARR_TIME: int
    CRS_ELAPSED_TIME: int
    ACTUAL_ELAPSED_TIME: int

# route pour un message de bienvenue à l'adresse racine
welcome_message = 'Bienvenue sur Flights Delays, votre compagnon de voyage!'
@app.get("/")
async def Welcome():
    return welcome_message


# Endpoint pour rechercher l'aeroport par son code
@app.get("/airport/{code}")
async def get_airport_name(code: str):
    if code.upper() in list_airports:
        return {code.upper(): list_airports[code.upper()]}
    else:
        return {"Airport not found, please check your airport code again!"}


# Endpoint pour prédire si un vol est en retard ou pas et le delai de retard
@app.post("/predict")
async def predict_delay(flight: Flight):
    # Créer un DataFrame à partir de l'objet Flight
    input_data = pd.DataFrame([flight.dict()])

    # Encoder la feature CARRIER_NAME
    ohe = OneHotEncoder(handle_unknown='ignore')
    ohe.fit(input_data[['CARRIER_NAME']])
    carrier_encoded = ohe.transform(input_data[['CARRIER_NAME']]).toarray()
    input_data = np.concatenate((input_data.drop('CARRIER_NAME', axis=1), carrier_encoded), axis=1)

    # Charger les modèles de ML
    with open("./ml_models/classifier.pkl", "rb") as f:
        classifier = pickle.load(f)
    with open("./ml_models/regressor.pkl", "rb") as f:
        regressor = pickle.load(f)

    # Faire des prédictions avec les modèles
    pred_class = classifier.predict(input_data)[0]
    if pred_class == 0:
        return {"Résultat: Il y'aurait pas de retard sur ce vol."}

    pred_delay = regressor.predict(input_data)[0]
    return {"Résultat: Il y'aurait du retard sur ce vol de ", pred_delay, " minutes."}