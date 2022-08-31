#coding:utf-8

import pygame

window_resolution = (640,480)
"""
white_color = (255, 255, 255)
black_color = (0, 0, 0)
"""


pygame.init()
pygame.display.set_caption("Python # 40 - évènements")
window_surface = pygame.display.set_mode(window_resolution) #pygame.RESIZABLE


"""
helena_font = pygame.font.Font("Helena.ttf", 100)
dimensions_text = helena_font.render("{}".format(window_resolution), True, white_color )
window_surface.blit(dimensions_text, [10, 10])
pygame.display.flip()
"""

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.MOUSEMOTION:
            print("{}".format(event.pos))

            """  elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Haut")
            elif event.key == pygame.K_DOWN:
                print("BAS")
            elif event.key == pygame.K_LEFT:
                print("Gauche")
            elif event.key == pygame.K_RIGHT:
                print("Droite")
            else:
                print("Autre touche")"""
        
            """event.type == pygame.VIDEORESIZE:
                window_surface.fill(black_color)
                dimensions_text = helena_font.render("{}x{}".format(event.w, event.h), True, white_color )
                window_surface.blit(dimensions_text, [10, 10])
                pygame.display.flip()"""
      