import streamlit as st
import requests
import logging
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

BASE_URL = "http://api:4000/student"

# Add employer review
def add_employer_review(employer_id, review):
    """
    Sends a POST request to add a new employer review.
    """
    try:
        response = requests.post(
            f"{BASE_URL}/add_employer_review",
            json={
                "employerId": employer_id,
                "review": review
            }
        )
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error while adding employer review: {e}")
        return {"error": "Failed to connect to the server"}
    
    SideBarLinks()

    # Page Title
st.title("Employer Reviews Dashboard")

# Section: Add a New Employer Review
st.header("Add a New Employer Review")

# Input Fields
employer_id = st.number_input("Employer ID", min_value=1, step=1)
review = st.text_area("Review Text")

# Button to Submit Review
if st.button("Add Review"):
    if employer_id and review.strip():
        result = add_employer_review(employer_id, review)
        if "error" in result:
            st.error(result["error"])
        else:
            st.success("Review added successfully!")
            st.json(result)
    else:
        st.error("Please fill in all fields.")

#