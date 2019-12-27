import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
REDIS_HOST=str(os.environ.get("REDIS_HOST"))
REDIS_PORT=(os.environ.get("REDIS_PORT"))
MQTT_HOST=str(os.environ.get("MQTT_HOST"))
MQTT_PORT=(os.environ.get("MQTT_PORT"))
WSS_ADD=str(os.environ.get("WSS_ADD"))
TILE_HOST=str(os.environ.get("TILE_HOST"))
TILE_PORT=(os.environ.get("TILE_PORT"))
# print(REDIS_HOST,REDIS_PORT,MQTT_HOST,MQTT_PORT,WSS_ADD,TILE_PORT,TILE_HOST)
