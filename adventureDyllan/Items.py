class Item():
	"""
	The base class for all items in the game

	Variables:
		name <str>
		description <str>
		value <int>

	Methods:
		__init__(self, name, description, value): Initializes the base class
		__str__(self): returns a string with the information of the item
		is_looted(self): Checks if the item is_looted
		set_looted(self): Sets the item as looted
	"""
	def __init__(self, name, description, value, looted = False):
		"""
		Input: 
			name <str>
			description <str>
			value <int>
		"""
		self.name = name
		self.description = description
		self.value = value
		self.looted = looted

	def __str__(self):
		"""
		Redefined __str__ to have useful information when call print on the object

		Input:
			None

		Output:
			<str> <- Object information
		"""
		return "{}\n====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

	def is_looted(self):
		"""
		Checks if the item is_looted
		"""
		return self.looted

	def set_looted(self):
		"""
		Sets the item to looted
		"""
		self.looted = True



class Gold(Item):
	"""
	Extends the Item class specifically to gold, as a means of currency in the game
	 This class holds the value of gold pieces as amt
	 Is a subclass of superclass Item

	Variables:
		amt <int>
		name <str>
		description <str>
		value <int>

	Methods:
		__init__(self, amt): Initializes as subclass of Item and add amt variable
	"""
	def __init__(self, amt):
		"""
		Input: 
			amt <int>
		"""

		self.amt = amt
		super().__init__(name = "Gold",
						 description = "A round shiny coin with {} stamped on the front".format(str(self.amt)),
						 value = self.amt)



# class Weapon(Item):
# 	"""
# 	Extends the Item class, this will be another base class for all specific
# 	 weapons in the game

# 	Variables:
# 		name <str>
# 		description <str>
# 		value <int>
# 		damage <int>

# 	Methods:
# 		__init__(self, name, description, value, damage) calls Item init, adds damage variable
# 		__str__(self): returns a string with the information of the weapon
# 	"""
# 	def __init__(self, name, description, value,  damage):
# 		"""
# 		Input: 
# 			name <str>
# 			description <str>
# 			value <int>
# 			damage <int>
# 		"""
# 		self.damage = damage
# 		super().__init__(name, description, value)

# 	def __str__(self):
# 		"""
# 		Redefined __str__ to have useful information when call print on the object

# 		Output:
# 			<str> <- Object information
# 		"""
# 		return "{}\n====\n{}\nValue: {}\nDamage: {}\n".format(self.name, self.description, self.value, self.damage)



# class Fist(Weapon):
# 	"""
# 	A specific weapon Fist subclass of Weapon

# 	Variables:
# 		name <str>
# 		description <str>
# 		value <int>
# 		damage <int>

# 	Methods:
# 		__init__(self): Initializes as subclass of Weapon
# 	"""
# 	def __init__(self):
# 		"""
# 		Input: 
# 			name <str>
# 			description <str>
# 			value <int>
# 			damage <int>
# 		"""
# 		super().__init__(name = "Fist",
# 						 description = "Your bruised and battered fist.",
# 						 value = 0,
# 						 damage = 3)



# class Rock(Weapon):
# 	"""
# 	A specific weapon Rock subclass of Weapon

# 	Variables:
# 		name <str>
# 		description <str>
# 		value <int>
# 		damage <int>

# 	Methods:
# 		__init__(self): Initializes as subclass of Weapon
# 	"""
# 	def __init__(self):
# 		"""
# 		Input: 
# 			name <str>
# 			description <str>
# 			value <int>
# 			damage <int>
# 		"""
# 		super().__init__(name = "Rock",
# 						 description = "A fist-sized rock, suitable for bludgeoning heads",
# 						 value = 0,
# 						 damage = 5)



# class Dagger(Weapon):
# 	"""
# 	A specific weapon Dagger subclass of Weapon

# 	Variables:
# 		name <str>
# 		description <str>
# 		value <int>
# 		damage <int>

# 	Methods:
# 		__init__(self): Initializes as subclass of Weapon
# 	"""
# 	def __init__(self):
# 		"""
# 		Input: 
# 			name <str>
# 			description <str>
# 			value <int>
# 			damage <int>
# 		"""
# 		super().__init__(name = "Dagger",
# 						 description = "A rust covered dagger, slightly more dangerous than a rock",
# 						 value = 10,
# 						 damage = 10)
