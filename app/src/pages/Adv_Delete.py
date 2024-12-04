import streamlit as st
import requests
import logging

logger = logging.getLogger(__name__)

from modules.nav import SideBarLinks

# Configure logging
logger = logging.getLogger(__name__)

SideBarLinks()

# Base URL of the Flask application 
BASE_URL = "http://api:4000/advisor"

def delete_job(id):
    # Adjusted URL to remove redundant 'delete' in the path
    response = requests.delete(f"{BASE_URL}/jobposting/{id}")
    
    # Check for successful deletion and handle the response
    if response.status_code == 200:
        return response.json()  # Return JSON response if deletion is successful
    else:
        return {"error": "Failed to delete job", "status_code": response.status_code}

st.title("Job Posting Management")

st.header("Delete Job Posting")
alumniId = st.number_input("Enter JobID", min_value=1, step=1)
if st.button("Delete Job from Database"):
    if alumniId:
        result = delete_job(alumniId)
        st.json(result)
