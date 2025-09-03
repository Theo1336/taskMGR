import streamlit as st
import datetime
import time

# réglages page principal #

st.set_page_config(
    page_title="Deuxième Page",
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

st.markdown("<h1>Gérer l'ajout de vos devoirs à un seul endroit</h1>", unsafe_allow_html=True)
st.markdown("<h6>ici vous pouvez ajouter vos devoirs à votre agenda, consultable sur la page d'acceuil.</h6>", unsafe_allow_html=True)
st.markdown("---")

# formulaire #

st.title("Ajouter un devoirs à votre agenda")


with st.form("form_devoirs", clear_on_submit=True):
    st.write("Remplisser ces champs pour ajouter un devoirs: ")
    st.text_input("Matière...")
    st.text_area("Description...")
    st.date_input("Devoir à faire pour le: ",  datetime.date(2025, 9, 1), format="DD/MM/YYYY")
    
    
    st.markdown("---")

    st.write("maintenant estimons le temps que cela vous prendra, si cela prendra probablement plus d'une heure veuillez cocher la case.")
    


    st.checkbox("une heure est nécessaire ou plus pour le terminer")
    


    
    st.markdown("---") 
    st.write("ajouter des tags: ")

    
    col1t, col2t, col3t, colt4 = st.columns(4)
    
    with col1t:
        st.checkbox("DST")
        
    with col2t:
        st.checkbox("TP")
    
    with col3t:
        st.checkbox("Révision")
    with colt4:
        st.checkbox("urgent 🚨")
    

    submitted = st.form_submit_button("ajouter")
    
# notifications en haut à droite #
 
if submitted:
    st.toast("enregistrement du devoir en cours", icon="⌛")
    time.sleep(1.0)
    st.toast("Devoirs enregistré et ajouter avec succèss", icon='✅')


    