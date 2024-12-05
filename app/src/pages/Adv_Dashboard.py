import logging
import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd
import plotly.express as px

# Configure logging
logger = logging.getLogger(__name__)

# Streamlit page configuration
st.set_page_config(
    page_title="Advisor Dashboard",
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
    .stDataFrame {
        margin-top: 20px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
        padding: 15px;
    }
    .metric-box {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .metric-box h3 {
        color: #6a11cb;
        margin-bottom: 10px;
    }
    .plotly-chart {
        margin-top: 20px;
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
        <h1>📈 Student Dashboard</h1>
        <p>View student application data!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Add a button to fetch and display the data
if st.button('Fetch Data', type='primary', use_container_width=True):
    try:
        # Fetch data from the API
        logger.info("Fetching data from the /advisor/studentdasboard endpoint.")
        response = requests.get('http://api:4000/advisor/studentdashboard')
        
        if response.status_code == 200:
            data = response.json()
            
            # Convert the data to a DataFrame
            df = pd.DataFrame(data)
            df.rename(columns={'CompanySize': 'Company Size', 'JobPostingsCount': 'Job Postings Count'}, inplace=True)
            
            # Display raw data in a styled table
            st.subheader('Raw Data')
            st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error("An error occurred while fetching data.")
        logger.error(f"Exception occurred: {e}")
