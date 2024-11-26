# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon='🏠')

def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")

#### ------------------------ Examples for Role of pol_strat_advisor ------------------------
def PolStratAdvHomeNav():
    st.sidebar.page_link("pages/Marketing_Analyst_Home.py", label="Marketing Analyst Home", icon='👤')

def CompanySizes():
    st.sidebar.page_link("pages/Mar_Company_Size.py", label="Company Sizes Breakdown", icon='🏤')

def PopEmployers():
    st.sidebar.page_link("pages/Mar_Companies_Count.py", label="Popular Companies", icon='💼')

def PlacementMetrics():
    st.sidebar.page_link("pages/Mar_Placements.py", label="Placement Metrics", icon='📈')

## ------------------------ Examples for Role of usaid_worker ------------------------
def ApiTestNav():
    st.sidebar.page_link("pages/12_API_Test.py", label="Test the API", icon='🛜')

def PredictionNav():
    st.sidebar.page_link("pages/11_Prediction.py", label="Regression Prediction", icon='📈')

def ClassificationNav():
    st.sidebar.page_link("pages/13_Classification.py", label="Classification Demo", icon='🌺')

#### ------------------------ System Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon='🖥️')
    st.sidebar.page_link("pages/21_ML_Model_Mgmt.py", label='ML Model Management', icon='🏢')


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in. 
    """    

    # add a logo to the sidebar always
    st.sidebar.image("assets/image.png")

    # If there is no logged in user, redirect to the Home (Landing) page
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page('Home.py')
        
    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show relevant links if the user is a political strategy advisor role.
        if st.session_state['role'] == 'marketing_analyst':
            PolStratAdvHomeNav()
            CompanySizes()
            PopEmployers()
            PlacementMetrics()

        # If the user role is usaid worker, show the Api Testing page
        if st.session_state['role'] == 'usaid_worker':
            PredictionNav()
            ApiTestNav() 
            ClassificationNav()
        
        # If the user is an administrator, give them access to the administrator pages
        if st.session_state['role'] == 'administrator':
            AdminPageNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state['role']
            del st.session_state['authenticated']
            st.switch_page('Home.py')

