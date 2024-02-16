import streamlit as st
import plotly.express as px
import pandas
import sqlite3

#Esatblish a conneciton and a server
connection = sqlite3.connect("data.db")
cursor = connection.cursor

df = pandas.read_csv("data.txt")

figure = px.line(x=df["date"], y=df["temperature"],
                             labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)