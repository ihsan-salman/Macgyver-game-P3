#!/usr/bin/python3
# -*- coding: Utf-8 -*

# importation of moduls
import pygame
from pygame.locals import *

from labyrinth import Labyrinth
import constants as constants
from macgyver import Macgyver

# Window initialization

pygame.init()
screen = pygame.display.set_mode((constants.WINDOW_SIZE, constants.WINDOW_SIZE))
pygame.display.set_caption(constants.WINDOW_TITLE)
image_font = pygame.image.load(constants.IMAGE_FONT)


# Main loop 

run = True
print('Game start')
pygame.time.Clock().tick(30)
screen.blit(image_font, (0, 0))
	
# Instances of classes
lab = Labyrinth(screen)
mac = Macgyver(lab)

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
			
	
	pygame.display.flip()