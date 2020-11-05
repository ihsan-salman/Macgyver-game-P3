#!/usr/bin/python3
# -*- coding: Utf-8 -*


import pygame
from pygame.locals import *

# importation des modules

from labyrinthe import *
from constantes import *


pygame.init()

# initialisation de la fenetre

fenetre = pygame.display.set_mode((COTE_FENETRE , COTE_FENETRE))
pygame.display.set_caption(TITRE_FENETRE)




# main loop

run = True

while run:
	
	pygame.time.Clock().tick(30)
	
	for e in pygame.event.get():
		if e.type == pygame.QUIT or e.type == KEYDOWN and e.key == K_ESCAPE :
        	 run = False
	lab=Labyrinthe()
	lab.generer()
	lab.afficher(fenetre)

pygame.display.flip()
       
			
				
       
