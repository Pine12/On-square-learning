"""
Created on Mon Nov  4 10:16:28 2024

@author: gelliott
"""
import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Entered Apprentice", "Fellow Craft", "Master Mason","Admin"]


def login():
    st.title("🎈 On The Square - Ritual Learning")
    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role
st.set_page_config(layout="wide",)
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
ea_page = st.Page(
    "ea/ea.py",
    title="1st Degree",
    icon=":material/help:",
    default=(role == "Entered Apprentice"),
)
fc_page = st.Page(
    "fc/fc.py",
    title="2nd Degree",
    icon=":material/bug_report:",
    default=(role == "Fellow Craft"),
)
mm_page = st.Page(
    "mm/mm.py",
    title="3rd Degree",
    icon=":material/healing:",
    default=(role == "Master Mason"),
)
admin = st.Page(
    "admin/admin.py",
    title="Admin 1",
    icon=":material/person_add:",
    default=(role == "Admin"),
)

account_pages = [logout_page, settings]
ea_degree_pages = [ea_page]
fc_degree_pages = [ea_page, fc_page]
mm_degree_pages = [ea_page, fc_page, mm_page]
admin_pages = [admin]

st.logo(
    "images/square-and-compass-07.png",
    icon_image="images/square-and-compass-07.png",
    size="large"
)

page_dict = {}
if st.session_state.role in ["Entered Apprentice","Admin"]:
    page_dict["EA"] = ea_degree_pages
if st.session_state.role in ["Fellow Craft","Admin"]:
    page_dict["FC"] = fc_degree_pages
if st.session_state.role in ["Master Mason","Admin"]:
    page_dict["MM"] = mm_degree_pages
if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()

       