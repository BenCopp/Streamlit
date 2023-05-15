import lightgbm as lgb
import uvicorn
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
import numpy as np
import joblib
from Fonction_API import traitement



model = lgb.Booster(model_file='./my_model.txt')


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.post('/prediction')
async def predict(json_data: dict):

  df= traitement(json_data)
  y_pred = model.predict(df)
  y_pred = y_pred.reshape((-1, 1))

  return {'prediction': y_pred.tolist()}
