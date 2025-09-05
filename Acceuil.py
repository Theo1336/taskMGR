import streamlit as st
import datetime
import time
import sqlite3


# mise en place bdd #

con = sqlite3.connect("taskmgr.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS devoirs( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matiere TEXT,
    desc TEXT,
    date TEXT,
    duree TEXT,
    tags TEXT  
)""")

con.commit()
con.close()


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

