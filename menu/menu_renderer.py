import pygame

default_font_size = 20
menu_font = pygame.font.SysFont(pygame.font.get_default_font(), default_font_size)
active_menu_selection_color = (50, 255, 50)
inactive_menu_selection_color = (50, 50, 50)


class MenuRenderer:
    def __init__(self, screen, menu_items_len):
        self.screen = screen
        self.menu_items_len = menu_items_len
        self.menu_spacing = self.screen.get_height() / (1 + self.menu_items_len)

    def render_menu_item(self, menu_item, index, active):
        self.screen.fill(pygame.Color("black"), (0, (index + 1) * self.menu_spacing, self.screen.get_width(),
                                                 default_font_size))
        surface = menu_font.render(menu_item.name, True,
                                   active_menu_selection_color if active else inactive_menu_selection_color)
        self.screen.blit(surface, dest=(10, (index + 1) * self.menu_spacing))