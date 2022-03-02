import streamlit as st
import pandas as pd
from random import randint

def app():
    df = pd.read_csv('./assets/Darknet.csv', on_bad_lines='skip')
    sites = ['Netflix', 'Youtube', 'Amazon', 'Yahoo', 'Medium', 'CBC', 'BBC', 'Fox News', 'Instagram', 'Ebay', 'Google Classroom', 'Facebook', \
        'Wikipedia']
    attitude = ['Positive', 'Negative', 'Neutral']
    domain_of_interest = ['Sports', 'Technology', 'Literature', 'Politics', 'Education', 'Psychology' \
        , 'Travel']

    st.markdown('## Internet Traffic Surveillance')
    st.write('Internet traffic surveillance refers to the constant tracking of an individuals digital footprint (or online activites). \
        This footprint includes your social media consumption, your web browsing habits, and even your communication patterns. \
        These forms of data can be put together to form a psychographic profile through the use of segementation algorithms, they essentially connect \
            multiple data points to paint a narrative about you and what you represent.')
    st.sidebar.markdown('----')
    user_id = st.sidebar.slider('User Number (# ID)', 1, 250, value=10)
    if user_id >= 248:
        user_id = 248
    st.markdown('----')
    st.write(f'`Simulated data of 250 users being surveilled on a web platform`')

    st.write(f'**User number:** `{user_id}`')
    st.markdown('## Analysis')
    first = sites[randint(0,12)]
    second = sites[randint(0,12)]
    third = sites[randint(0,12)]
    st.write(f'`Top Sites:` {first, second, third}')
    st.write(f'`Minutes Per Site (Daily):` {randint(45, 210), randint(45, 100), randint(45, 130)}')
    st.write(f'`Predicted Age:` {randint(16, 45)}')
    st.write(f'`Digital Attitude:` {attitude[randint(0, 2)]}')
    st.write(f'`Domain of Interest:` {domain_of_interest[randint(0, 6)]}')

    st.markdown('----')
    st.write('Raw data:')
    st.write(df.iloc[[user_id]].to_dict())
    st.write(df.iloc[[user_id]])

    st.markdown('----')
    st.write('## Outcome')
    st.write('This data surrounding your web footprint is extremely valuable as corporations can construct \
        extensive psychographic profiles (determine your beliefs, values, lifestyle, social status, opinions and activities). \
        This intelligence pipeline unethically invades our privacy; even though our information is not directly given to corporations, \
        algorithms are capable of connecting the dots and compiling large amounts of data through segmentation and analysis. ')




