#!/usr/bin/env python3

import World
from createPlayer import Player

def play():
	"""
	A loop to have the game continue until player is no longer alive or wins
	"""
	######################################################################################################
	# Load the instances of the world and player
	######################################################################################################

	# Loads the world map
	World.initialize_world()

	# Instantiates the player class
	player = Player()

	# Places the player in the associated room(starting) and prints the text
	room = World.tile_exists(player.location_x, player.location_y)
	print(room.intro_text())

	######################################################################################################
	# While loop for continual gameplay
	######################################################################################################

	while player.is_alive() and not player.victory:

		# Sets the room = player x,y location
		if (World.tile_exists(player.location_x, player.location_y)):
			room = World.tile_exists(player.location_x, player.location_y)

		else:
			room = World.generate_world(player.location_x, player.location_y)

		# Runs room modifications on player if there are any and describes the room
		room.modify_player(player)

		# Print for Game over
		if not player.is_alive():
			
			print("GAME OVER!!!!!\n")

		# Chack the player's state
		if player.is_alive() and not player.victory:

			######################################################################################################
			# Player input
			######################################################################################################

			print("Choose your action adventurer: \n")

			available_actions = room.available_actions()

			# Show which actions the player can perform
			for action in available_actions:
				print(action)

			action_input = input("Action: \n")

			# Verifies the action is one that corresponds to a key
			for action in available_actions:
				if action_input == action.hotkey:
					player.do_action(action, **action.kwargs)
					break



if __name__ == "__main__":
	play()

