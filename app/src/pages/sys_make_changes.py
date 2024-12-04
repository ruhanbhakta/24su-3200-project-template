import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)

from modules.nav import SideBarLinks
# Configure logging
logger = logging.getLogger(__name__)

SideBarLinks()

# Base URL of the Flask application (updated to http://api:4000/sysadmin)
BASE_URL = "http://api:4000/sysadmin"  
# Function to call the `/students/<student_id>/update_major` route (PUT)
def update_student_major(student_id, new_major):
    response = requests.put(
        f"{BASE_URL}/students/{student_id}/update_major", 
        json={"major": new_major}
    )
    return response.json()

# Function to call the `/skills/add` route (POST)
def add_skill(skill_name):
    response = requests.post(
        f"{BASE_URL}/skills/add", 
        json={"name": skill_name}
    )
    return response.json()

# Function to call the `/job_postings/<job_id>/delete` route (DELETE)
def delete_alumni(id):
    response = requests.delete(f"{BASE_URL}/job_postings/{id}/delete")
    return response.json()

# Streamlit UI
st.title("System Administrator Dashboard - Manage Data")

# Section 1: Update Student Major
st.header("Update Student Major")
student_id = st.number_input("Enter Student ID", min_value=1, step=1)
new_major = st.text_input("Enter New Major")
if st.button("Update Major"):
    if student_id and new_major:
        result = update_student_major(student_id, new_major)
        st.json(result)

# Section 2: Add a New Skill
st.header("Add a New Skill")
new_skill = st.text_input("Enter Skill Name")
if st.button("Add Skill"):
    if new_skill:
        result = add_skill(new_skill)
        st.json(result)

# Section 3: Delete Job Posting
st.header("Delete Alumni")
alumniId = st.number_input("Enter AlumniID", min_value=1, step=1)
if st.button("Delete Alum from Database"):
    if alumniId:
        result = delete_alumni(alumniId)
        st.json(result)
