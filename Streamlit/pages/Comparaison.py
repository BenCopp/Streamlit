import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Charger les données dans un DataFrame
#df = pd.read_csv('/content/drive/MyDrive/OpenClassroom/Projet7/Streamlot/df.csv')


st.set_page_config(
    page_title="Comparaison",
    layout="wide",
)

st.markdown("# Comparaison")
st.sidebar.markdown("# Comparaison")



fig = plt.figure(figsize = (5, 3))
# KDE plot of loans that were repaid on time
ax = sns.kdeplot(st.session_state.df.loc[st.session_state.df['TARGET'] == 0, 'DAYS_BIRTH'].abs() / 365, label = 'target == Bon client')
# KDE plot of loans which were not repaid on time
ax = sns.kdeplot(st.session_state.df.loc[st.session_state.df['TARGET'] == 1, 'DAYS_BIRTH'].abs() / 365, label = 'target == Mauvais Client')
ax.axvline(x = st.session_state.df.loc[st.session_state.df['SK_ID_CURR']==  st.session_state.key, 'DAYS_BIRTH'].values[0]/365*-1,    
           ymin = 0, 
           ymax = 1
           )
plt.legend(loc="upper right")
plt.xlabel('Age (years)'); plt.ylabel('Density'); plt.title('Distribution of Ages');




grig= plt.figure(figsize = (5, 3))
fx = sns.histplot(data=st.session_state.df, x="FLAG_OWN_CAR", hue="TARGET", multiple="dodge", stat="percent", common_norm=False,  shrink=0.8)
fx.axvline(x = st.session_state.df.loc[st.session_state.df['SK_ID_CURR']==  st.session_state.key,  'FLAG_OWN_CAR'].values[0],    
           ymin = 0, 
           ymax = 20,
           color= 'r'
           )
plt.legend(loc="upper right")
plt.xlabel('FLAG_OWN_CAR'); plt.ylabel('Density'); plt.title('Distribution of FLAG_OWN_CAR');


gig = plt.figure(figsize = (5, 3))
fx = sns.kdeplot(st.session_state.df.loc[st.session_state.df['TARGET'] == 0, 'CREDIT_INCOME_PERCENT'], label = 'target == Bon client')
fx = sns.kdeplot(st.session_state.df.loc[st.session_state.df['TARGET'] == 1, 'CREDIT_INCOME_PERCENT'], label = 'target == Mauvais client')
fx.axvline(x = st.session_state.df.loc[st.session_state.df['SK_ID_CURR']==  st.session_state.key, 'CREDIT_INCOME_PERCENT'].values[0],    
           ymin = 0, 
           ymax = 1
           )
plt.xlim((0,15))
plt.legend(loc="upper right")
plt.xlabel('CREDIT_INCOME_PERCENT'); plt.ylabel('Density'); plt.title('Distribution of CREDIT_INCOME_PERCENT');



histplot_child = plt.figure(figsize = (5, 3))
px = sns.histplot(data=st.session_state.df, x="CNT_CHILDREN", hue="TARGET", multiple="dodge", stat="percent", common_norm=False, binwidth=0.5)
px.set_xlim(0, 4)
px.axvline(x = st.session_state.df.loc[st.session_state.df['SK_ID_CURR']==  st.session_state.key,  'CNT_CHILDREN'].values[0],    
           ymin = 0, 
           ymax = 20,
           color= 'r'
           )


plt.xticks([0,1, 2, 3, 4])
plt.legend(loc="upper right")
plt.xlabel('CNT_CHILDREN'); plt.ylabel('Density'); plt.title('Distribution of Children');



histplot_withp= plt.figure(figsize = (5, 3))
gb = sns.histplot(data=st.session_state.df, x="REGION_RATING_CLIENT", hue="TARGET", multiple="dodge", stat="percent", common_norm=False)
gb.axvline(x = st.session_state.df.loc[st.session_state.df['SK_ID_CURR']==  st.session_state.key,  'REGION_RATING_CLIENT'].values[0],    
           ymin = 0, 
           ymax = 20,
           color= 'r'
           )
plt.xticks([1, 2, 3])
plt.legend(loc="upper right")
plt.xlabel('Region Rating'); plt.ylabel('Density'); plt.title('Distribution of Region Rating');





col1, col2, col3= st.columns(3)

with col1:
    st.pyplot(fig)

with col2:
    st.pyplot(grig)

with col3:
    st.pyplot(gig)

col1, col2= st.columns(2)

with col1:
    st.pyplot(histplot_child)

with col2:
    st.pyplot(histplot_withp)
