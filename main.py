import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Teerthanker Sarker")
    content ="""Hi, I’m Teerthanker Sarker, a Computer Science and Engineering graduate with a strong passion for crafting seamless and engaging web experiences. As an expert in web development, I specialize in building responsive, user-friendly, and dynamic web applications that align with modern design and functionality standards.
        I am committed to continuous learning and innovation, always eager to tackle new challenges and stay ahead in the rapidly evolving tech landscape. Whether it’s front-end intricacies, back-end logic, or full-stack solutions, I aim to deliver high-quality results that meet user needs and exceed client expectations.
        Let’s create something extraordinary together!
    """
    st.info(content)

content2="""
Below you can find some of the apps i have built in Python.Feel free to contact me!
"""
st.write(content2)

col3,col4 = st.columns(2)

df= pd.read_csv("data.csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])


with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
