import redis
import time
from decimal import Decimal
from loading_environment import TILE_HOST,TILE_PORT,MQTT_HOST,MQTT_PORT
import random
import json
def set_web_hook(fence_id,x_coordinate_of_geofence_center,y_coordinate_of_geofence_center,radius):
    client=redis.Redis(host=TILE_HOST, port=int(TILE_PORT))
    mqtt_webhook='mqtt://'+MQTT_HOST+':'+str(MQTT_PORT)+'/test?qos=2&retained=0'
    result=client.execute_command('SETHOOK',fence_id,mqtt_webhook,'NEARBY','fleet','POINT',x_coordinate_of_geofence_center,y_coordinate_of_geofence_center,radius)
    if(result==1):
        print('setting set_web_hook',result,flush=True)
def set_web_hook_polygon(fence_id,dictionaryt_of_corrdinates):
    client=redis.Redis(host=TILE_HOST, port=int(9851))
    mqtt_webhook='mqtt://'+MQTT_HOST+':'+str(MQTT_PORT)+'/test?qos=2&retained=0'
    print(dictionaryt_of_corrdinates,type(dictionaryt_of_corrdinates))
    result=client.execute_command('SETHOOK',fence_id,mqtt_webhook,'INTERSECTS','fleet','FENCE','object' ,json.dumps(dictionaryt_of_corrdinates))
    if(result==1):
        print('setting set_web_hook',result,flush=True)

def setfleet(deviceId,a,b,c):
    a1=float(a)
    b1=float(b)
    client = redis.Redis(host=TILE_HOST, port=int(TILE_PORT))
    result = client.execute_command('SET', 'fleet',deviceId,'FIELD', 'campaignCode',c, 'POINT', a1, b1)
    # print (deviceId,a1,b1,c,result)
