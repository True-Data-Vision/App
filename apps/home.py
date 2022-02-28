import streamlit as st
from PIL import Image

def app():
    
    st.markdown('## Home')

    st.markdown('*Data Vision* is a Non-Governmental Organization fighting against data driven surveillance for civil liberties and digital rights. \
        This app hopes to bring awarness to the technologies behind internet surveillance such that the general public becomes involved with the issue. \
            Visit the links below to view the organization\'s social media and other action pieces.')

    st.caption('Organization Links')
    st.markdown("""
    - [Instagram](https://www.instagram.com/true.datavision/) 
    - [Petition w/ OpenMedia](https://action.openmedia.org/page/95077/petition/1)
    - [Github](https://github.com/True-Data-Vision)
    """)