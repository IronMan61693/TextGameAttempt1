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
		self.my_gold_pouch = Items.GoldPouch(15)
		self.inventory = [self.my_gold_pouch]
		self.guesses_remaining = 1
		self.location_x, self.location_y =  World.starting_position
		self.victory = False



	def add_to_pouch(self, coin_value):
		self.my_gold_pouch.add_to_me(coin_value)




	def is_alive(self):
		"""
		bool for alive condition determined by hp
		
		Output <bool>
		"""
		return self.guesses_remaining > 0




	def print_inventory(self):
		"""
		print statement for player inventory

		Output:
			print statement
		"""
		print("You have beaten {} tiles!".format(World.how_many_tile()))
		print("You have {} guesses remaining".format(self.guesses_remaining))

		print("And you are located at {}, {}".format(self.location_x, self.location_y))
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
		if not World.tile_exists(self.location_x, self.location_y):
			World.generate_world(self.location_x, self.location_y)
		print(World.tile_exists(self.location_x, self.location_y).intro_text())



	def move_north(self):
		"""
		use move() method to move character decreasing in dy

		Output:
			move(0, -1)
		"""
		self.move(dx = 0, dy = 1)



	def move_south(self):
		"""
		use move() method to move character increasing in dy

		Output:
			move(0, -1)
		"""
		self.move(dx = 0, dy = -1)



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



	def guess(self, enemy):
		"""
		Uses the weapon with the highest damage in the
		 player inventory to decrement hp of enemy

		Input:
			enemy <Enemy>

		Output:
			modifies enemy instance
			print statement
		"""
		player_guess = input('Please type your guess! ')
		player_guess = player_guess.strip()
		enemy.guess_made(player_guess)
		answer = "wrong"
		if enemy.correct:
			answer = "right"

		print("You guessed {} against the question {} and your guess was {}!".format(player_guess, enemy.question, answer))
	
		if not enemy.is_alive():
			print("You have successfully answered the question!".format(enemy.question))

		else:
				print("You have {} attempts for this question remaining.".format(enemy.guesses))
				if (enemy.out_of_guesses()):
					print("You are out of attempts for this room, you are being teleported to a random room")



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
		self.guesses_remaining = 0




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