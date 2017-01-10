from unrealcv import client

# X runs east-west
# Y runs north-south

ROOM_LENGTH = 1500 #11250 to -11750
ROOM_WIDTH = 1500 #11500 to -3500
ROOM_HEIGHT = 0.0

STARTING_X = 1250.0
STARTING_Y = 1250.0
STARTING_Z = 1000.0

X_TRANSLATION = 250
Y_TRANSLATION = 250

heading_north = True

client.connect() # Connect to the game
if not client.isconnected(): # Check if the connection is successfully established
  print('UnrealCV server is not running. Run the game from http://unrealcv.github.io first.')
else:
	yaw = 0.0
	z_location = STARTING_Z
	for x_offset in range(0, ROOM_WIDTH + 1, X_TRANSLATION):
		x_location = STARTING_X + (x_offset)
		
		if heading_north:
			pitch = 0.0
			starting_y_range = 0
			ending_y_range = ROOM_LENGTH + 1
			translation_y_range = Y_TRANSLATION
			heading_north = False
		else:
			pitch = 180.0
			starting_y_range = ROOM_LENGTH
			ending_y_range = 0 - 1
			translation_y_range = -1 * Y_TRANSLATION
			heading_north = True

	
		for y_offset in range(starting_y_range, ending_y_range, translation_y_range):
			y_location = STARTING_Y + y_offset
			
			print (x_location , y_location)
			
			cmd = 'vset /camera/0/location %.1f %.1f %.1f' % (x_location, y_location, z_location)
			response = client.request(cmd)
			
			cmd = 'vset /camera/0/rotation %.1f %.1f %.1f' % (270, pitch, yaw)
			response = client.request(cmd)
						
			response = client.request('vget /camera/0/lit')
			print response
			
			#cmd = 'vset /camera/0/rotation %.1f %.1f %.1f' % (300, pitch, yaw)
			#response = client.request(cmd)
			
			#response = client.request('vget /camera/0/lit')
			#print response
			

  
