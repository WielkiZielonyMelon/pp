from menu.menu_item import MenuItem


polski_key = 'Polski'
polski_menu_items = [MenuItem('New game', 'Nowa gra'), MenuItem('Load game', 'Wczytaj grę'),
                     MenuItem('Scores', 'Wyniki'), MenuItem('Quit', 'Wyjdź')]

english_key = 'English'
english_menu_items = [MenuItem('New game', 'New game'), MenuItem('Load game', 'Load game'),
                      MenuItem('Scores', 'Scores'), MenuItem('Quit', 'Quit')]

deutsch_key = 'Deutsch'

language_selection_items = [MenuItem(polski_key, polski_key), MenuItem(english_key, english_key),
                            MenuItem(deutsch_key, deutsch_key)]
