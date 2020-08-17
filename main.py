import sys

import pygame

pygame.init()
resolution = (1024, 768)
screen = pygame.display.set_mode(resolution)
default_font_size = 20
menu_font = pygame.font.SysFont(pygame.font.get_default_font(), default_font_size)
active_menu_selection_color = (50, 255, 50)
inactive_menu_selection_color = (50, 50, 50)


def render_menu_item(screen, font, text, position, active):
    if active:
        surface = font.render(text, True, active_menu_selection_color)
        screen.blit(surface, dest=position)
    else:
        screen.fill(pygame.Color("black"), (position[0], position[1], 110, default_font_size))
        surface = font.render(text, True, inactive_menu_selection_color)
        screen.blit(surface, dest=position)


surfaces = [('Polski', (100, 500)), ('English', (100, 525)), ('Deutsch', (100, 550))]
current_surface_index = 0
render_menu_item(screen, menu_font, surfaces[0][0], surfaces[0][1], True)

for surface in surfaces[1:]:
    render_menu_item(screen, menu_font, surface[0], surface[1], False)

current_surface_index = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                render_menu_item(screen, menu_font, surfaces[current_surface_index][0], surfaces[current_surface_index][1],
                                 False)

                current_surface_index += 1
                if current_surface_index >= len(surfaces):
                    current_surface_index = 0
                render_menu_item(screen, menu_font, surfaces[current_surface_index][0], surfaces[current_surface_index][1],
                                 True)

            elif event.key == pygame.K_UP:
                render_menu_item(screen, menu_font, surfaces[current_surface_index][0], surfaces[current_surface_index][1],
                                 False)

                current_surface_index -= 1
                if current_surface_index < 0:
                    current_surface_index = len(surfaces) - 1

                render_menu_item(screen, menu_font, surfaces[current_surface_index][0], surfaces[current_surface_index][1],
                                 True)

        pygame.display.flip()


