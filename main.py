#!/usr/bin/python3
# -*- coding: Utf-8 -*


import pygame
from pygame.locals import *

# importation des modules

import labyrinthe as lb
import constantes as c
import macgyver as m

# initialisation de la fenetre

pygame.init()
fenetre = pygame.display.set_mode((c.COTE_FENETRE , c.COTE_FENETRE))
pygame.display.set_caption(c.TITRE_FENETRE)


# boucle principale

run = True

while run:
	
	
	pygame.time.Clock().tick(30)
	
	for e in pygame.event.get():
		if e.type == pygame.QUIT or e.type == KEYDOWN and e.key == K_SPACE :
        	 run = False
				
		"""instance des classes"""
		lab = lb.Labyrinthe()
		lab.generer()
		lab.afficher(fenetre)
		Mg = m.MacGyver(c.IMAGE_MACGYVER)
		
		#commande directionnelle pour déplacer 
		#le personnage dans le labyrinthe
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
       
			
				
       
