#coding:utf-8
from hashlib import blake2s
import pygame
"""
Surface , Rect
Rect(left, top, width, height)

"""
pygame.init()

window_resolution = (640, 480)
blue_color = (89, 152, 255)

pygame.display.set_caption("Python #36")

window_surface = pygame.display.set_mode(window_resolution)
window_surface.fill(blue_color)
black_color = (0, 0 ,0)

#pygame.draw.line(window_surface, black_color, [10,10], [100,100])
rect_form =  pygame.Rect(10, 10, 150, 65)
#pygame.draw.rect(window_surface, black_color, rect_form)

#pygame.draw.circle(window_surface, black_color, [150, 100], 50 )
coords= [(10,10),(100,10),(30,50), (40,60)]
pygame.draw.polygon(window_surface, black_color, coords )


pygame.display.flip() # Apporte un changement dans l'affichage


launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
