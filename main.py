import sys

import pygame
pygame.init()

from menu.menu import Menu
from menu.menu_item import MenuItem
from menu.menu_renderer import MenuRenderer

resolution = (1024, 768)
screen = pygame.display.set_mode(resolution)

menu = Menu([MenuItem('Polski'), MenuItem('English'), MenuItem('Deutsch')])
menu_renderer = MenuRenderer(screen, menu)
menu_renderer.render()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                menu_renderer.down()
            elif event.key == pygame.K_UP:
                menu_renderer.up()
            elif event.key == pygame.K_ESCAPE:
                sys.exit(0)

        pygame.display.flip()


