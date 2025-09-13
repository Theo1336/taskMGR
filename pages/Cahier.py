import streamlit as st
import os


# réglages page devoirs #

st.set_page_config(
    page_title="Cahier",
    page_icon="📚",
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

st.markdown("<h1>Accéder facilement à vos cours 📚</h1>", unsafe_allow_html=True)
st.markdown("<h6>Ici, vous pouvez consulter facilement tous vos cours.</h6>", unsafe_allow_html=True)
st.markdown("---")


dossier = "cours"
os.makedirs(dossier, exist_ok=True)
lst = os.listdir("./cours")

for i in range(len(lst)):
    st.badge(lst[i], icon=":material/cloud_download:", color="blue")
    dossier = "cours"
    path = os.path.join(dossier, lst[i])
    with open(path, "r") as file:
        file_content = file.read()
        st.download_button(
            label="📥 Télécharger",
            data=file,
            file_name = lst[i],
            mime="text/plain",
            key=f"download_{i}",         
        )
            
    if st.button("👀 voir", type="secondary", key=f"voir_{i}"):
        st.text_area(label="area_hide", label_visibility="hidden", value=file_content)
        if st.button("🫣 cacher", key=f"cacher_{i}"):
            st.rerun()

    if st.button("🗑️ Supprimer", type="primary", key=f"supp_{i}"):
        os.remove(path)
        st.toast(f"{lst[i]} fichier supprimé 🗑️ ➡️ ✅")
        st.rerun()

        