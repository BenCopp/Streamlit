import lightgbm as lgb
import uvicorn
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
import numpy as np
import joblib
from Fonction_API import traitement
import shap


model = lgb.Booster(model_file='./my_model.txt')
with open('./list_column_final.txt', 'r') as f:
  columns_value = [line.strip() for line in f.readlines()]

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


@app.post('/plot')

async def predict(json_data: dict):

  
  df= traitement(json_data)
  y_pred = model.predict(df)

  y_pred = y_pred.reshape((-1, 1))


  data_type = str(type(df))
  df = pd.DataFrame(df, columns= columns_value )
  data_type = str(type(df))

  model.params['objective'] = 'binary'
  explainer = shap.Explainer(model)
  shap_values = explainer(df)
  feature_names = df.columns.values.tolist()
  shap_values = explainer.shap_values(df)
  shap_list = shap_values[0].tolist()

  return {'data_type': shap_list}


