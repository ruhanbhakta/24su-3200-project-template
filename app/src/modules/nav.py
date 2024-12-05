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
    st.sidebar.page_link("pages/Advisor_Home.py", label="Home Page", icon='🛜')

def AdvDashboard():
    st.sidebar.page_link("pages/Adv_Dashboard.py", label="Students Dashboard", icon='📈')

def AdvSorter():
    st.sidebar.page_link("pages/Adv_Sorter.py", label="Sorted Students", icon='🔁')

def AdvPop():
    st.sidebar.page_link("pages/Adv_Popularjobs.py", label="Popular Jobs", icon='📃')\

#### ------------------------ System Admin Role ------------------------
def SysAdmin():
    st.sidebar.page_link("pages/Sysadmin_Home.py", label="System Admin", icon='🏠')
    st.sidebar.page_link("pages/sys_health.py", label='Active Connections', icon='🏢')
    st.sidebar.page_link("pages/sys_conn_limit.py", label="Allowed Connections", icon= "⚠️")
    st.sidebar.page_link("pages/sys_conn_limit.py", label="Server Load", icon= "🏋🏻")
    st.sidebar.page_link("pages/sys_make_changes.py", label="Update DB Information")

#### ------------------------ Students Role ------------------------
def Student():
    st.sidebar.page_link("pages/Student_Home.py", label="Student Home", icon='🖥️')
    st.sidebar.page_link("pages/Stu_Numapps.py", label='Less Popular Jobs', icon='📉')
    st.sidebar.page_link("pages/Stu_Add_Review.py", label='Add a Review', icon='➕')
    st.sidebar.page_link("pages/Stu_Update_Review.py", label='Update a Review', icon='↔️')
    st.sidebar.page_link("pages/Stu_Delete_Review.py", label='Delete a Review', icon='🗑️')
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

        if st.session_state["role"] == "student":
            Student()

        # If the user role is usaid worker, show the Api Testing page
        if st.session_state['role'] == 'coop_advisor':
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

