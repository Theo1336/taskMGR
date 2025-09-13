import streamlit as st
import os

# réglages page devoirs #

st.set_page_config(
    page_title="Notes de Cours",
    page_icon="📓",
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

st.markdown("<h1>Gérer efficacement vos prises de notes 📓</h1>", unsafe_allow_html=True)
st.markdown("<h6>Ici, vous pouvez écrire vos cours et prendre vos notes efficacement au même endroit.</h6>", unsafe_allow_html=True)
st.markdown("---")

# formulaire / enregistrement cours #

titre = st.text_input("Nouvel page", placeholder="Titre")
corpText = st.text_area("notes de cours", placeholder="Description, notes de cours, cours", label_visibility="collapsed")
btn = st.button("💾 Sauvegarder")


if btn:
    
    dossier = "cours"
    os.makedirs(dossier, exist_ok=True)
    
    if titre.isalpha() or titre.isdigit() and titre != "":
        chemin = os.path.join(dossier, titre.strip() + ".txt")
        with open(chemin, "w", encoding="utf-8") as fichier:
            fichier.write(corpText)
            st.toast("devoir sauvegardé ✅")
    else:
        st.toast("devoir non sauvegardé ❌")
        st.warning("Attention un titre est manquant", icon="⚠️")