 ### Projet : Analyse de Satisfaction des Clients ###

 ### Structure du projet

    1** app/ : contient le coeur de l'application

        . main.py : est le point d'entrée principal

        .routes.py: definir les routes de l'api fait à base de FastAPI

        .utils.py : les fonctions utilitaires comme le pretraitement de texte ou la gestion des fichiers

        . models/ : est le dossier qui contient les modèles de classification des sentiments et autres models

    2** config/ : stocke toutes les configurations

        . config.yaml : inclure les paramètres comme les chemins des modeles , les configurations des api et autres ;
        . logging.conf : est un fichier pour configurer les logs de l'application

    3** data/ : dossier d'organisation des données

        . raw/ : contiennt les données brutes à importer

        . processed/ : contient les données après nettoyage pretes pour les modèles

        . results/ : contient les resultats de la modelisation
    
    4** Analyse/ :: Cahiers jupyter pour l'analyse exploratoire des données

    5** tests/ : contient les tests unitaires
        . test_app.py  : ce fichier est utilisé pour verifier que le modèle renvoie des scores cohérents
                        et fonctionne correectement
    
    6** requirements.txt : c'est un fichier important pour tout structure de project afin de gerer les problèmes de dépendances lord du deploiement

    7** Dockerfile : contient les instructions pour conteneuriser l'application
    8** deployment/
        . deploy.sh : c'est un fichier qui sera utilisé pour automatiser le deploiement de l'application sur un server
        . wsgi.py : est le server WSGI pour exécuter l'application en production (Gunicorn)
    
    