import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import mysql connector
import mysql.connector

# import streamlit
import streamlit as st
# create connection
mydb = mysql.connector.connect(
    host="test-database.chuimlqlnedu.us-east-1.rds.amazonaws.com",
    user = "admin",
    passwd = "password",
    database = "sample"
)

# create cursor
mycursor = mydb.cursor()

# create query

def app():
    st.title("Name and Age Input Form")
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age")

    if st.button("Submit"):
        st.success("You have successfully submitted your name and age")
        st.write("Name: ", name)
        st.write("Age: ", age)

        sql = "INSERT INTO mytable (Name, Age) VALUES (%s, %s)"
        val = (name, age)
        mycursor.execute(sql, val)
        mydb.commit()

        st.success("Data successfully committed to database!")

     # Add a button to read data from the database
    if st.button("Read Data"):
        # Retrieve data from the database
        mycursor.execute("SELECT * FROM mytable")
        data = mycursor.fetchall()
        
        # Display the data in a table
        st.write("Data from database:")
        st.table(data)

# run the app
if __name__ == "__main__":
    app()