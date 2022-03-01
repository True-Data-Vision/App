import streamlit as st
import pandas as pd

def app():
    st.markdown('## Internet Traffic Surveillance')
    st.write('Internet traffic surveillance refers to the constant tracking of an individuals digital footprint (or online activites). \
        This footprint includes your social media consumption, your web browsing habits, and even your communication patterns.')

    df = pd.read_csv('./assets/Darknet.csv', on_bad_lines='skip')
    st.write(df)