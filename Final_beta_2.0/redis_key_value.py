
import redis
import json
from loading_environment import REDIS_HOST,REDIS_PORT
r = redis.Redis(host=REDIS_HOST,port=REDIS_PORT)

def get_value(geofence_id):
	return json.loads(r.get(geofence_id))

def set_value(geofence_id,name_of_geofence,x_coordinate_of_geofence_center,y_coordinate_of_geofence_center,radius,is_geoFence_set,payload,campaign_id):
	 r.set(geofence_id,json.dumps({'name_of_geofence':name_of_geofence,'x_coordinate_of_geofence_center':x_coordinate_of_geofence_center,'y_coordinate_of_geofence_center':y_coordinate_of_geofence_center,'radius':radius,'is_geoFence_set':is_geoFence_set,'payload':payload,'campaign_id':campaign_id}))

def all_geo_fence_id():
	lis=[k.decode("utf-8") for k  in r.scan_iter("*")]
	return(lis)

def all_set_geo_fence_id():
	lis1=all_geo_fence_id()
	list2 = set()
	for key in lis1:
		if key not in list2:
			dictionary=get_value(key)
			if dictionary['is_geoFence_set']=='T':
				list2.add(key)
	return (list2)

def all_set_geo_fence_id_and_campaign_code_pair():
	l=set()
	l=all_set_geo_fence_id()
	lis=[]
	for key in l:
		dictionary=get_value(key)
		lis.append([key,dictionary['campaign_id']])
	return (lis)

def make_geo_fence_inactive(geofence_id):
	dictionary=get_value(geofence_id)
	dictionary['is_geoFence_set']='F'
	r.set(geofence_id,json.dumps(dictionary))

def make_geo_fence_active(geofence_id):
	dictionary=get_value(geofence_id)
	dictionary['is_geoFence_set']='T'
	r.set(geofence_id,json.dumps(dictionary))
