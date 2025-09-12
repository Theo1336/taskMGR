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
df = pd.read_sql_query("""
    SELECT id, matiere, description_mat, date_mat, duree_mat, tags
    FROM devoirs
""", con)

df["finit"] = False
df_edit = st.data_editor(df, hide_index=True)


btn = st.button("supprimer la sélection", type="primary")
btnac = st.button("actualiser")


# suppression #
def supp():
    finis = df_edit[df_edit["finit"] == True]

    for _, row in finis.iterrows():
        id_bdd = row["id"]

        # Vérification avant suppression
        cur.execute("SELECT matiere FROM devoirs WHERE id=?", (id_bdd,))
        if cur.fetchone() == None:
            st.toast("Un problème est survenu, réessayez plus tard", icon='❌')
            

        # Suppression en BDD
        cur.execute("DELETE FROM devoirs WHERE id=?", (id_bdd,))
        st.toast(f"Ligne avec {id_bdd} à été supprimé 🗑️")

    con.commit()

    df = pd.read_sql_query("""
        SELECT id, matiere, description_mat, date_mat, duree_mat, tags
        FROM devoirs
    """, con)
    df["finit"] = False

if btn:
    supp()




con.close()
