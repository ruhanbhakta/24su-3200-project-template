import logging
import streamlit as st
from modules.nav import SideBarLinks
import requests

# Configure logging
logger = logging.getLogger(__name__)

SideBarLinks()

st.title('Server Load Page')

st.write('\n\n')

if st.button('View Server Load', 
             type = 'primary',
             use_container_width=True):
  results = requests.get('http://api:4000/sysadmin/db/server_load').json()
  st.dataframe(results)
