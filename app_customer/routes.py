import streamlit as st
import requests

# URL de l'API FastAPI
api_url = "http://localhost:8000/predict/"

# Titre de l'application
st.title('Analyse de Sentiment')

# Description
st.write('Entrez un commentaire pour analyser son sentiment.')

# Champ pour entrer un texte
user_input = st.text_area("Votre commentaire")

# Lorsque l'utilisateur soumet le texte
if st.button('Analyser'):
    if user_input:
        # Préparer les données à envoyer à l'API
        payload = {"text": user_input}
        
        try:
            # Envoyer la requête à l'API
            response = requests.post(api_url, json=payload)
            
            # Vérifier si la réponse est correcte
            if response.status_code == 200:
                result = response.json()
                
                # Afficher le résultat de la prédiction
                st.subheader("Sentiment prédit :")
                st.write(f"**Sentiment :** {result['sentiment']}")
                st.write(f"**Probabilité :** {result['probability']}")

                st.subheader("Texte nettoyé :")
                st.write(result['cleaned_text'])
            else:
                st.error("Erreur dans la prédiction. Veuillez réessayer.")
        except Exception as e:
            st.error(f"Une erreur s'est produite : {e}")
    else:
        st.warning("Veuillez entrer un commentaire.")
