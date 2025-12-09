import os
from dotenv import load_dotenv

load_dotenv()

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_NAME = os.environ.get('DB_NAME') 
 
# Instancia de configuración que se usa en el resto de la app
AppConfig = Config()