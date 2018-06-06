import Items, World
import random

class Player():
	"""
	The player class uses Items class
	 Sets the player to the starting position described in World

	Variables:
		inventory [<Items>]
		hp <int>
		location_x <int>
		location_y <int>
		victory <bool>

	Methods:
		is_alive() bool for alive condition determined by hp
		print_inventory() print statement for player inventory
		move(dx, dy) basic move method, dx and dy are change in x and y
		move_north() calls move dy = -1
		move_south() calls move dy = 1
		move_east() calls move dx = 1
		move_west() calls move dx = -1
		attack(enemy) finds the best weapon in inventory
		 and decrements enemy hp by the weapon.damage
		flee(tile) Allows player to move to random adjacent tile
		 when in combat
		do_action(action, kwargs) uses Action class to run
		 the action's method

	"""
	def __init__(self):
		self.inventory = [Items.Gold(15), Items.Fist()]
		self.hp = 100
		self.location_x, self.location_y =  World.starting_position
		self.victory = False



	def is_alive(self):
		"""
		bool for alive condition determined by hp
		
		Output <bool>
		"""
		return self.hp > 0



	def print_inventory(self):
		"""
		print statement for player inventory

		Output:
			print statement
		"""
		for item in self.inventory:
			print(item, '\n')



	def move(self, dx, dy):
		"""
		basic move method, dx and dy are change in x and y

		Input:
			dx <int>
			dy <int>

		Output:
			print statement for tile entered
		"""
		self.location_x += dx
		self.location_y += dy
		print(World.tile_exists(self.location_x, self.location_y).intro_text())



	def move_north(self):
		"""
		use move() method to move character decreasing in dy

		Output:
			move(0, -1)
		"""
		self.move(dx = 0, dy = -1)



	def move_south(self):
		"""
		use move() method to move character increasing in dy

		Output:
			move(0, -1)
		"""
		self.move(dx = 0, dy = 1)



	def move_east(self):
		"""
		use move() method to move character increasing in dx

		Output:
			move(0, -1)
		"""
		self.move(dx = 1, dy = 0)



	def move_west(self):
		"""
		use move() method to move character decreasing in dx

		Output:
			move(0, -1)
		"""
		self.move(dx = -1, dy = 0)



	def attack(self, enemy):
		"""
		Uses the weapon with the highest damage in the
		 player inventory to decrement hp of enemy

		Input:
			enemy <Enemy>

		Output:
			modifies enemy instance
			print statement
		"""
		best_weapon = None
		max_dmg = 0

		# Finds the most damage weapon in inventory
		for weap in self.inventory:
			if isinstance(weap, Items.Weapon):
				if weap.damage > max_dmg:
					max_dmg = weap.damage
					best_weapon = weap

		print("You used your {} against the {}!".format(best_weapon.name, enemy.name))
		enemy.hp -= best_weapon.damage

		if not enemy.is_alive():
			print("You killed the {}!".format(enemy.name))

		else:
			print("The {}'s HP is now {}.".format(enemy.name, enemy.hp))



	def flee(self, tile):
		"""
		Allows player to move to random adjacent tile in combat

		Input:
			tile <MapTile>
		"""
		available_moves = tile.adjacent_moves()
		r = random.randint(0,len(available_moves) -1)
		self.do_action(available_moves[r])



	def quit(self):
		"""
		Allows player to exit the game
		"""
		print("You have decided to leave the adventure early. See you next time!")
		self.hp = 0




	def do_action(self, action, **kwargs):
		"""
		Allows Action to implement Player methods

		Input:
			action <Action>
			kwargs <char> <- keyboard input
		"""
		action_method = getattr(self, action.method.__name__)

		# Verifies valid input
		if action_method:
			action_method(**kwargs)