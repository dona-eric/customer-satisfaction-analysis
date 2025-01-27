# Etape 1 : utiliser une image python officielle
FROM python:3.12-slim

## Definir le repertoire de travail
WORKDIR /app

# copier les fichiers du projet

COPY . /app

# installer les dependances
RUN pip install --no-cache-dir -r requirements.txt

# Port de l'application
EXPOSE 8000

# commande pour lancer l'application
CMD [ "uvicorn", "app.main.app", "--host", "0.0.0.0", "--port", "8000"]