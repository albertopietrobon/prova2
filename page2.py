import streamlit as st
st.title("Page 2!")

st.title(":red[Get info from the sidebar]")

player = st.session_state["Players"]
team = st.session_state["Team"]

st.write("The player is ", player)
st.write("The team is ", team)
