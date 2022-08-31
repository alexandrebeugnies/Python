#coding:utf-8

import pygame

"""
arial_font.set_bold()
arial_font.set_italic()
arial_font.set_underline()

Pour un objet, on parle de méthode;
"""
pygame.init()
window_resolution = (640,480)
blank = (255, 255, 255)

pygame.display.set_caption("Python #39")
window_surface = pygame.display.set_mode(window_resolution)


#arial_font = pygame.font.SysFont("arial", 100)
helena_font = pygame.font.Font("Helena.ttf", 100)
hello_text = helena_font.render("Hello World !", True, blank )
#hello_text = arial_font.render("Hello World !", False, blank )  # rend une surface

window_surface.blit(hello_text, [10, 10])
pygame.display.flip()
#print(pygame.font.get_fonts())

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False