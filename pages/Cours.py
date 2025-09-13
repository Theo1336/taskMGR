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

uploaded_files = st.file_uploader(
    "OU ajouter un fichier texte (Attention : si un fichier portant le même nom existe déjà, il sera remplacé. Pour plus d'informations sur vos fichiers, consultez votre cahier.)", accept_multiple_files=True, type="txt"
)

btn = st.button("💾 Sauvegarder")


if btn:
    dossier = "cours"
    os.makedirs(dossier, exist_ok=True)
    

    if titre.isalpha() or titre.isdigit() and titre != "":
        chemin = os.path.join(dossier, titre.strip() + ".txt")
        with open(chemin, "w", encoding="utf-8") as fichier:
            fichier.write(corpText)
            st.toast("devoir sauvegardé ✅")
    elif not uploaded_files:
        st.toast("devoir non sauvegardé ❌")
        st.warning("Attention un titre est manquant", icon="⚠️")
        
    if uploaded_files:
        for uploaded_file in uploaded_files:
            chemin = os.path.join(dossier,  uploaded_file.name)
            
            with open(chemin, "w", encoding="utf-8") as fichier:
                content = uploaded_file.read().decode("utf-8")
                fichier.write(content)
                st.success(f"Fichier {uploaded_file.name} sauvegardé ✅")


            
        
    
        
