import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title("Welcome System Admin!")
st.write('')
st.write('')
st.write('### What would you like to do today?')

st.write("")  
st.write("")  

if st.button('View Number of Active Connections', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/sys_health.py')

if st.button('View Number of Allowed Connections', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/sys_conn_limit.py')

if st.button('View Server Load', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/sys_server.py')

if st.button('Update DB Data', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/sys_make_changes.py')
