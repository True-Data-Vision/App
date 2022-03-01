import streamlit as st
import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim

def app():
    st.markdown('## Geo-Location Surveillance')
    st.write('Geolocation refers to the use of location technologies including GPS or IP addresses to identify and track the whereabouts of devices. These devices are carried on an individual\'s \
        person, as a result, geolocation is used in mass surveillance to track the movements and location of people.')

    st.sidebar.markdown('----')
    data_count = st.sidebar.slider('Data Count', 1, 100, value=10)
    st.markdown('----')
    st.write('`Simulated location data of a citizen in the Greater Toronto Area`')
    df = pd.DataFrame(np.random.randn(data_count, 2) / [50, 50] + [43.6411414,-79.7887964],
    columns=['lat', 'lon'])
    st.map(df)
    # st.write(df)
    st.markdown('## Analysis')
    col1, col2,  = st.columns([2,3])
    with col1:
        st.write(df)
    with col2:
        geolocator = Nominatim(user_agent="http")
        location = geolocator.reverse(f"{df.lat.max()}, {df.lon.min()}")
        st.write(f'`Predicted Central Location:` {location.address}')
        
        st.write(f'`Central Latitude:` {df.lat.mean()}')
        st.write(f'`Central Longitude:` {df.lon.mean()}')

    st.markdown('## Outcome')
    st.write('This geo-location data is compiled alongside your digital footprint to determine where you went (institutions, facilities, community centers) \
        , what you did (leisure, work, commerce), and its association with your psychographic profile. Through this type of surveillance, corporations \
            and governments can determine your daily routine to nearest second and how it correlates to your tracked information.')

