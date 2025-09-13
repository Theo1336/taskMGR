import streamlit as st
import datetime
import time
import sqlite3


# réglages page devoirs #

st.set_page_config(
    page_title="Devoirs",
    page_icon="📝",
    layout="wide"
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

# titre sous titre #

st.markdown("<h1>Gérer l'ajout de vos devoirs à un seul endroit 📝</h1>", unsafe_allow_html=True)
st.markdown("<h6>ici vous pouvez ajouter vos devoirs à votre agenda, consultable sur la page d'acceuil.</h6>", unsafe_allow_html=True)
st.markdown("---")

# formulaire #

with st.form("form_devoirs", clear_on_submit=True):
    st.write("Remplissez ces champs pour ajouter un devoirs: ")
    nom_matiere = st.text_input("Matière...", placeholder="nom de votre matière")
    desc_matiere = st.text_area("Description...",  placeholder="ajoutez une description")
    date_matiere = st.date_input("Devoir à faire pour le: ",  datetime.date(2025, 9, 1), format="DD/MM/YYYY")

    options = ["5 min", "10 min", "15 min", "30 min", "45 min", "1h", "1h 30 min", "2h", "Plus de 2 h"]
    choix_duree = st.selectbox("Durée estimée :", options)

    st.markdown("---") 
    st.write("ajouter des tags: ")
    
    col1t, col2t, col3t, colt4 = st.columns(4)

    
    with col1t:
        check1 = st.checkbox("DST")
    with col2t:
        check2 =st.checkbox("TP")
    with col3t:
        check3 = st.checkbox("Revision")
    with colt4:
        check4 = st.checkbox("Urgent") 

    tags = []
    if check1:
        tags.append("DST 📑")
    if check2:
        tags.append("TP ✒️")
    if check3:
        tags.append("Révision 📖")
    if check4:
        tags.append("Urgent 🚨")
        
    for tag in tags:
        st.markdown(f":violet-badge[{tag}] ", unsafe_allow_html=True)

    submitted = st.form_submit_button("💾 Sauvegarder")
    
    
# ajout bdd fontion #

def ajout_bdd():
    try:
        con = sqlite3.connect("taskmgr.db")
        cur = con.cursor()
        date_str = date_matiere.isoformat()
        tags_text = ", ".join(tags)
        cur.execute("INSERT INTO Devoirs (matiere, description_mat, date_mat, duree_mat, tags) VALUES (?, ?, ?, ?, ?)", (nom_matiere, desc_matiere, date_str, choix_duree, tags_text))
        con.commit()
        con.close()
        return 0
    except Exception as e:
        st.error(f"Erreur SQL : {e}")
        print(f"{e}")
        return -1

# notifications en haut à droite et avertissement en bas #
# ajout à la base de données #
 
if submitted:    

    if nom_matiere == "":
        st.warning("Vous n'avez pas spécifié de nom pour la matière", icon="⚠️")
    if desc_matiere == "":
        st.warning("Il manque une description", icon="⚠️")
    elif nom_matiere and desc_matiere:        
        st.toast("Enregistrement du devoir en cours...", icon="⌛")
        res = ajout_bdd()       
        time.sleep(1.0)
        if res == 0:
            st.toast("Devoir enregistré et ajouté avec succès", icon='✅')
            st.badge("Success", icon=":material/check:", color="green")
        else:
            st.toast("Un problème est survenu, réessayez plus tard", icon='❌')




    
