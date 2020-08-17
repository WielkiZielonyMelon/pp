class Menu:
    def __init__(self, menu_items):
        self.menu_items = menu_items
        self.current_position = 0

    def down(self):
        self.current_position += 1
        if self.current_position >= len(self.menu_items):
            self.current_position = 0

    def up(self):
        self.current_position -= 1
        if self.current_position < 0:
            self.current_position = len(self.menu_items) - 1
