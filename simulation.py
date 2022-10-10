from room import Room
from item import Item
from adventurer import Adventurer
from quest import Quest
import sys

def read_paths(source):
	"""Returns a list of lists according to the specifications in a config file, (source).

	source contains path specifications of the form:
	origin > direction > destination.

	read_paths() interprets each line as a list with three elements, containing exactly those attributes. Each list is then added to a larger list, `paths`, which is returned."""

	paths=config_create(source, ' > ')
	
	return paths


def create_rooms(paths):
	"""Receives a list of paths and returns a list of rooms based on those paths. Each room will be generated in the order that they are found."""

	i=0
	rooms=[]
	while i<len(paths):
		x=paths[i]					# after using readlines() and split(), each element of the list is a tuple,
		y=Room(x[0])				# the third index of each element has \n at the end, so split() was used 
		z=x[2].split('\n')			# again to get the destination. 
		w=Room(z[0])
		y.set_path(x[1], w)
		rooms.append(y)
		i+=1
	
	return rooms


def generate_items(source):
	"""Returns a list of items according to the specifications in a config file, (source).

	source contains item specifications of the form:
	item name | shortname | skill bonus | will bonus
	"""

	items=config_create(source, ' | ')
	return items


def generate_quests(source, items, rooms):
	"""Returns a list of quests according to the specifications in a config file, (source).

	source contains quest specifications of the form:
	reward | action | quest description | before_text | after_text | quest requirements | failure message | success message | quest location
	"""
	
	quests=config_create(source, ' | ')

	return quests

def config_create(source, sep):
	f=open(source, 'r')
	ls=f.readlines()
	i=0
	config=[]
	while i<len(ls): 
		e=ls[i].split(sep)
		config.append(e)
		i+=1
	return config
	
# TODO: Retrieve info from CONFIG files. Use this information to make Adventurer, Item, Quest, and Room objects.


if len(sys.argv)<4 or len(sys.argv)<2:
	print("Usage: python3 simulation.py <paths> <items> <quests>")
	sys.exit()
else:	
	try:
		path_config=open(sys.argv[1])
		item_config=open(sys.argv[2])
		quest_config=open(sys.argv[3])
	except FileNotFoundError:
		print("Please specify a valid configuration file.")
		sys.exit()

paths=read_paths(sys.argv[1])
rooms=create_rooms(paths)
items=generate_items(sys.argv[2])
quests=generate_quests(sys.argv[3], items, rooms)
if len(rooms)==0:
		print('No rooms exist! Exiting program...')
		sys.exit()


# TODO: Receive commands from standard input and act appropriately.

player=Adventurer()
room=rooms[0]
room.draw()
while True:
	print('')
	command=input('>>> ')
	n=room.can_go_north()
	e=room.can_go_east()
	w=room.can_go_west()
	s=room.can_go_south()
	dir_des=room.paths[0]
	des=dir_des[1]
	
	if command.casefold() == 'QUIT'.casefold():
		print('Bye!')
		break
	
	elif command.casefold() == 'HELP'.casefold():
		print("""HELP       - Shows some available commands.
LOOK or L  - Lets you see the map/room again.
QUESTS     - Lists all your active and completed quests.
INV        - Lists all the items in your inventory.
CHECK      - Lets you see an item (or yourself) in more detail.
NORTH or N - Moves you to the north.
SOUTH or S - Moves you to the south.
EAST or E  - Moves you to the east.
WEST or W  - Moves you to the west.
QUIT       - Ends the adventure.""")
	
	elif command.casefold() == 'LOOK'.casefold() or command.casefold() == 'L'.casefold():
		room.draw()
		
	elif command.casefold() == 'QUESTS'.casefold():
		if len(quests)==0:
			print('')
			print('=== All quests complete! Congratulations! ===')
			sys.exit()
		else:
			a=0
			b=0
			while a<len(quests) and b<len(quests):
				print('#{:02d}: {:21}- {}'.format(a, quests[b][0], quests[b][2]))
				a+=1
				b+=2
				
	elif command.casefold() == 'CHECK'.casefold():
		x=input('Check what? ')
		print('')
		if x.casefold() == 'ME'.casefold():
			print(player.check_self())
		else:
			print('You don\'t have that!')
		
	elif command.casefold() == 'NORTH'.casefold() or command.casefold() == 'N'.casefold():
		if n == True:
			print('You move to the north, arriving at the {}.'.format(des.get_name()))
			x=room.move('NORTH')
			room=x
		else:
			print('You can\'t go that way.')
		
	elif command.casefold() == 'SOUTH'.casefold() or command.casefold() == 'S'.casefold():
		if s == True:
			print('You move to the south, arriving at the {}.'.format(des.get_name()))
			x=room.move('SOUTH')
			room=x
		else:
			print('You can\'t go that way.')
			
	elif command.casefold() == 'EAST'.casefold() or command.casefold() == 'E'.casefold():
		if e == True:
			print('You move to the east, arriving at the {}.'.format(des.get_name()))
			x=room.move('EAST')
			room=x
		else:
			print('You can\'t go that way.')
			
	elif command.casefold() == 'WEST'.casefold() or command.casefold() == 'W'.casefold():
		if w == True:
			print('You move to the west, arriving at the {}.'.format(des.get_name()))
			x=room.move('WEST')
			room=x
		else:
			print('You can\'t go that way.')
			
	elif command.casefold() == 'INV'.casefold():
		print('You are carrying:')
		print(player.get_inv())
		
	else:
		print('You can\'t do that.')
	
