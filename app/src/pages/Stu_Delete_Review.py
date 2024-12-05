import streamlit as st
import requests
import logging
from modules.nav import SideBarLinks

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)  # Ensure proper logging configuration

# Initialize sidebar navigation
SideBarLinks()

# Base URL of the Flask application
BASE_URL = "http://api:4000/student"  # Update this to match your API's actual base URL

def delete_review(review_id):
    """
    Send a DELETE request to the Flask API to delete a review.
    """
    try:
        response = requests.delete(f"{BASE_URL}/delete_student_review", json={"reviewId": int(review_id)})
        
        # Handle the response
        if response.status_code == 200:
            return response.json()  # Successful deletion
        else:
            return {
                "error": "Failed to delete review",
                "status_code": response.status_code,
                "details": response.text,
            }
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        return {"error": "Unable to connect to the server"}

# Streamlit UI
st.header("Delete Student Review")

# Input field for review ID
review_id = st.number_input("Enter Review ID", min_value=1, step=1, format="%d")  # Forces integer display

# Button to trigger deletion
if st.button("Delete Review from Database"):
    if review_id > 0:
        result = delete_review(int(review_id))  # Explicitly convert to integer
        st.json(result)
    else:
        st.error("Please enter a valid Review ID.")
