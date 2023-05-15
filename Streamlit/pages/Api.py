import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.graph_objs as go
import json

st.set_page_config(
    page_title="Api",
    layout="wide",
)

st.markdown("# Pour Api")
st.sidebar.markdown("# Pour Api")


id_sk = st.session_state.df['SK_ID_CURR'].unique()

# display a dropdown menu with the unique values
selected_id = st.selectbox('Select an ID', id_sk)

# display the selected city
st.write('You selected:', selected_id)


if 'key' not in st.session_state:
    st.session_state['key'] = selected_id

# Session State also supports attribute based syntax
if 'key' in st.session_state:
    st.session_state.key = selected_id


df_pred = st.session_state.df.loc[st.session_state.df['SK_ID_CURR'] ==  selected_id]

url = 'https://api-open-classroom.herokuapp.com/prediction'
headers = {'Content-Type': 'application/json'}

df_dict = df_pred.to_dict()
data_json = json.dumps(df_dict)
b = requests.post(url, headers=headers, data=data_json)



if 'key' in st.session_state:
    st.session_state.key = selected_id

value = b.json()
value = value['prediction'][0][0]


fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = value,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Note", 'font': {'size': 24}},
    delta = {'reference': 1, 'increasing': {'color': "RebeccaPurple"}},
    gauge = {
        'axis': {'range': [None, 1], 'tickwidth': 1, 'tickcolor': "blue"},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 0.404], 'color': 'green'},
            {'range': [0.405, 1], 'color': 'red'}],
        'threshold': {
            'line': {'color': "black", 'width': 5},
            'thickness': 0.75,
            'value': 0.405}}))

fig.update_layout(paper_bgcolor = "lavender", font = {'color': "black", 'family': "Arial"})


# Créez une colonne centrale dans Streamlit
col1, col2, col3 = st.columns([1, 3, 1])

# Placez un espace vide dans la colonne de gauche pour centrer la figure
with col1:
    st.write("")

# Placez la figure dans la colonne centrale
with col2:
      st.plotly_chart(fig)
  

# Placez un autre espace vide dans la colonne de droite pour centrer la figure
with col3:
    st.write("")

