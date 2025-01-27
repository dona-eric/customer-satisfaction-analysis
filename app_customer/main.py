import logging
import logging.config
import joblib
import yaml
from fastapi import FastAPI
from pydantic import BaseModel
from app_customer.utils import create_vectorizer, vectorize_text, preprocess

# charger la configuration
with open('../config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)
    
## configurer les logs.

logging.config.fileConfig('../config/logging.conf', disable_existing_loggers=False)
logger = logging.getLogger("app")

## initialisation de l'application
app = FastAPI(title=config['app']['name'], version=config['app']['version'])
logger.info('Application démarrée')


## definir les routes pour l'api 

# Charger le modèle sauvegardé
model = joblib.load("/home/dona-erick/Customer-satisfaction-analysis/app_customer/models/model.pkl")

# Initialiser le vectoriseur
vectorizer = create_vectorizer(max_features=10000)

# Schéma pour les données entrantes
class InputData(BaseModel):
    text: str  # Texte utilisateur
    
    @classmethod
    def validate(cls, value):
        if not value.strip():
            raise ValueError("Le texte ne peut pas être vide.")
        return value

# Route d'accueil
@app.get("/")
def home():
    return {"message": "Bienvenue sur la plateforme d'analyse de sentiment !"}

# Route pour prédire le sentiment
@app.post("/predict/")
def predict(data: InputData):
    try:
        # Vérifier si le texte est vide
        if not data.text.strip():
            raise ValueError("Le texte fourni est vide.")

        # Prétraiter et vectoriser le texte
        vectorized_text = vectorize_text(data.text, vectorizer)
        
        # Prédire le sentiment
        prediction = model.predict(vectorized_text)[0]
        probability = model.predict_proba(vectorized_text).max()

        # Déterminer le sentiment
        sentiment = "Positif" if prediction == 2 else "Négatif" if prediction == 0 else "Neutre"
        
        return {
            "original_text": data.text,
            "cleaned_text": preprocess(data.text),
            "sentiment": sentiment,
            "probability": round(probability, 2),
        }
    except ValueError as e:
        logger.error(f"Erreur : {e}")
        return {"error": str(e)}
    except Exception as e:
        logger.error(f"Erreur inattendue : {e}")
        return {"error": "Une erreur inattendue s'est produite."}


## pour le test
@app.get("/healthcheck/")
def health_check():
    try:
        sample_text = "Ceci est un test"
        _ = vectorize_text(sample_text, vectorizer)
        return {"status": "ok", "message": "Le modèle et le vectoriseur sont opérationnels"}
    except Exception as e:
        logger.error(f"Healthcheck erreur : {e}")
        return {"status": "error", "message": str(e)}