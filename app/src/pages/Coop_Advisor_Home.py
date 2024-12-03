import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title("Welcome Co-op Advisor!")
st.write('')
st.write('')
st.write('### What would you like to do today?')

st.write("")  # Spacer
st.write("")  # Spacer

col1, col2, col3 = st.columns(3, gap="large")

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
    if st.button("View Students", type="primary"):
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
    if st.button("View Breakdown", type="primary"):
        st.switch_page("pages/Adv_Sorter.py")

with col3:
    st.markdown(
        """
        <div class="card">
            <h3>📃 Popular Jobs List</h3>
            <p>See the most applied to jobs.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("View Metrics", type="primary"):
        st.switch_page("pages/Adv_Popularjobs.py")