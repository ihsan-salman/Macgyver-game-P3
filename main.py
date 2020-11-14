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
screen = pygame.display.set_mode((constants.WINDOW_SIZE , constants.WINDOW_SIZE))
pygame.display.set_caption(constants.WINDOW_TITLE)
image_font = pygame.image.load(constants.IMAGE_FONT)


# Main loop 

run = True
print('Game start')
while run:
	
	pygame.time.Clock().tick(30)
	screen.blit(image_font, (0, 0))
	
	
	# Instances of classes
	lab = Labyrinth(screen)
	mac = Macgyver(lab)

	# player action that allows interaction with the game
	for e in pygame.event.get():
		if e.type == pygame.QUIT or e.type == KEYDOWN and e.key == K_SPACE :
			run = False
			print('you quit the game')
		elif e.type == KEYDOWN and e.key == K_RIGHT :
			mac.move_right()
			pygame.display.flip()

		
	pygame.display.flip()
	
	

       
			
				
       
