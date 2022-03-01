import streamlit as st
import pandas as pd
from random import randint

def app():
    df = pd.read_csv('./assets/Darknet.csv', on_bad_lines='skip')
    sites = ['Netflix', 'Youtube', 'Amazon', 'Yahoo', 'Medium', 'CBC', 'BBC', 'Fox News', 'Instagram', 'Ebay', 'Google Classroom', 'Facebook', \
        'Wikipedia']

    st.markdown('## Internet Traffic Surveillance')
    st.write('Internet traffic surveillance refers to the constant tracking of an individuals digital footprint (or online activites). \
        This footprint includes your social media consumption, your web browsing habits, and even your communication patterns.')
    st.sidebar.markdown('----')
    user_id = st.sidebar.slider('User Number (# ID)', 1, 250, value=10)
    if user_id >= 248:
        user_id = 248
    st.markdown('----')
    st.write(f'`Simulated data of 250 users being surveilled on a web platform`')

    st.write(f'**User number:** `{user_id}`')
    st.write(df.iloc[[user_id]].to_dict())
    st.write(df.iloc[[user_id]])

    st.markdown('## Analysis')
    first = sites[randint(0,12)]
    second = sites[randint(0,12)]
    third = sites[randint(0,12)]
    st.write(f'`Top Sites:` {first, second, third}')
    st.write(f'`Minutes Per Site (Daily):` {randint(1, 210), randint(1, 100), randint(1, 130)}')
    st.write(f'`Predicted Age:` {randint(16, 45)}')
