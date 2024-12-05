# Import required libraries
import logging
import streamlit as st
from modules.nav import SideBarLinks

# Set up logging configuration
logging.basicConfig(
    format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Streamlit configuration
st.set_page_config(
    page_title="FreshMeet - Valuable Co-op Insights",
    page_icon=":mortar_board:",
    layout="wide"
)

# Initialize session state for authentication
st.session_state['authenticated'] = False

# Configure sidebar links
# Ensure 'src/.streamlit/config.toml' sets [client] showSidebarNavigation = false
SideBarLinks(show_home=True)

# ***************************************************
#                   Page Content
# ***************************************************

# Add a visually appealing banner at the top
st.markdown(
    """
    <style>
    .banner {
        background-color: #f4f4f9;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-family: Arial, sans-serif;
    }
    .banner h1 {
        color: #4A90E2;
        margin: 0;
        font-size: 2.5em;
    }
    .banner p {
        color: #6c757d;
        margin: 0;
        font-size: 1.2em;
    }
    </style>
    <div class="banner">
        <h1>FreshMeet</h1>
        <p>Your Gateway to Valuable Co-op Insights</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Page introduction
st.write('\n\n')
st.write('<h3 style="text-align: center;">Hi! Who would you like to log in as?</h3>', unsafe_allow_html=True)
st.write('\n')

# Define a function to handle user role selection
def authenticate_user(role, page_path, role_description):
    """Authenticate and redirect to a specific page based on the role."""
    st.session_state['authenticated'] = True
    st.session_state['role'] = role
    logger.info(f"Logging in as {role_description}")
    st.switch_page(page_path)

# Create buttons in a grid layout for better visual appeal
cols = st.columns(2)  # Create two columns for buttons

roles = [
    ('Student', 'student', 'pages/Student_Home.py', 'Student'),
    ('Co-op Advisor', 'coop_advisor', 'pages/Advisor_Home.py', 'Co-op Advisor'),
    ('Marketing Analyst', 'marketing_analyst', 'pages/Marketing_Analyst_Home.py', 'Marketing Analyst'),
    ('System Admin', 'sysadmin', 'pages/Sysadmin_Home.py', 'System Admin')
]

# Display buttons
for i, (button_label, role, page, role_desc) in enumerate(roles):
    col = cols[i % 2]  # Alternate columns for buttons
    with col:
        if st.button(button_label, type='primary', use_container_width=True):
            authenticate_user(role, page, role_desc)
