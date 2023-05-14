import streamlit as st
import pandas as pd

import streamlit as st

st.set_page_config(
    page_title="Banque",
    layout="wide",
)

st.markdown("# Base de données avec filtre")
st.sidebar.markdown("# Base de données avec filtre")


st.write("# Votre base de données")
df = pd.read_csv('Streamlit/df.csv')
df['Age'] = round(df['DAYS_BIRTH'] / 365).abs()
df['CREDIT_INCOME_PERCENT'] = df['AMT_CREDIT'] / df['AMT_INCOME_TOTAL']
df['ANNUITY_INCOME_PERCENT'] = df['AMT_ANNUITY'] / df['AMT_INCOME_TOTAL']
df['CREDIT_TERM'] = df['AMT_ANNUITY'] / df['AMT_CREDIT']
df['DAYS_EMPLOYED_PERCENT'] = df['DAYS_EMPLOYED'] / df['DAYS_BIRTH']



if 'df' not in st.session_state:
    # Save the data to session state
    st.session_state.df = df

# Charger les données dans un DataFrame


# Définir les options de filtrage
options = {
    'CODE_GENDER': ['M', 'F'],
    'Age': list(df['Age'].unique()),
    'NAME_CONTRACT_TYPE': list(df['NAME_CONTRACT_TYPE'].unique())
}

# Afficher les éléments de filtrage
with st.container():
    
    # Diviser l'espace horizontal en trois colonnes
    col1, col2, col3 = st.columns(3)
    
    # Ajouter les select box dans la première colonne
    with col1:
        selected_option1 = st.selectbox('Sélectionner Genre', options['CODE_GENDER'])
    
    with col2:
        selected_option2 = st.selectbox('Sélectionner Age', options['Age'])
    
    # Ajouter le slider dans la troisième colonne
    with col3:
        selected_option3 = st.selectbox('Sélectionner Type de contrat', options['NAME_CONTRACT_TYPE'])
        
# Filtrer les données en fonction des options sélectionnées
filtered_df = df[(df['CODE_GENDER'] == selected_option1) & (df['Age'] == selected_option2) & (df['NAME_CONTRACT_TYPE'] == selected_option3)]

# Afficher le DataFrame filtré
st.dataframe(filtered_df.head(300))
