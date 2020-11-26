#!/usr/bin/python3
# -*- coding: Utf-8 -*

# importation of moduls
import pygame
from pygame.locals import *

from labyrinth import Labyrinth
import constants as constants
from macgyver import Macgyver
from items import Items 

# Window initialization

pygame.init()
screen = pygame.display.set_mode((constants.WINDOW_SIZE, constants.WINDOW_SIZE))
pygame.display.set_caption(constants.WINDOW_TITLE)
image_font = pygame.image.load(constants.IMAGE_FONT)
screen.blit(image_font, (0, 0))


# Main loop 

run = True
print('Game start')
	
# Instances of classes

lab = Labyrinth(screen)
mac = Macgyver(lab)
it = Items(lab)
mac.collect(it)
while run:

	# Player action that allows interaction with the game
	for e in pygame.event.get():
		# Quit the game
		if e.type == pygame.QUIT or e.type == KEYDOWN and e.key == K_SPACE :
			run = False
			print('you quit the game')
		# Move the hero 
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_RIGHT :
				mac.move_right()
			if e.key == pygame.K_LEFT :
				mac.move_left()
			if e.key == pygame.K_UP :
				mac.move_up()
			if e.key == pygame.K_DOWN :
				mac.move_down()

		# Condition to win the game
		#[0, 7] is the position of the guardian
		if [mac.pos_y, mac.pos_x] == [0,7] and len(mac.bag) == 3:
			print('you win!')
			run = False
		# Condition to lose the game	
		elif [mac.pos_y, mac.pos_x] == [0, 7]:
			print('you are dead')
			run = False
	
	pygame.display.flip()