import streamlit as st
import requests

# Base URL for your Flask backend
BASE_URL = "http://api:4000/student"  # Update to your actual API URL

# Function to update student review
def update_student_review(review_id, review):
    response = requests.put(
        f"{BASE_URL}/update_student_review", 
        json={"reviewId": review_id, "review": review}
    )
    return response.json()

# Streamlit app interface
st.title("Update Student Review")

# Collecting review details using text inputs
review_id = st.number_input("Review ID", min_value=1, step=1)
review = st.text_area("New Review Text", height=150)

# Button to submit the data
if st.button("Update Review"):
    if review_id and review.strip():
        # Send request to Flask API to update the student's review
        result = update_student_review(review_id, review)
        
        # Show the result from the Flask API
        if "message" in result:
            st.success(result["message"])
        elif "error" in result:
            st.error(result["error"])
    else:
        st.error("Please enter both Review ID and Review text.")
