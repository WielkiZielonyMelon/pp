import sys

import pygame

from menu.menu_controller import MenuController

pygame.init()

from menu.menu_item import MenuItem
from menu.menu_renderer import MenuRenderer


def get_main_menu(language):
    if language == 'Polski':
        return [MenuItem('Nowa gra'), MenuItem('Wczytaj grę'), MenuItem('Wyniki'), MenuItem('Wyjdź')]
    if language == 'English':
        return [MenuItem('New game'), MenuItem('Load game'), MenuItem('Scores'), MenuItem('Quit')]

    raise Exception(f'Not yet translated to {language}')


def main_menu_loop(menu_controller):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.key == pygame.K_DOWN:
                    menu_controller.down()
                elif event.key == pygame.K_UP:
                    menu_controller.up()
                elif event.key == pygame.K_RETURN:
                    print("Not yet implemented")
                    sys.exit(0)
            pygame.display.flip()


def language_selection(menu_controller):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.key == pygame.K_DOWN:
                    menu_controller.down()
                elif event.key == pygame.K_UP:
                    menu_controller.up()
                elif event.key == pygame.K_RETURN:
                    return menu_controller.get_menu_item()

            pygame.display.flip()


def generate_language_menu_controller(screen):
    menu_items = ([MenuItem('Polski'), MenuItem('English'), MenuItem('Deutsch')])
    menu_renderer = MenuRenderer(screen, len(menu_items))
    menu_controller = MenuController(menu_items, menu_renderer)

    return menu_controller


def generate_main_menu_controller(screen, language_item):
    menu_items = get_main_menu(language_item.name)
    menu_renderer = MenuRenderer(screen, len(menu_items))
    menu_controller = MenuController(menu_items, menu_renderer)

    return menu_controller


def main():
    resolution = (1024, 768)
    screen = pygame.display.set_mode(resolution)

    menu_controller = generate_language_menu_controller(screen)
    menu_controller.render()

    language_item = language_selection(menu_controller)
    screen.fill((0, 0, 0))

    menu_controller = generate_main_menu_controller(screen, language_item)

    menu_controller.render()
    pygame.display.flip()

    while True:
        main_menu_loop(menu_controller)


if __name__ == "__main__":
    # execute only if run as a script
    main()
