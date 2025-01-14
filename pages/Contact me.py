import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your Email address")
    option = st.selectbox("What topic do you want to discuss?",
                          ["Job", "Project Proposals", "Other"])
    raw_message = st.text_area("Your Message ")
    text = f"""\
Subject: New email from {user_email}

From:{user_email}

Topic:{option}

{raw_message}
"""
    button = st.form_submit_button("Send")
    if button:
        #text = user_email+message
        send_email(text)
        st.info("Email Received.Thanks for reaching out")