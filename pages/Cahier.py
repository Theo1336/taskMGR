import streamlit as st


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