import streamlit as st
import requests

# Base URL for your Flask backend
BASE_URL = "http://api:4000/advisor"  

# Function to update student's advisor ID
def update_student_advisor(student_id, advisor_id):
    response = requests.put(
        f"{BASE_URL}/student/{student_id}/advisor", 
        json={"advisorId": advisor_id}
    )
    return response.json()

# Streamlit app interface
st.title("Update Student's Advisor")

# Collecting student details using text inputs
student_id = st.number_input("Student ID", min_value=1, step=1)
advisor_id = st.number_input("New Advisor ID", min_value=1, step=1)

# Button to submit the data
if st.button("Update Advisor"):
    if student_id and advisor_id:
        
        result = update_student_advisor(student_id, advisor_id)
        
        # Show the result from the Flask API
        st.json(result)
    else:
        st.error("Please enter both Student ID and Advisor ID.")
