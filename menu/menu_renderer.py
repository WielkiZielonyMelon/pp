import pygame


class MenuRenderer:
    DEFAULT_FONT_SIZE = 48
    ACTIVE_COLOR = (50, 255, 50)
    INACTIVE_COLOR = (50, 50, 50)

    def __init__(self, screen, menu_items_len):
        self.screen = screen
        self.menu_items_len = menu_items_len
        self.menu_spacing = self.screen.get_height() / (1 + self.menu_items_len)
        self.menu_font = pygame.font.SysFont(pygame.font.get_default_font(), self.DEFAULT_FONT_SIZE)

    def render_menu_item(self, menu_item, index, active):
        y_offset = (index + 1) * self.menu_spacing
        # Erase previous text
        self.screen.fill(pygame.Color("black"), (0, y_offset, self.screen.get_width(),
                                                 self.DEFAULT_FONT_SIZE))

        surface = self.menu_font.render(menu_item.display, True, self.ACTIVE_COLOR if active else self.INACTIVE_COLOR)

        x_offset = (self.screen.get_width() - surface.get_width()) / 2
        self.screen.blit(surface, dest=(x_offset, y_offset))
