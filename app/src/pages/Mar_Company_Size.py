import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

# Display the appropriate sidebar links for the role of the logged-in user
SideBarLinks()

st.title('Job Postings by Company Size')

# Add a button to fetch and display the data
if st.button('Fetch Data', type='primary', use_container_width=True):
    try:
        # Fetch data from the API
        logger.info("Fetching data from the /marketing/companysizes endpoint.")
        response = requests.get('http://api:4000/marketing/companysizes')
        
        if response.status_code == 200:
            data = response.json()
            
            # Convert the data to a DataFrame
            df = pd.DataFrame(data)
            df.rename(columns={'CompanySize': 'Company Size', 'JobPostingsCount': 'Job Postings Count'}, inplace=True)
            
            # Display raw data
            st.subheader('Raw Data')
            st.dataframe(df)
            
            # Visualization: Bar Chart
            st.subheader('Bar Chart of Job Postings by Company Size')
            bar_chart = px.bar(df, x='Company Size', y='Job Postings Count',
                               title='Job Postings by Company Size',
                               labels={'Job Postings Count': 'Number of Job Postings', 'Company Size': 'Company Size'},
                               color='Company Size', text='Job Postings Count')
            st.plotly_chart(bar_chart, use_container_width=True)
            
            logger.info("Data successfully fetched and visualized.")
        else:
            st.error(f"Failed to fetch data. Status Code: {response.status_code}")
            logger.error(f"Error: {response.json()}")

    except Exception as e:
        st.error("An error occurred while fetching data.")
        logger.error(f"Exception occurred: {e}")
