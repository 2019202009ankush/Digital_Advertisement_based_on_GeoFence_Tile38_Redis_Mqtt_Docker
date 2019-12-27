import redis_key_value
import time, threading
import tile_38_interface
import time
WAIT_SECONDS = 5
all_unique_geo_fence=set()

def runPeriodic():
	global all_unique_geo_fence
	all_unique_geo_fence=redis_key_value.all_set_geo_fence_id()
	print("Running a Periodic_update ",flush=True)
	for x in all_unique_geo_fence:
		print(x)
		d=redis_key_value.get_value(x)
		if d['geometry']=='C':
			tile_38_interface.set_web_hook(x,d['x_coordinate_of_geofence_center'],d['y_coordinate_of_geofence_center'],d['radius'])
		elif d['geometry']=='P':
			tile_38_interface.set_web_hook_polygon(x,d['dictionary'])
	threading.Timer(WAIT_SECONDS, runPeriodic).start()

runPeriodic()
