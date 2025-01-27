import joblib, pickle
import nltk, re, os, sys, string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

## fonction de pretraitement 

def preprocess(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub(r"\d+", "", text) ## suppression des chiffres
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    
    ## pour transformer le texte
    ## tokenizer le texte
    token = word_tokenize(text)
    ## supprimer les stopwords
    stop_words = set(stopwords.words("english")) | set(stopwords.words('french'))
    tokens=[word for word in token if word not in stop_words]  # Supprimer les stopwords
    lematizer = WordNetLemmatizer()
    tokens= [lematizer.lemmatize(w) for w in tokens]
    texted = " ".join(tokens)
    return  texted


# Fonction pour créer un vectoriseur TF-IDF
def create_vectorizer(max_features=10000):
    """
    Crée un TfidfVectorizer configuré avec des paramètres prédéfinis.
    """
    return TfidfVectorizer(max_features=max_features, analyzer="word", min_df=5.0)

# Fonction pour vectoriser un texte
def vectorize_text(text, vectorizer):
    """
    Nettoie et transforme le texte en vecteur TF-IDF.
    """
    cleaned_text = preprocess(text)  # Nettoyer le texte
    return vectorizer.transform([cleaned_text])  # Vectoriser