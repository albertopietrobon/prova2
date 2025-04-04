import streamlit as st
import pandas as pd
import numpy as np

#metrics
st.title(":red[Metric]")
st.metric("Number of **assists**:", 36, "+4")

#dataframe
st.title(":red[Dataframe]")
data = {
    "name":["Kaka", "Pelè", "Maradona"],
    "goals":[45, 60, 77],
    "team":["Milan", "Boca", "Napoli"]
}

df = pd.DataFrame(data)

st.subheader("Dataframe")
st.dataframe(df) #interactive
st.subheader("Table")
st.table(df) #not interactive

#data
n_goals = np.random.randint(15, size=(38,3))
player_names = ["Baggio", "Fonseca", "Ancelotti"]
df1 = pd.DataFrame(n_goals,columns=player_names )

#line charts
st.title(":red[Line chart]")

st.line_chart(df1)

#area chart
st.title(":red[Area chart]")

st.area_chart(df1)

#bar chart
st.title(":red[Bar chart]")

st.bar_chart(df1)

#scatter chart
st.title(":red[Scatter chart]")

n_matches = 38
x = np.random.rand(n_matches)*100
y = np.random.rand(n_matches)*100
goal_values = np.random.randint(0, 15, size=(n_matches))


goal_color = np.random.rand(n_matches,3) #RGB color
goal_color_lot = [tuple(c) for c in goal_color]
data_goal={
    "X": x,
    "Y": y,
    "goal": goal_values,
    "color": goal_color_lot
}
st.dataframe(data_goal)
df2 = pd.DataFrame(data_goal)
st.scatter_chart(data_goal, x="X", y="Y", size="goal", color="color")

#map
st.title(":red[Map]")

n_pos = 100
lat = np.random.uniform(45.8,45.9, n_pos)
long = np.random.uniform(9.35,9.45, n_pos)

location = {
    "latitude":lat,
    "longitude":long
}

df3 = pd.DataFrame(location)
st.map(df3)