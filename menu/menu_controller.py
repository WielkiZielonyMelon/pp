class MenuController:
    def __init__(self, menu_items, menu_renderer):
        self.menu_items = menu_items
        self.menu_renderer = menu_renderer
        self.index = 0

    def down(self):
        self.menu_renderer.render_menu_item(self.menu_items[self.index], self.index, active=False)
        self.index += 1
        if self.index >= len(self.menu_items):
            self.index = 0
        self.menu_renderer.render_menu_item(self.menu_items[self.index], self.index, active=True)

    def up(self):
        self.menu_renderer.render_menu_item(self.menu_items[self.index], self.index, active=False)
        self.index -= 1
        if self.index < 0:
            self.index = len(self.menu_items) - 1
        self.menu_renderer.render_menu_item(self.menu_items[self.index], self.index, active=True)

    def render(self):
        self.index = 0
        self.menu_renderer.render_menu_item(self.menu_items[self.index], self.index, active=True)
        self.index += 1
        while self.index < len(self.menu_items):
            self.menu_renderer.render_menu_item(self.menu_items[self.index], self.index, active=False)
            self.index += 1

        self.index = 0
