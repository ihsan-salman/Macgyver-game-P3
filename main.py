#!/usr/bin/python3
# -*- coding: Utf-8 -*

# importation of moduls
import pygame
from pygame.locals import KEYDOWN, K_SPACE

from labyrinth import Labyrinth
import constants as constants
from macgyver import Macgyver
from items import Items

# Window initialization
pygame.init()
# 44 represent the black field in the down of the window
screen = pygame.display.set_mode(
	(constants.WINDOW_SIZE, constants.WINDOW_SIZE + 44))
pygame.display.set_caption(constants.WINDOW_TITLE)

# Font initialization
image_font = pygame.image.load(constants.IMAGE_FONT)
screen.blit(image_font, (0, 0))

# Win image
image_win = pygame.image.load(constants.IMAGE_WIN)

# Death image
image_death = pygame.image.load(constants.IMAGE_DEATH)

# Main loop
run = True
print('Game start')

# Instances of classes
labyrinth = Labyrinth(screen)
items = Items(labyrinth)
macgyver = Macgyver(labyrinth)
macgyver.collect(items)

while run:

	# Player action that allows interaction with the game
	for e in pygame.event.get():
		# Quit the game
		if e.type == pygame.QUIT or e.type == KEYDOWN and e.key == K_SPACE:
			run = False
			print('you quit the game')
		# Move the hero
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_RIGHT:
				macgyver.move_right()
			if e.key == pygame.K_LEFT:
				macgyver.move_left()
			if e.key == pygame.K_UP:
				macgyver.move_up()
			if e.key == pygame.K_DOWN:
				macgyver.move_down()

		# Condition to win the game
		# [0, 7] is the position of the guardian
		if [macgyver.pos_y, macgyver.pos_x] == [0, 7] and len(macgyver.bag) == 3:
			# Display a white font and the winner's image
			screen.blit(image_font, (0, 0))
			screen.blit(image_win, (0, 0))
			print('you win!')

		# Condition to lose the game
		elif [macgyver.pos_y, macgyver.pos_x] == [0, 7] and len(macgyver.bag) != 3:
			# Display a white font and the loser's image
			screen.blit(image_font, (0, 0))
			screen.blit(image_death, (0, constants.WINDOW_SIZE//4))
			print('you are dead')

	pygame.display.flip()