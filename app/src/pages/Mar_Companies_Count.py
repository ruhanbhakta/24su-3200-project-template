import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd

st.set_page_config(layout='wide')

# Display the appropriate sidebar links for the role of the logged-in user
SideBarLinks()

st.title('Employer Data Insights')

# Define endpoints
ALUMNI_COUNT_API = 'http://api:4000/marketing/alumnicount'
COOP_COUNT_API = 'http://api:4000/marketing/coopcount'

# Create a 2-column layout for alumni and co-op data
col1, col2 = st.columns(2)

# Alumni Count Section
with col1:
    st.header('Top Companies by Alumni Count')
    if st.button('Fetch Alumni Count Data', type='primary', key='alumni_btn'):
        try:
            logger.info("Fetching data from the /marketing/alumnicount endpoint.")
            response = requests.get(ALUMNI_COUNT_API)
            
            if response.status_code == 200:
                data = response.json()
                
                # Convert to DataFrame
                df = pd.DataFrame(data)
                df.rename(columns={'EmployerName': 'Employer Name', 'AlumniCount': 'Alumni Count'}, inplace=True)
                
                # Display data in a table
                st.subheader('Alumni Count Data')
                st.table(df)
                
                logger.info("Alumni data successfully fetched and displayed.")
            else:
                st.error(f"Failed to fetch data. Status Code: {response.status_code}")
                logger.error(f"Error: {response.json()}")

        except Exception as e:
            st.error("An error occurred while fetching alumni count data.")
            logger.error(f"Exception occurred: {e}")

# Co-op Count Section
with col2:
    st.header('Top Companies by Co-op Applications')
    if st.button('Fetch Co-op Count Data', type='primary', key='coop_btn'):
        try:
            logger.info("Fetching data from the /marketing/coopcount endpoint.")
            response = requests.get(COOP_COUNT_API)
            
            if response.status_code == 200:
                data = response.json()
                
                # Convert to DataFrame
                df = pd.DataFrame(data)
                df.rename(columns={'EmployerName': 'Employer Name', 'CoopCount': 'Co-op Applications'}, inplace=True)
                
                # Display data in a table
                st.subheader('Co-op Applications Data')
                st.table(df)
                
                logger.info("Co-op data successfully fetched and displayed.")
            else:
                st.error(f"Failed to fetch data. Status Code: {response.status_code}")
                logger.error(f"Error: {response.json()}")

        except Exception as e:
            st.error("An error occurred while fetching co-op count data.")
            logger.error(f"Exception occurred: {e}")
