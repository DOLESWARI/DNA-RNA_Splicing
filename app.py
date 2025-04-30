import streamlit as st
from streamlit_option_menu import option_menu
import hashlib
import sqlite3
from streamlit_option_menu import option_menu

import about_us
import feedback
import papers
import disease_pred
import rna_pred
import home
import black_white


# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Function to create users table
def create_users_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


# Function to add user to the database
def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hash_password(password)))
    conn.commit()
    conn.close()


# Function to authenticate user
def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT password FROM users WHERE username = ?', (username,))
    result = c.fetchone()
    conn.close()
    if result and result[0] == hash_password(password):
        return True
    return False


# Function to check if a user exists
def user_exists(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    result = c.fetchone()
    conn.close()
    if result:
        return True
    return False


def signup():
    st.subheader("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    password_confirm = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if not username or not password or not password_confirm:
            st.warning("Please fill in all fields.")
        elif user_exists(username):
            st.warning("Username already exists. Please choose a different username.")
        elif password != password_confirm:
            st.warning("Passwords do not match. Please try again.")
        else:
            add_user(username, password)
            st.success("Sign up successful. You can now log in.")
            st.info("Go to the Login page to log in.")


def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not username or not password:
            st.warning("Please fill in all fields.")
        elif not user_exists(username):
            st.warning("Username does not exist. Please sign up first.")
        elif not authenticate_user(username, password):
            st.warning("Incorrect password. Please try again.")
        else:
            st.success("Login successful!")
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.rerun()


def home_page():
    st.subheader("Home")
    st.write("Welcome to the DNA Splicing App!")
    home.run()


'''def prediction_page():
    st.subheader("Prediction of Brain Tumor")
    st.write("This page will contain the prediction functionality.")
    pred.run()'''


def about_us_page():
    st.subheader("About Us")
    st.write("This page will provide information about us.")
    about_us.run()


def help_page():
    st.subheader("Help")
    st.write("This page will provide help and support.")


def main():
    st.markdown("""
        <style>
        .stApp {
            background-color: #fa8072;
            color: #000000;
        }
        .css-1d391kg, .css-1v3fvcr {
            background-color: #ba1c53;
        }
        .sidebar .sidebar-content {
            background-color: #ffa07a;
        }

        </style>
        """, unsafe_allow_html=True)

    st.title("DNA Splicing Insight")

    # Create the users table if it doesn't exist
    create_users_table()

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if st.session_state["logged_in"]:
        st.subheader(f"Welcome, {st.session_state['username']}!")

        # Sidebar navigation with streamlit-option-menu
        with st.sidebar:
            selected = option_menu(
                'DNA Splicing Website',
                ['Home', 'Female Fertility Prediction',
                 'Male Fertility Prediction', 'Composite Fertility Score', 'Image Processing', 'RNA_Seq(IVF)',
                 'DNA Analysis', 'Research Papers', 'About Us', 'Feedback' 'Help', 'Logout'],
                icons=['house', 'person-standing-dress', 'person-standing','people-fill','bandaid','bar-chart-steps', 'activity', 'info-circle', 'question-circle',
                       'box-arrow-right'],
                menu_icon='hospital-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5px", "background-color": "#ffa07a"},
                    "icon": {"color": "white", "font-size": "25px"},
                    "nav-link": {
                        "font-size": "16px",
                        "text-align": "left",
                        "margin": "0px",
                        "color": "black",
                    },
                    "nav-link-selected": {"background-color": "#ba1c53"},
                },
            )

        # Display pages based on selection
        if selected == "Image Processing":
            black_white.run()
        if selected == "Home":
            home_page()
        elif selected == "RNA_Seq(IVF)":
            rna_pred.run()
        elif selected == "DNA Analysis":
            disease_pred.run()
        elif selected == "Research Papers":
            papers.main()
        elif selected == "About Us":
            about_us_page()
        elif selected == "Feedback":
            feedback.run()
        elif selected == "Help":
            help_page()
        elif selected == "Logout":
            st.session_state["logged_in"] = False
            st.session_state["username"] = None
            st.rerun()  # Rerun the app to update the state

    else:
        # Initial login/signup page
        page = option_menu(
            'Sign_In/Login',
            ['Sign In', 'Log In'],
            icons=['person-circle', 'person-check'],
            menu_icon='hospital-fill',
            default_index=0,
            styles={
                "container": {"padding": "5px", "background-color": "#ffa07a", "border-radius": "0px"},
                "icon": {"color": "white", "font-size": "25px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px",
                    "color": "black",
                },
                "nav-link-selected": {"background-color": "#ba1c53"},
            },
        )

        if page == "Sign In":
            signup()
        elif page == "Log In":
            login()


if __name__ == "__main__":
    main()
