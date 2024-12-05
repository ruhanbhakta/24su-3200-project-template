import logging
import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd

# Configure logging
logger = logging.getLogger(__name__)

# Streamlit page configuration
st.set_page_config(
    page_title="Employer Data Insights",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main-header {
        background: linear-gradient(90deg, #6a11cb, #2575fc);
        color: white;
        padding: 20px;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .stButton button {
        background-color: #007BFF;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 8px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 15px rgba(0, 123, 255, 0.3);
    }
    .data-section {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    .data-section h3 {
        color: #6a11cb;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
SideBarLinks()

# Main Header
st.markdown(
    """
    <div class="main-header">
        <h1>📊 Employer Data Insights</h1>
        <p>Explore top companies by alumni count and co-op applications.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Define API endpoints
ALUMNI_COUNT_API = 'http://api:4000/marketing/alumnicount'
COOP_COUNT_API = 'http://api:4000/marketing/coopcount'


col1, col2 = st.columns(2, gap="large")

# Alumni Count Section
with col1:
    st.header("🎓 Top Companies by Alumni Count")
    if st.button("Fetch Alumni Count Data", type="primary", key="alumni_btn"):
        try:
            logger.info("Fetching data from the /marketing/alumnicount endpoint.")
            response = requests.get(ALUMNI_COUNT_API)
            
            if response.status_code == 200:
                data = response.json()
                
                # Convert to DataFrame
                df = pd.DataFrame(data)
                df.rename(columns={'EmployerName': 'Employer Name', 'AlumniCount': 'Alumni Count'}, inplace=True)
                
                # Display data in a styled table
                st.markdown(
                    """
                    <div class="data-section">
                        <h3>Alumni Count Data</h3>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.dataframe(df, use_container_width=True)
                
                logger.info("Alumni data successfully fetched and displayed.")
            else:
                st.error(f"Failed to fetch data. Status Code: {response.status_code}")
                logger.error(f"Error: {response.json()}")

        except Exception as e:
            st.error("An error occurred while fetching alumni count data.")
            logger.error(f"Exception occurred: {e}")

# Co-op Count Section
with col2:
    st.header("💼 Top Companies by Co-op Applications")
    if st.button("Fetch Popular Companies", type="primary", key="coop_btn"):
        try:
            logger.info("Fetching data from the /marketing/coopcount endpoint.")
            response = requests.get(COOP_COUNT_API)
            
            if response.status_code == 200:
                data = response.json()
                
                # Convert to DataFrame
                df = pd.DataFrame(data)
                df.rename(columns={'EmployerName': 'Employer Name', 'CoopCount': 'Co-op Applications'}, inplace=True)
                
                
                st.markdown(
                    """
                    <div class="data-section">
                        <h3>Co-op Applications Data</h3>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.dataframe(df, use_container_width=True)
                
                logger.info("Co-op data successfully fetched and displayed.")
            else:
                st.error(f"Failed to fetch data. Status Code: {response.status_code}")
                logger.error(f"Error: {response.json()}")

        except Exception as e:
            st.error("An error occurred while fetching co-op count data.")
            logger.error(f"Exception occurred: {e}")
