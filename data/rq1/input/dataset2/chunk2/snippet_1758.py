#Source: https://stackoverflow.com/questions/73217356/with-headersection-attributeerror-enter
import streamlit as st
from user import login

headerSection = st.container
mainSection = st.container
loginSection = st.container
logoutSection = st.container

def main_page():
    with mainSection:
        st.text("Things to do")

def loggedOut_clicked():
    st.session_state['loggedIn'] = False


def logout_page():
    loginSection.empty();
    with logoutSection:
        st.button("Log out", key="logout", on_click=loggedOut_clicked)


def loggedIn_clicked(userName, password):
    if login(userName, password):
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False
        st.error("Invalid user name or password")


def login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            userName = st.text_input(placeholder="Enter emailAddress")
            password = st.text_input(placeholder="Enter password", type="password")
            st.button("Login", on_click=loggedIn_clicked, args=(userName, password))


with headerSection:
    st.title("Talent Search")
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        login_page()
    else:
        if st.session_state['loggedIn']:
            logout_page()
            main_page()