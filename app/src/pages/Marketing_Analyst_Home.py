import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title("Welcome Marketing Analyst!")
st.write('')
st.write('')
st.write('### What would you like to do today?')

st.write("")  
st.write("")  

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown(
        """
        <div class="card">
            <h3>🎯 Popular Companies</h3>
            <p>Discover top companies for students and alumni.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Explore Companies", type="primary"):
        st.switch_page("pages/Mar_Companies_Count.py")

with col2:
    st.markdown(
        """
        <div class="card">
            <h3>🏢 Company Breakdown</h3>
            <p>Analyze companies by size for better insights.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("View Breakdown", type="primary"):
        st.switch_page("pages/Mar_Company_Size.py")

with col3:
    st.markdown(
        """
        <div class="card">
            <h3>📊 Placement Metrics</h3>
            <p>Understand placement trends and key metrics.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("View Metrics", type="primary"):
        st.switch_page("pages/Mar_Placements.py")
