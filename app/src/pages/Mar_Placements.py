import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd

st.set_page_config(layout='wide')

# Display the appropriate sidebar links for the role of the logged-in user
SideBarLinks()

st.title('Applications Overview')

# Define API endpoints
ACCEPTED_APPS_API = 'http://api:4000/marketing/acceptedapps'
TOTAL_APPS_API = 'http://api:4000/marketing/totalapps'

# Create a two-column layout
col1, col2 = st.columns(2)

# Accepted Applications Section
with col1:
    st.header('Accepted Applications')
    if st.button('Fetch Accepted Applications Count', type='primary', key='accepted_btn'):
        try:
            logger.info("Fetching data from the /marketing/acceptedapps endpoint.")
            response = requests.get(ACCEPTED_APPS_API)
            
            if response.status_code == 200:
                data = response.json()
                total_accepted = data[0]['TotalAcceptances'] if data else 0
                
                # Display the result
                st.subheader('Total Accepted Applications')
                st.metric(label="Accepted Applications", value=total_accepted)
                
                logger.info(f"Total Accepted Applications: {total_accepted}")
            else:
                st.error(f"Failed to fetch data. Status Code: {response.status_code}")
                logger.error(f"Error: {response.json()}")

        except Exception as e:
            st.error("An error occurred while fetching accepted applications data.")
            logger.error(f"Exception occurred: {e}")

# Total Applications Section
with col2:
    st.header('Total Applications')
    if st.button('Fetch Total Applications Count', type='primary', key='total_btn'):
        try:
            logger.info("Fetching data from the /marketing/totalapps endpoint.")
            response = requests.get(TOTAL_APPS_API)
            
            if response.status_code == 200:
                data = response.json()
                total_apps = data[0]['TotalApplications'] if data else 0
                
                # Display the result
                st.subheader('Total Applications')
                st.metric(label="Total Applications", value=total_apps)
                
                logger.info(f"Total Applications: {total_apps}")
            else:
                st.error(f"Failed to fetch data. Status Code: {response.status_code}")
                logger.error(f"Error: {response.json()}")

        except Exception as e:
            st.error("An error occurred while fetching total applications data.")
            logger.error(f"Exception occurred: {e}")
