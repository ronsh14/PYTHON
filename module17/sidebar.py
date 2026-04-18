import streamlit as st

st.sidebar.header("sidebar")

st.sidebar.write("This is the side bar.")

st.sidebar.selectbox("choose an option", ["Option 1","Option 2","Option 3"])

st.sidebar.radio("Go to", ["Home","Data","Settings"])

