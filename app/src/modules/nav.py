# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon='🏠')

def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")

#### ------------------------ Marketing Analyst ------------------------
def MarketingAnalystHome():
    st.sidebar.page_link("pages/Marketing_Analyst_Home.py", label="Marketing Analyst Home", icon='👤')

def CompanySizes():
    st.sidebar.page_link("pages/Mar_Company_Size.py", label="Company Sizes Breakdown", icon='🏤')

def PopEmployers():
    st.sidebar.page_link("pages/Mar_Companies_Count.py", label="Popular Companies", icon='💼')

def PlacementMetrics():
    st.sidebar.page_link("pages/Mar_Placements.py", label="Placement Metrics", icon='📈')

## ------------------------ Coop Advisor ------------------------
def AdvisorHome():
    st.sidebar.page_link("pages/Coop_advisor_Home.py", label="Test the API", icon='🛜')

def AdvDashboard():
    st.sidebar.page_link("pages/Adv_Dashboard.py", label="Regression Prediction", icon='📈')

def AdvSorter():
    st.sidebar.page_link("pages/Adv_Sorter.py", label="Classification Demo", icon='🔁')

def AdvPop():
    st.sidebar.page_link("pages/Adv_Sorter.py", label="Classification Demo", icon='📃')\

#### ------------------------ System Admin Role ------------------------
def SysAdmin():
    st.sidebar.page_link("pages/Sysadmin_Home.py", label="System Admin", icon='🖥️')
    st.sidebar.page_link("pages/sys_health.py", label='Active Connections', icon='🏢')

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

        # Show relevant links if the user is a marketing analyst role.
        if st.session_state['role'] == 'marketing_analyst':
            MarketingAnalystHome()
            CompanySizes()
            PopEmployers()
            PlacementMetrics()
        
        # Show relevant links if the user is a system admin
        if st.session_state["role"] == "sysadmin":
            SysAdmin()

        # If the user role is usaid worker, show the Api Testing page
        if st.session_state['role'] == 'usaid_worker':
            AdvisorHome()
            AdvDashboard() 
            AdvSorter()        
            AdvPop()
            
       

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state['role']
            del st.session_state['authenticated']
            st.switch_page('Home.py')

