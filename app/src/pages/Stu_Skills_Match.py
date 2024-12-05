import streamlit as st
import requests
import pandas as pd

# Base URL 
BASE_URL = "http://api:4000/student"  


def fetch_matching_job_postings(student_id):
    response = requests.get(f"{BASE_URL}/matching_job_postings/{student_id}")
    return response.json()

st.title("View Matching Job Postings Based on Skills")

# Collecting student ID
student_id = st.number_input("Student ID", min_value=1, step=1)

# Button to fetch matching job postings
if st.button("Fetch Matching Job Postings"):
    if student_id:
       
        result = fetch_matching_job_postings(student_id)
        
        if "error" not in result:
            if len(result) > 0:
               
                df = pd.DataFrame(result)

                # Display the result as a table
                st.subheader("Matching Job Postings")
                st.dataframe(df) 

            else:
                st.warning("Sorry. There are currently no jobs that match your skills.")
        else:
            st.error(f"Error: {result['error']}")
    else:
        st.error("Please enter a valid Student ID.")
