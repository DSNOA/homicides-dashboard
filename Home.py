import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Unsolved Murders",
    page_icon="😨",
)
st.title('Unsolved Murders in 55 Cities Over The Past Decade')


@st.cache_data
def load_data(nrows):
    data = pd.read_csv('../data/homicide.csv', nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data


data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# st.image('images/covid-icon.png')

# display the link to that page.
st.write('<a href="/Charts"> Check out charts</a>', unsafe_allow_html=True)
