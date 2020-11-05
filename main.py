#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame

# importation des modules

import labyrinthe
import constantes


pygame.init()

# initialisation de la fenetre

fenetre = pygame.display.set_mode((COTE_FENETRE , COTE_FENETRE))
pygame.display.set_caption(TITRE_FENETRE)




# main loop

run = True
pygame.time.Clock().tick(30)

while run:
	
	for e in pygame.event.get():
		if e.type == pygame.QUIT or e.type == KEYDOWN and e.key == K_SPACE:
        	 run = False
lab = Labyrinthe()  # instance du labyrinthe
lab.afficher(fenetre)  # instance de la methode 

pygame.display.flip()
       
			
				
       
