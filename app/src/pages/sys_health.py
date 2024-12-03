import logging
import streamlit as st
from modules.nav import SideBarLinks
import requests

# Configure logging
logger = logging.getLogger(__name__)

SideBarLinks()

st.title('Systeam Health Page')

st.write('\n\n')
st.write('## System Health Insights')

if st.button('Get Number of Active Connections', 
             type = 'primary',
             use_container_width=True):
  results = requests.get('http://api:4000/sysadmin/db/health').json()
  st.dataframe(results)
