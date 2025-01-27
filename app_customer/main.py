import logging
import logging.config
import yaml
from fastapi import FastAPI
from app_customer.utils import load_models, analyze_sentiment

# charger la configuration
with open('config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)
    
## configurer les logs

logging.config.fileConfig('config/logging.conf', disable_existing_loggers=False)
logger = logging.getLogger("app")

## initialisation de l'application
app = FastAPI(title=config['app']['name'], version=config['app']['version'])
logger.info('Application démarrée')


## definir les routes pour l'api 