import logging
import streamlit as st
from modules.nav import SideBarLinks
import requests

# Configure logging
logger = logging.getLogger(__name__)

SideBarLinks()

st.title('Connection Limit')

st.write('\n\n')
st.write('## Current Connection Limit')

if st.button('Get Number of Allowed Connections', 
             type = 'primary',
             use_container_width=True):
  results = requests.get('http://api:4000/sysadmin/db/connection_limit').json()
  st.dataframe(results)
