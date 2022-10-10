from quest import Quest
class Room:
	def __init__(self, name):
		"""TODO: Initialises a room. Do not change the function signature (line 2)."""
		self.name = name
		self.paths = []

	def get_name(self):
		"""TODO: Returns the room's name."""
		return self.name

	def get_short_desc(self):
		"""TODO: Returns a string containing a short description of the room. This description changes based on whether or not a relevant quest has been completed in this room.

		If there are no quests that are relevant to this room, this should return: 'There is nothing in this room.' """
		print('You are standing at the {}.'.format(self.name))
		if Quest.reward in adventurer.inventory:
			return Quest.post_quest()
		else:
			return Quest.pre_quest()
			
	def get_quest_action(self):
		"""TODO: If a quest can be completed in this room, returns a command that the user can input to attempt the quest."""
		

	def set_quest(self, q):
		"""TODO: Sets a new quest for this room."""
		#x=Quest.get_room()
		#y=str(Room.get_name())
		#if x==y:
		#	self.quest=Quest
		#else:
		#	self.quest=None
			
		#return self.quest
		
	def get_quest(self):
		"""TODO: Returns a Quest object that can be completed in this room."""
		return Quest.get_info()
		
	def set_path(self, dir, dest):
		"""TODO: Creates a path leading from this room to another."""
		self.paths.append((dir, dest))
		
	def can_go_north(self):
		self.north=False
		for path in self.paths:
			if path[0].casefold() == 'NORTH'.casefold():
				self.north = True
		return self.north
		
	def can_go_south(self):
		self.south=False
		for path in self.paths:
			if path[0].casefold() == 'SOUTH'.casefold():
				self.south = True
		return self.south
		
	def can_go_east(self):
		self.east=False
		for path in self.paths:
			if path[0].casefold() == 'EAST'.casefold():
				self.east = True
		return self.east
		
	def can_go_west(self):
		self.west=False
		for path in self.paths:
			if path[0].casefold() == 'WEST'.casefold():
				self.west = True
		return self.west
		
	def draw(self):
		"""TODO: Creates a drawing depicting the exits in each room."""
		print('')
		n=self.can_go_north()
		e=self.can_go_east()
		w=self.can_go_west()
		s=self.can_go_south()
		
		if n == True:
			print('+---------NN---------+')
		else:
			print('+--------------------+')
		print('|                    |')
		print('|                    |')
		print('|                    |')
		print('|                    |')
		
		if e == True and w == True:
			print('W                    E')
		elif e == True:
			print('|                    E')
		elif w == True:
			print('W                    |')
		else:
			print('|                    |')
			
		print('|                    |')
		print('|                    |')
		print('|                    |')
		print('|                    |')
		
		if s ==True:
			print('+---------SS---------+')
		else:
			print('+--------------------+')
		print('You are standing at the {}.'.format(self.name))
		print('There is nothing in this room.')
		#if self.quest.is_complete()==True:
		#	print(Quest.post_quest())
		#else:
		#	print(Quest.pre_quest())
			

	def move(self, dir):
		"""TODO: Returns an adjoining Room object based on a direction given. (i.e. if dir == "NORTH", returns a Room object in the north)."""
		for path in self.paths:
			if path[0] == dir:
				return path[1]
