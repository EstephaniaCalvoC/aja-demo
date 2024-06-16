import streamlit as st

st.set_page_config(page_title="AJA Demo", page_icon=":robot:")
st.header("AI Judge Assistant Demo")

description = "\
    AI-powered tool to summarize legal cases, \
    helping judges quickly understand the key points of a case.\
    "
st.text(description)
