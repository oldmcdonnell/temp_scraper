import streamlit as st
import plotly.express as px
import pandas
import sqlite3

#Esatblish a conneciton and a server
connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("SELECT date FROM temp")
date = cursor.fetchall()
date = [item[0] for item in date]

cursor.execute("SELECT temperature FROM temp")
temperature = cursor.fetchall()
temperature = [item[0] for item in temperature]

figure = px.line(x=date, y=temperature,
                 labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)
#text file date fetch
# df = pandas.read_csv("data.txt")
# figure = px.line(x=df["date"], y=df["temperature"],
#                              labels={"x": "Date", "y": "Temperature (C)"})
# st.plotly_chart(figure)

