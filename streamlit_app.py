import streamlit as st


page1 = st.Page('page1.py', title='Page 1')
page2 = st.Page('page2.py', title='Page 2')
page3 = st.Page('page3.py', title='Page 3')
pg = st.navigation([page1,page2,page3])
st.set_page_config(page_title='DV4S')

st.sidebar.selectbox(
    "Select your player",
    ("Maradona", "Pele", "Fonseca"),
    key="Players"
)

with st.sidebar:
    rb = st.radio(
        "Team",
        ("Napoli", "Milan", "Roma"),
        key="Team"
    )

pg.run()