import streamlit as st
import sqlite3
import pandas as pd
import json

# mise en place bdd #

con = sqlite3.connect("taskmgr.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS devoirs( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matiere TEXT,
    description_mat TEXT,
    date_mat TEXT,
    duree_mat TEXT,
    tags TEXT  
)""")

con.commit()



# Réglages page principal #


st.set_page_config(
    page_title="Page Principale",
    page_icon="🏠",  
    # layout="wide" 
)



st.markdown("""
    <style>
        div.stMarkdown h1 {
            margin-bottom: -2vhvh; 
        }
        
        div.stMarkdown h6 {
            margin-bottom: -10vh; 
        }
    </style>
""", unsafe_allow_html=True)

# presentation titre sous titre #

st.markdown("<h1>Bienvenue sur Task Manager👋</h1>", unsafe_allow_html=True)
st.markdown("<h6>vous retrouverez ici le menu principal, ainsi que votre agenda.</h6>", unsafe_allow_html=True)
st.markdown("---")


# ajout à l'agenda #

nombre = 0
df = pd.read_sql_query("""
    SELECT matiere, description_mat, date_mat, duree_mat, tags
    FROM devoirs""", con)
con.close()


st.dataframe(df)