import sys

import pygame

from menu.menu_controller import MenuController

pygame.init()

from menu.menu_item import MenuItem
from menu.menu_renderer import MenuRenderer

resolution = (1024, 768)
screen = pygame.display.set_mode(resolution)

menu_items = ([MenuItem('Polski'), MenuItem('English'), MenuItem('Deutsch')])
menu_renderer = MenuRenderer(screen, len(menu_items))
menu_controller = MenuController(menu_items, menu_renderer)
menu_controller.render()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                menu_controller.down()
            elif event.key == pygame.K_UP:
                menu_controller.up()
            elif event.key == pygame.K_ESCAPE:
                sys.exit(0)

        pygame.display.flip()


