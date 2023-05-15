import unittest
import json
from API.Fonction_API import traitement
import lightgbm as lgb
import pandas as pd






class MyTest(unittest.TestCase):
    def test_prediction_good(self):
        model = lgb.Booster(model_file='API/my_model.txt')
        df = pd.read_csv('Streamlit/df.csv')
        df_pred = df.loc[df['SK_ID_CURR'] == 156685]
        df_dict = df_pred.to_dict()
        df = traitement(df_dict)
        y_pred = model.predict(df)
        y_pred = y_pred.reshape((-1, 1))
        expected_value = 0.217
        self.assertAlmostEqual(y_pred[0][0], expected_value, places=3)

    def test_prediction_bad(self):
        model = lgb.Booster(model_file='API/my_model.txt')
        df = pd.read_csv('Streamlit/df.csv')
        df_pred = df.loc[df['SK_ID_CURR'] == 389871]
        df_dict = df_pred.to_dict()
        df = traitement(df_dict)
        y_pred = model.predict(df)
        y_pred = y_pred.reshape((-1, 1))
        expected_value = 0.621
        self.assertAlmostEqual(y_pred[0][0], expected_value, places=3)


if __name__ == '__main__':
    unittest.main()
