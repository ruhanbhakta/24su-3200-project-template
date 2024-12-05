import streamlit as st
import requests
import logging

logger = logging.getLogger(__name__)

from modules.nav import SideBarLinks

# Configure logging
logger = logging.getLogger(__name__)

SideBarLinks()

# Base URL
BASE_URL = "http://api:4000/advisor"

# Function to call the `/add_advisor` route (POST)
def add_advisor(first_name, last_name, email):
    response = requests.post(
        f"{BASE_URL}/add_advisor",
        json={
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    )
    return response.json()

# Streamlit UI
st.title("Advisor Management Dashboard")

# Section: Add a New Advisor
st.header("Add a New Advisor")

# Input fields for advisor information
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
email = st.text_input("Email")

if st.button("Add Advisor"):
    if first_name and last_name and email:
        result = add_advisor(first_name, last_name, email)
        st.json(result)
    else:
        st.error("Please fill in all fields")
