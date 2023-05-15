import lightgbm as lgb
import uvicorn
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
import numpy as np
import joblib





def traitement(json_data):
  
  df =pd.DataFrame.from_dict(json_data)

  feature1_encoder = joblib.load('./Encoder/FLAG_OWN_CAR_encoder.joblib')
  feature2_encoder = joblib.load('./Encoder/FLAG_OWN_REALTY_encoder.joblib')
  feature3_encoder = joblib.load('./Encoder/NAME_CONTRACT_TYPE_encoder.joblib')
  imputer = joblib.load('./Encoder/imputer.joblib')
  scaler = joblib.load('./Encoder/scaler.joblib')
  with open('./list_column_dummmies.txt', 'r') as f:
    cols_dummies = [line.strip() for line in f.readlines()]

  with open('./list_column_final.txt', 'r') as f:
    cols_to_keep = [line.strip() for line in f.readlines()]

  df.replace({'XNA': np.nan, 'XNP': np.nan, 'Unknown': np.nan}, inplace = True)

  df['FLAG_OWN_CAR'] = feature1_encoder.transform(df['FLAG_OWN_CAR'])
  df['FLAG_OWN_REALTY'] = feature2_encoder.transform(df['FLAG_OWN_REALTY'])
  df['NAME_CONTRACT_TYPE'] = feature3_encoder.transform(df['NAME_CONTRACT_TYPE'])

  df = pd.get_dummies(df)
 
  df = df.reindex(columns=cols_dummies, fill_value=0)

    # Create an anomalous flag column
  df['DAYS_EMPLOYED_ANOM'] = df["DAYS_EMPLOYED"] == 365243

  # Replace the anomalous values with nan
  df['DAYS_EMPLOYED'].replace({365243: np.nan}, inplace = True)

  df['CREDIT_INCOME_PERCENT'] = df['AMT_CREDIT'] / df['AMT_INCOME_TOTAL']
  df['ANNUITY_INCOME_PERCENT'] = df['AMT_ANNUITY'] / df['AMT_INCOME_TOTAL']
  df['CREDIT_TERM'] = df['AMT_ANNUITY'] / df['AMT_CREDIT']
  df['DAYS_EMPLOYED_PERCENT'] = df['DAYS_EMPLOYED'] / df['DAYS_BIRTH']


  df = df[cols_to_keep]



  df = imputer.transform(df)

 

  df = scaler.transform(df)
  
  return df 
