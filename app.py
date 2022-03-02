import streamlit as st
from multipapp import MultiApp
from apps import home, geo, traffic, about

app = MultiApp()

st.set_page_config(page_title="Data Vision App", page_icon="⚫", layout='centered', initial_sidebar_state="expanded")

app.add_app("Home", home.app)
app.add_app("Geo Tracking Demo", geo.app)
app.add_app("Internet Traffic Demo", traffic.app)
app.add_app("About", about.app)

# The main app
app.run()