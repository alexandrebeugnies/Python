import pygame
"""
pygame.FULLSCREEN
pygame.DOUBLEBUF
pygame.HWSURFACE
pygame.OPENGL
pygame.RESIZABLE
pygame.NOFRAME
"""
res = (640, 480)
pygame.init()
pygame.display.set_caption("Mon Premier Pygame")
window_surface = pygame.display.set_mode(res, pygame.RESIZABLE)

#print(pygame.get_sdl_version())
#print(pygame.display.Info())
#print(type(screen))

launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

pygame.quit() # Décharge les modules initialisés

