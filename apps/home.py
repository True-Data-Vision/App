import streamlit as st
from PIL import Image

def app():
    logo = Image.open('./assets/logo.png')
    col1, col2, col3 = st.columns([2,6,2])

    with col1:
        st.write("")

    with col2:
        st.image(logo)

    with col3:
        st.write("")

    st.markdown("""
    # Data Vision
    """)

    st.markdown('Welcome to the Data Vision App, an interactive sandbox where you can explore the tech behind internet surveillance.')

    st.markdown('----')
    st.markdown('## Scope')

    st.markdown('*Data Vision* is a Non-Governmental Organization fighting against data driven surveillance for civil liberties and digital rights. \
        This app hopes to bring awarness to the technologies behind internet surveillance so the general public becomes involved with the issue. \
        This app runs **simulations** of data tracking software but does not affect the users privacy as the data not been gathered from a real source (it\'s simply synthetic). \
        Visit the links below to view the organization\'s social media and other action pieces.')

    st.markdown('***Organization Links***')
    st.markdown("""
    - [Instagram](https://www.instagram.com/true.datavision/) 
    - [Petition w/ OpenMedia](https://action.openmedia.org/page/95077/petition/1)
    - [Github](https://github.com/True-Data-Vision)
    """)