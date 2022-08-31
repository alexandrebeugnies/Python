
#coding:utf-8
from operator import truediv
from urllib.request import ProxyDigestAuthHandler
import pygame
import time
"""
pygame.Rect(x, y, width, height)
Rect.copy()
Rect.move()
Rect.move_ip()
Rect.inflate()
Rect.colliderect()
"""
pygame.init()
window_resolution =(640,480)
red = (255, 0, 0)
blue = (0, 75, 255)
black = (0, 0, 0)
i = 0

pygame.display.set_caption("Python #38 - l'objet rect")
window_surface = pygame.display.set_mode(window_resolution)

myrect = pygame.Rect(10, 100,25, 25)
myblock = pygame.Rect(600, 50, 20, 300)
pygame.draw.rect(window_surface, red, myrect)
pygame.draw.rect(window_surface, blue, myblock)
pygame.display.flip()

    
"""
while i < 100:
    time.sleep(.050)
    window_surface.fill(black) 
    myrect.x += 1
    myrect.y += 1
    pygame.draw.rect(window_surface, red, myrect)
    pygame.display.flip()
    i += 1
"""


launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    while not myrect.colliderect(myblock):
        time.sleep(.010)
        window_surface.fill(black)
        myrect.x += 1
        pygame.draw.rect(window_surface, red, myrect)
        pygame.draw.rect(window_surface, blue, myblock)
        pygame.display.flip()