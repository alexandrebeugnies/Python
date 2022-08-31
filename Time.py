#coding:utf-8
from turtle import delay
import pygame

window_resolution = (640,480)
blue_color = (132, 180, 255)
red_color = (255, 0, 0)
black_color = (0, 0, 0)

pygame.init()

clock = pygame.time.Clock()

pygame.time.set_timer(pygame.USEREVENT, 2000)

pygame.display.set_caption("Python # 41 - gestion de temps")
window_surface = pygame.display.set_mode(window_resolution)

helena_font = pygame.font.Font("Helena.ttf", 40)
text = helena_font.render("Hello World !", True, blue_color )

#print(pygame.time.get_ticks())

window_surface.blit(text, [50, 50])
pygame.display.flip()

#pygame.time.wait(5000) # Processus en Pause 
#pygame.time.delay(5000) # Processeur en pause
"""
text = helena_font.render("Hello World !", True, red_color )
window_surface.blit(text, [50, 50])
pygame.display.flip()
"""


launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.USEREVENT:
            window_surface.fill(black_color)
            text = helena_font.render(f"{clock.get_fps():.2f} FPS", True, blue_color )
            window_surface.blit(text, [50, 50])
            pygame.display.flip()
    
    clock.tick(60) # 30 images par secondes (30 fps)
    
    #print("%.2f" % clock.get_fps())
    