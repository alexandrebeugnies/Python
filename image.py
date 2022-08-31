#coding:utf-8
import pygame

pygame.init()
window_resolution = (640,480)
blank_color = (255, 255, 255)
black_color = (0 ,0 , 0)

pygame.display.set_caption("Python #37")
window_surface = pygame.display.set_mode(window_resolution)

sardegna_image = pygame.image.load("sardegna.jpg") # Retourne une surface
sardegna_image.convert()
sardegna_image.set_colorkey(blank_color)
"""'
logo = pygame.image.load("logo.png")
logo.convert_alpha() # Pour la transparence 
"""
launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    # Corps du programme
    window_surface.fill(black_color)
    window_surface.blit(sardegna_image, [10, 10])
    pygame.display.flip()