#!/usr/bin/python3
# -*- coding: Utf-8 -*


import pygame
from pygame.locals import *

# importation des modules

from labyrinthe import *
from constantes import *
from macgyver import *

pygame.init()

# initialisation de la fenetre

fenetre = pygame.display.set_mode((COTE_FENETRE , COTE_FENETRE))
pygame.display.set_caption(TITRE_FENETRE)




# main loop

run = True

while run:
	
	
	pygame.time.Clock().tick(30)
	
	
	for e in pygame.event.get():
		if e.type == pygame.QUIT or e.type == KEYDOWN and e.key == K_SPACE :
        	 run = False
		lab = Labyrinthe()
		lab.generer()
		lab.afficher(fenetre)
		Mg = MacGyver()
		if e.type == KEYDOWN and e.key == K_RIGHT:
			Mg.se_deplace('droite')
		elif  e.type == KEYDOWN and e.key == K_LEFT:
			Mg.se_deplace('gauche')
		elif e.type == KEYDOWN and e.key == K_UP:
			Mg.se_deplace('haut')
		elif e.type == KEYDOWN and e.key == K_DOWN:
			Mg.se_deplace('bas')	
			
		# condition de victoire
		if lab.structure[Mg.case_y][Mg.case_x] == 'a':
			run = False
	

pygame.display.flip()
       
			
				
       
