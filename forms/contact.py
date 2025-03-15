import re

import streamlit as st
import requests

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

def is_valid_email(email):
    # basic email validation
    email_pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email) is not None




def contact_form():
    with st.form("contact_form"):
        name = st.text_input('First Name')
        email = st.text_input('Email Address')
        message = st.text_area(' Your Message')
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            if not WEBHOOK_URL:
                st.error(
                    "Email service is not set up. Please try again later.", icon="📧"
                 )
                st.stop()

        if not name:
            st.error("Please enter your name.", icon="🧑🏾")
            st.stop()
                
        if not email:
            st.error("Please enter your email address.", icon="📨")
            st.stop()
        
        if not is_valid_email(email):
            st.error("Please enter a valid email address.", icon="📧")
            st.stop()

        if not message:
            st.error("Please enter your message.", icon="💬")
            st.stop()


        # prepare the data payload for the webhook request
        data = {"email": email, "name": name, "message": message}
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 200:
            st.success("Message sent successfully! 🥳", icon="🚀")
        else:
            st.error("Failed to send message. Please try again later.", icon="❌")