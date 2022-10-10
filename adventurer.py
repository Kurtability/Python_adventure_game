from item import Item
class Adventurer:
	def __init__(self):
		"""TODO: Initialises an adventurer object."""
		self.skill=5
		self.will=5
		self.inventory=[]
		self.bonus_skill=0
		self.bonus_will=0
		
	def get_inv(self):
		"""TODO: Returns the adventurer's inventory."""
		if len(self.inventory)==0:
			return 'Nothing.'
		else:
			return self.inventory

	def get_skill(self):
		"""TODO: Returns the adventurer's skill level. Whether this value is generated before or after item bonuses are applied is your decision to make."""
		return self.skill

	def get_will(self):
		"""TODO: Returns the adventurer's will power. Whether this value is generated before or after item bonuses are applied is your decision to make."""
		return self.will

	def take(self, item):
		"""TODO: Adds an item to the adventurer's inventory."""
		self.inventory.append(item)

	def check_self(self):
		"""TODO: Shows adventurer stats and all item stats."""
		x=int(self.total_skill_bonus())
		y=int(self.total_will_bonus())
		a=x+self.get_skill()
		b=y+self.get_will()
		if a<0:
			a=0
		if b<0:
			b=0
		print("""You are an adventurer, with a SKILL of {} and a WILL of {}.
You are carrying:
""".format(self.skill, self.will))
		print(self.get_inv())
		print('')
		return('With your items, you have a SKILL level of {} and a WILL power of {}.'.format(a, b))

	def total_skill_bonus(self):
		if len(self.inventory)==0:
			self.bonus_skill=0
			return self.bonus_skill
		else:
			for i in [0,(len(self.inventory)-1)]:
				x=self.inventory[i]
				self.bonus_skill+=x.skill_bonus()
				return self.bonus_skill
			else:	
				return self.bonus_skill
			
	def total_will_bonus(self):
		if len(self.inventory)==0:
			self.bonus_will=0
			return self.bonus_will
		else:
			for i in [0,(len(self.inventory)-1)]:
				x=self.inventory[i]
				self.bonus_will+=x.will_bonus()
			return self.bonus_will

	def skill_total(self):
		self.total_skill=self.skill + self.total_skill_bonus()
		return self.total_skill

	def will_total(self):
		self.total_will=self.will + self.total_will_bonus()
		return self.total_will
