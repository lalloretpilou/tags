import streamlit as st
import requests

# Titre de l'application
st.title("P5")

input_text = st.text_area("Entrez la description", "")

api_url = "https://lalloret.pythonanywhere.com/predict"  # Remplacez par l'URL de votre API

# Fonction pour appeler l'API
def get_nlp_estimation(text):
    try:
        response = requests.post(api_url, json={"text": text})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Erreur lors de l'appel de l'API : {e}")
        return None

# Bouton pour effectuer l'estimation
if st.button("Analyser le texte"):
    if input_text:
        estimation = get_nlp_estimation(input_text)
        if estimation:
            st.subheader("R�sultats de l'estimation")
            st.write(estimation)
    else:
        st.warning("Veuillez entrer un texte avant de lancer l'analyse.")