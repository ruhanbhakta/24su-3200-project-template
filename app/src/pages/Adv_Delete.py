import streamlit as st
import requests
import logging
from modules.nav import SideBarLinks

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO) 

# Initialize sidebar navigation
SideBarLinks()

# Base URL
BASE_URL = "http://api:4000/advisor" 

def delete_job(job_id):
    """
    Send a DELETE request to the Flask API to delete a job posting.
    """
    try:
        response = requests.delete(f"{BASE_URL}/jobposting/{int(job_id)}")
        
        # Handle the response
        if response.status_code == 200:
            return response.json()  # Successful deletion
        else:
            return {
                "error": "Failed to delete job",
                "status_code": response.status_code,
                "details": response.text,
            }
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        return {"error": "Unable to connect to the server"}

# Streamlit UI
st.header("Delete Job")

# Input field for job ID
job_id = st.number_input("Enter Job ID", min_value=1, step=1, format="%d") 
# Button to trigger deletion
if st.button("Delete Job from Database"):
    if job_id > 0:
        result = delete_job(int(job_id))
        st.json(result)
    else:
        st.error("Please enter a valid Job ID.")
