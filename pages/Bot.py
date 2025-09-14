import streamlit as st
from ollama import chat, generate



# réglages page devoirs #

st.set_page_config(
    page_title="Assistant",
    page_icon="👷",
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

st.markdown("<h1>Communiquer facilement avec votre assistant IA personel 👷</h1>", unsafe_allow_html=True)
st.markdown("<h6>ici vous pouvez communiquer avec votre chatbot ia.</h6>", unsafe_allow_html=True)
st.markdown("---")


# Initialiser la mémoire du chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Afficher l’historique
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# saisie msg #

prompt = st.chat_input(
    "écrivez quelque chose...",
    accept_file=False,
)



if prompt:
    user_text = prompt

    # Ajouter le message utilisateur
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    # Envoyer tout l’historique à Ollama
    response = chat(model="mistral", messages=st.session_state.messages)

    # Récupérer la réponse
    ai_msg = response["message"]["content"]

    # Ajouter la réponse dans l’historique
    st.session_state.messages.append({"role": "assistant", "content": ai_msg})

    # Afficher la réponse
    with st.chat_message("assistant"):
        st.markdown(ai_msg)


