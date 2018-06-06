# A dictionary to hold the maptiles making up the world
_world = {}

# A tuple holding the x,y grid coordinates
starting_position = (0,0)

def load_tiles():
	"""
	A function to parse the map tiles, works by parsing based off tabs
	 puts the parsed information into the _world dict

	Output:
		Loaded the input text into the _world object
	"""
	with open('resources/map.txt', mode = 'r') as MAP_FILE:
		rows = MAP_FILE.readlines()

	# Sets the max value to the number of tabs in the first row
	# Assumes all rows have the same number of tabs
	x_max = len(rows[0].split('\t'))

	for y in range(len(rows)):
		cols = rows[y].split('\t')

		for x in range(x_max):
			tile_name = cols[x].replace('\n', '')

			if tile_name == 'StartingRoom':
				global starting_position
				starting_position = (x,y)

			if tile_name == '' :
				_world[(x, y)] = None 

			else:
				_world[(x, y)] = getattr(__import__('MapTiles'), tile_name)(x,y)



def tile_exists(x, y):
	"""
	Check if there is a tile at the coordinate x,y

	Input:
		x <int>
		y <int>

	Output:
		value of x,y key in world dict
	"""
	return _world.get((x,y))
