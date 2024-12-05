import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Student")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View Jobs with Fewer Applications', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Stu_Numapps.py')

if st.button('Add a Review on Previous or Current Employer', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Stu_Add_Review.py')

if st.button("Update a Review Previously Posted",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Stu_Update_Review.py')