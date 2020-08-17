import sys

import pygame
pygame.init()

from menu.menu_controller import MenuController


from menu.menu_item import MenuItem
from menu.menu_renderer import MenuRenderer


def get_main_menu(language):
    if language == 'Polski':
        return [MenuItem('New game', 'Nowa gra'), MenuItem('Load game', 'Wczytaj grę'), MenuItem('Scores', 'Wyniki'),
                MenuItem('Quit', 'Wyjdź')]
    if language == 'English':
        return [MenuItem('New game', 'New game'), MenuItem('Load game', 'Load game'), MenuItem('Scores', 'Scores'),
                MenuItem('Quit', 'Quit')]

    raise Exception(f'Not yet translated to {language}')


def menu_selection(menu_controller):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return MenuItem('Quit')
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
    menu_items = ([MenuItem('Polski', 'Polski'), MenuItem('English', 'English'), MenuItem('Deutsch', 'Deutsch')])
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
    language_item = menu_selection(menu_controller)
    if language_item.name == 'Quit':
        sys.exit(0)

    screen.fill((0, 0, 0))
    menu_controller = generate_main_menu_controller(screen, language_item)
    menu_controller.render()

    while True:
        menu_selected = menu_selection(menu_controller)
        if menu_selected.name == 'Quit':
            sys.exit(0)


if __name__ == "__main__":
    # execute only if run as a script
    main()
