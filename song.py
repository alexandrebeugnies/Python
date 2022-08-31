#coding:utf-8

import pygame
"""
<Sound>.play(loop = 0, time = 0, fadein = 0)
       .stop()
       .fadeout()
       .set_volume(0.0 -> 1.0)
       .get_volume()
       .get_lenght()
"""
window_resolution = (640, 480)
launched = True

pygame.init()
pygame.display.set_caption("Python #42 - jouer du son")
window_surface = pygame.display.set_mode(window_resolution)

forest_song = pygame.mixer.Sound("AMBForst_Foret (ID 0100)_LS.ogg")
#forest_song = pygame.mixer.Sound("AMBForst_Foret (ID 0100)_LS.ogg") on peut charger autant de sons que l'on veut
forest_song.play()

pygame.mixer.music.load("AMBForst_Foret (ID 0100)_LS.ogg")
pygame.mixer.music.play()
pygame.display.flip()

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                forest_song.stop()
                pygame.mixer.music.rewind()
                pygame.mixer.stop() # Stoppe tout les chansons
                pygame.mixer.pause()
            if event.key == pygame.K_p:    
                pygame.mixer.unpause()