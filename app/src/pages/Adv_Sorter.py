import logging
import streamlit as st
from modules.nav import SideBarLinks
import requests

# Configure logging
logger = logging.getLogger(__name__)

# Streamlit page configuration
st.set_page_config(
    page_title="Student Skill Sorter",
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
        <h1>🔁 Student Skill Sorter</h1>
        <p>Sort students by their unique skill counts.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Define API endpoint
STUDENT_SORTER_API = 'http://api:4000/advisor/sorter'

# Fetch and display data
if st.button("Fetch Sorted Students", type="primary", key="fetch_sorter_btn"):
    try:
        logger.info("Fetching data from the /advisor/sorter endpoint.")
        response = requests.get(STUDENT_SORTER_API)
        if response.status_code == 200:
            data = response.json()
            if data:
                # Display as a table
                st.subheader("Students Sorted by Skills")
                st.table(data) 
                logger.info("Data successfully displayed as a table.")
            else:
                st.warning("No data available.")
                logger.warning("API returned no data.")
        else:
            st.error(f"Failed to fetch data. Status Code: {response.status_code}")
            logger.error(f"Error fetching data: {response.json()}")
    except Exception as e:
        st.error("An error occurred while fetching student data.")
        logger.error(f"Exception occurred: {e}")
