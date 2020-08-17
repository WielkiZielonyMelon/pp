import pygame

default_font_size = 20
menu_font = pygame.font.SysFont(pygame.font.get_default_font(), default_font_size)
active_menu_selection_color = (50, 255, 50)
inactive_menu_selection_color = (50, 50, 50)


class MenuRenderer:
    def __init__(self, screen, menu):
        self.screen = screen
        self.menu = menu

    def render_menu_element(self, active):
        self.screen.fill(pygame.Color("black"), (10, self.menu.current_position*100, 110, default_font_size))
        surface = menu_font.render(self.menu.menu_items[self.menu.current_position].name, True,
                                   active_menu_selection_color if active else inactive_menu_selection_color)
        self.screen.blit(surface, dest=(10, self.menu.current_position*100))

    def down(self):
        self.render_menu_element(False)
        self.menu.down()
        self.render_menu_element(True)

    def up(self):
        self.render_menu_element(False)
        self.menu.up()
        self.render_menu_element(True)

    def render(self):
        self.menu.current_position = 0
        self.render_menu_element(True)
        self.menu.down()
        while self.menu.current_position != 0:
            self.render_menu_element(False)
            self.menu.down()
