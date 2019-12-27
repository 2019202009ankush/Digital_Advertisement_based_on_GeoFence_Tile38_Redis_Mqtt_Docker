
import redis
import json
r = redis.Redis(host="0.0.0.0",port=6379)


def set_value(geofence_id,name_of_geofence,geometry,x_coordinate_of_geofence_center,y_coordinate_of_geofence_center,radius,is_geoFence_set,payload,campaign_id):
	r.set(geofence_id,json.dumps({'name_of_geofence':name_of_geofence,'geometry':geometry,'x_coordinate_of_geofence_center':x_coordinate_of_geofence_center,'y_coordinate_of_geofence_center':y_coordinate_of_geofence_center,'radius':radius,'is_geoFence_set':is_geoFence_set,'payload':payload,'campaign_id':campaign_id}))
def set_value_poly(geofence_id,name_of_geofence,geometry,dictionary,is_geoFence_set,payload,campaign_id):
	print(REDIS_PORT)
	r.set(geofence_id,json.dumps({'name_of_geofence':name_of_geofence,'geometry':geometry,'dictionary':dictionary,'is_geoFence_set':is_geoFence_set,'payload':payload,'campaign_id':campaign_id}))
print("Enter the details of geofence")
print("Enter the geofence_id")
geofence_id=input()
print("Enter the geofence_name")
name_of_geofence=input()
print("Enter geometry type of geo fence------Enter C for circle and P for polygon")
geometry=input()
dictionary={}
outer_list=[]
middle_list=[]
if geometry=='P':
	while 1:
		temp_list=[]
		print(" latitude  longitude ...Enter -1 -1 to stop")
		longitude=input()
		latitude=input()

		print(latitude,longitude)
		if(latitude=='-1' or longitude=='-1'):
			break
		temp_list.append(float(latitude))
		temp_list.append(float(longitude))
		middle_list.append(temp_list)
		print(middle_list,temp_list)
		# temp_list.clear()
	outer_list.append(middle_list)
	print(outer_list)
	dictionary['type']='Polygon'
	dictionary['coordinates']=outer_list
elif geometry=='C':
	print("Enter the x coordinate of center")
	x_coordinate_of_geofence_center=input()
	print("Enter the y coordinate of center")
	y_coordinate_of_geofence_center=input()
	print("Enter the radius")
	radius=input()
else:
	print("only ploygon and circle are suppoerted")
	exit()
print("Enter wether you want to set it")
is_geoFence_set=input()
print("Enter the payload")
payload=input()
print("Enter the campaign_id")
campaign_id=input()
if(geometry=="C"):
	set_value(geofence_id,name_of_geofence,geometry,x_coordinate_of_geofence_center,y_coordinate_of_geofence_center,radius,is_geoFence_set,payload,campaign_id)
elif geometry=="P":
	set_value_poly(geofence_id,name_of_geofence,geometry,dictionary,is_geoFence_set,payload,campaign_id)
