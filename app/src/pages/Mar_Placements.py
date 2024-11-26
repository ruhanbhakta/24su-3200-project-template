import logging
import streamlit as st
from modules.nav import SideBarLinks
import requests

# Configure logging
logger = logging.getLogger(__name__)

# Streamlit page configuration
st.set_page_config(
    page_title="Applications Overview",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add custom CSS for styling
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
        <h1>📊 Applications Overview Dashboard</h1>
        <p>Get a quick summary of application data and insights.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Define API endpoints
ACCEPTED_APPS_API = 'http://api:4000/marketing/acceptedapps'
TOTAL_APPS_API = 'http://api:4000/marketing/totalapps'

# Create a two-column layout
col1, col2 = st.columns(2, gap="large")

# Accepted Applications Section
with col1:
    st.header("✔️ Accepted Applications")
    if st.button("Fetch Accepted Applications", type="primary", key="accepted_btn"):
        try:
            logger.info("Fetching data from the /marketing/acceptedapps endpoint.")
            response = requests.get(ACCEPTED_APPS_API)
            if response.status_code == 200:
                data = response.json()
                total_accepted = data[0]['TotalAcceptances'] if data else 0
                # Display the result with a styled box
                st.markdown(
                    f"""
                    <div class="metric-box">
                        <h3>Total Accepted Applications</h3>
                        <h1 style="color: #6a11cb;">{total_accepted}</h1>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                logger.info(f"Total Accepted Applications: {total_accepted}")
            else:
                st.error(f"Failed to fetch data. Status Code: {response.status_code}")
                logger.error(f"Error: {response.json()}")
        except Exception as e:
            st.error("An error occurred while fetching accepted applications data.")
            logger.error(f"Exception occurred: {e}")

# Total Applications Section
with col2:
    st.header("📥 Total Applications")
    if st.button("Fetch Total Applications", type="primary", key="total_btn"):
        try:
            logger.info("Fetching data from the /marketing/totalapps endpoint.")
            response = requests.get(TOTAL_APPS_API)
            if response.status_code == 200:
                data = response.json()
                total_apps = data[0]['TotalApplications'] if data else 0
                # Display the result with a styled box
                st.markdown(
                    f"""
                    <div class="metric-box">
                        <h3>Total Applications</h3>
                        <h1 style="color: #2575fc;">{total_apps}</h1>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                logger.info(f"Total Applications: {total_apps}")
            else:
                st.error(f"Failed to fetch data. Status Code: {response.status_code}")
                logger.error(f"Error: {response.json()}")
        except Exception as e:
            st.error("An error occurred while fetching total applications data.")
            logger.error(f"Exception occurred: {e}")
