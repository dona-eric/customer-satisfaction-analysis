#!/bin/bash

## arreter les conatiners existantes
echo "Arret des conteneurs existants..."
docker-compose down

## construction et demarrer nouveaux container
echo "construction des containers"
docker-compose build

echo "Demarrage des conteneur ..."
docker-compose up -d


# verifier les logs
echo "Verificatio, des logs ..."
docker-compose logs -f

## script pour executer : deployment/deploy.sh