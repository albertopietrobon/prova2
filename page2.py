import streamlit as st
import numpy as np

st.title("Page 2!")

st.title(":red[Get info from the sidebar]")

#recall session stata
player = st.session_state["Players"]
team = st.session_state["Team"]

st.write("The player is ", player)
st.write("The team is ", team)

#columns
st.title(":red[Columns]")

col1,col2 = st.columns([0.3,0.7])

col1.header("This is col1")
col1.image("https://www.sixtusitalia.it/piuma/0_0_80:auto/https://www.sixtusitalia.it/wp-content/uploads/2022/09/infortuni-del-tennis.jpeg")

col2.header("This is col2")
col2.image("https://buonenotizie.it/wp-content/uploads/2024/06/pallavolo-femminile.jpg")

#notation
st.title(":red[More columns]")

data = np.random.rand(20,1)
colA,colB = st.columns(2)

with colA:
    st.header('Data Viz')
    st.bar_chart(data)

with colB:
    st.header('Table')
    st.table(data)

#tabs
st.title(":red[Tabs]")

tab1,tab2 = st.tabs(['Tennis','Volley'])

tab1.header("Tennis")
tab1.image("https://www.sixtusitalia.it/piuma/0_0_80:auto/https://www.sixtusitalia.it/wp-content/uploads/2022/09/infortuni-del-tennis.jpeg")
tab2.header("Volley")
tab2.image("https://buonenotizie.it/wp-content/uploads/2024/06/pallavolo-femminile.jpg")


#expenders
st.title(":red[Expanders]")

with st.expander("Data Viz open", expanded=True):
    st.subheader("My data")
    st.line_chart(data)

with st.expander("Data Viz close", expanded=False):
    st.subheader("My data")
    st.area_chart(data)

#secrets
st.title(":red[Secret info]")

username = st.secrets["username"]
st.write(username)

import os 
password = os.environ["password"]
st.write(password)



