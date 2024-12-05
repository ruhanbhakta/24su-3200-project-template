import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Add navigation links and optional logo
SideBarLinks()

# Page title and introduction
st.title("🚀 About FreshMeet")
st.markdown("---")

# Section: The Problem
st.subheader("🌟 The Problem")
st.markdown(
    """
    - **Students:** Overwhelmed and unsure during their first co-op search.  
    - **Recruiters:** Struggle to find qualified candidates efficiently.  
    - **Advisors:** Juggling hundreds of students with no scalable tools.
    """
)

# Section: The Solution
st.subheader("💡 FreshMeet: Revolutionizing Co-ops")
st.markdown(
    """
    FreshMeet simplifies the co-op experience with a **data-driven platform**:  
    - **For Students:** Personalized dashboards for tracking applications and skill progress.  
    - **For Advisors:** Intuitive tools to monitor and support students at scale.
    - **For Marketing Analaysts:** Valueable data insights on key metrics to communicate to prospective students.
    """
)

# Section: Why Choose FreshMeet?
st.subheader("✨ Why FreshMeet?")
st.markdown(
    """
    - **Streamlined Processes:** Transform the co-op journey from chaos to clarity.  
    - **Data Insights:** Leverage powerful analytics for better decision-making.  
    - **Seamless Connections:** Bring students and advisors together.
    """
)

# Footer
st.markdown("---")
st.markdown("*Created by Ruhan, Yuan, Borys, Jeff, and Spencer*")
