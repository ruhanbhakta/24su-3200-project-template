import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

st.title("Welcome Co-op Advisor!")
st.write('### What would you like to do today?')

# Spacer
st.write("") 
st.write("") 

# Group items into rows for better layout
# Row 1
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(
        """
        <div class="card">
            <h3>📊 Student Dashboard</h3>
            <p>A quick glance at all your students and their statuses.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("View Students", type="primary", key="dashboard"):
        st.switch_page("pages/Adv_Dashboard.py")

with col2:
    st.markdown(
        """
        <div class="card">
            <h3>🔁 Student Sorter</h3>
            <p>Sort through students based on skills and experiences.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("View Breakdown", type="primary", key="sorter"):
        st.switch_page("pages/Adv_Sorter.py")

st.write("")
st.write("")

# Row 2
col3, col4 = st.columns(2, gap="large")

with col3:
    st.markdown(
        """
        <div class="card">
            <h3>📃 Popular Jobs List</h3>
            <p>See the most applied-to jobs.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("View Metrics", type="primary", key="popular_jobs"):
        st.switch_page("pages/Adv_Popularjobs.py")

with col4:
    st.markdown(
        """
        <div class="card">
            <h3>👨‍🏫 Add New Advisor</h3>
            <p>Add a new advisor to the system.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Add Advisor", type="primary", key="add_advisor"):
        st.switch_page("pages/Adv_Add_Advisor.py")

st.write("")
st.write("")

# Row 3
col5, col6 = st.columns(2, gap="large")

with col5:
    st.markdown(
        """
        <div class="card">
            <h3>👨‍🏫 Update Student's Advisor</h3>
            <p>Assign a new advisor to a student.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Assign Advisor", type="primary", key="assign_advisor"):
        st.switch_page("pages/Adv_Assign.py")

with col6:
    st.markdown(
        """
        <div class="card">
            <h3>👨‍🏫 Delete Job Posting</h3>
            <p>Delete job postings easily.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Delete Posting", type="primary", key="delete_posting"):
        st.switch_page("pages/Adv_Delete.py")
