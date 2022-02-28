import streamlit as st
from multipapp import MultiApp
from apps import home, geo, traffic
from PIL import Image

app = MultiApp()

st.set_page_config(page_title="Data Vision App", page_icon="⚫", layout='centered', initial_sidebar_state="expanded")

# logo = Image.open('./assests/logo.png')
# col1, col2, col3 = st.columns([2,6,2])

# with col1:
#     st.write("")

# with col2:
#     st.image(logo)

# with col3:
#     st.write("")

# st.markdown("""
# # Data Vision
# """)

# st.markdown('Welcome to the Data Vision App, an interactive sandbox where you can explore the tech behind internet surveillance.')

# st.markdown('----')

app.add_app("Home", home.app)
app.add_app("Geo Tracking", geo.app)
app.add_app("Internet Traffic", traffic.app)

# The main app
app.run()