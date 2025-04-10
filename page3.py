import streamlit as st
import pandas as pd

#data
team_name = "Barcelona United"
seasons = ["2020-21","2021-22","2022-23","2023-24"]
wins = [20,22,18,25]
losses = [10,8,12,5]
goal_scored = [60,65,55,70]
top_scorers = {"Messi": 15, "Pelè":12, "Maradona": 10}

data = {
    "season":seasons,
    "win":wins,
    "loss":losses,
    "goals":goal_scored
}

df=pd.DataFrame(data)


st.title(":blue[Barcelona United stats]")

tab1,tab2 = st.tabs(['Win vs Loss', 'Goal scored'])
with tab1:
    st.header("Win vs Losses")
    st.area_chart(df,x="season", y=["win","loss"])

with tab2:
    st.header("Goal scored")
    st.bar_chart(df,x="season", y="goals")

with st.expander("Goals/Wins seasonal comparison", expanded=False):
    st.line_chart(df, x="season", y=["win","goals"])

col1,col2,col3 = st.columns(3)

with col1:
    st.header("Messi")
    st.write(f":green[{top_scorers['Messi']} goals]")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Lionel-Messi-Argentina-2022-FIFA-World-Cup_%28cropped%29.jpg/250px-Lionel-Messi-Argentina-2022-FIFA-World-Cup_%28cropped%29.jpg")
    

with col2:
    st.header("Pelè")
    st.write(f":green[{top_scorers['Pelè']} goals]")
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/5e/Pele_con_brasil_%28cropped%29.jpg")
    

with col3:
    st.header("Maradona")
    st.write(f":green[{top_scorers['Maradona']} goals]")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/48/Argentina_celebrando_copa_%28cropped%29.jpg")
    


