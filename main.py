import streamlit as st
import seaborn as sns
import pandas as pd

df=sns.load_dataset('tips')
st.dataframe(df)
@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')
v=convert_df(df)

st.download_button(label='download_button',data=v, file_name='tips_dat')

Name = st.radio(
     "Which Sem are you in now?",
     ('BADS','DS','Excel'))

if Name == 'BADS':
     st.write('You are in 3rd Sem BADS')
else:
     st.write("You are not enrolled")


agree = st.checkbox('I agree')
if agree:
     st.write('Great!')

import datetime
d = st.date_input(
     "When's your birthday",
     datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)