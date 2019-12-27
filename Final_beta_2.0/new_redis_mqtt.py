import json
import traceback
import paho.mqtt.client as mqtt
import redis_key_value
import base64
import asyncio
from loading_environment import WSS_ADD,MQTT_HOST,MQTT_PORT
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("test")

async def send_message(message):
    uri = WSS_ADD
    import websockets
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)

unique_devices_that_are_inside = set()

def on_message(client, userdata, msg):
    v=msg.payload.decode()
    jmsg = json.loads(v)
    campaignCode = jmsg["fields"]["campaignCode"]
    device_id = jmsg["id"].split('/')[1]
    detect=jmsg["detect"]
    geofence_id=jmsg["hook"]
    if detect=='inside':
        if device_id not in unique_devices_that_are_inside:
            unique_devices_that_are_inside.add(device_id)
            print(' [+] {} unique_devices_that_are_inside so far: {}'.format(len(unique_devices_that_are_inside), unique_devices_that_are_inside),flush=True)
            from periodic_update import all_unique_geo_fence
            print (all_unique_geo_fence)
            if geofence_id in all_unique_geo_fence:
                dictionary=redis_key_value.get_value(geofence_id)
                if campaignCode!=dictionary["campaign_id"]:
                    print("--- Sending ---", flush=True)
                    try:
                        payload_dictionary = dictionary["payload"]
                        message1=json.dumps({
                                    "Topic": "device/" + device_id + "/geofence/"+geofence_id,
                                    "Payload": base64.b64encode(json.dumps(payload_dictionary).encode()).decode()
                                   })
                        print(json.dumps(payload_dictionary, indent=2))
                        print(message1)
                        asyncio.get_event_loop().run_until_complete(send_message(message1))
                        print("sent")
                    except Exception as e:
                        traceback.print_exc()

    else:
        if device_id in unique_devices_that_are_inside:
            unique_devices_that_are_inside.remove(device_id)
            print(' [-] {} unique_devices_that_are_inside so far: {}'.format(len(unique_devices_that_are_inside), unique_devices_that_are_inside))
            print(device_id, campaign_id,detect,x_coordinate,y_coordinate)


client = mqtt.Client()
client.connect(MQTT_HOST,int(MQTT_PORT),60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
