from map import FatherList

def set_settings(screen):
    start_screen(screen)

def start_screen(screen):
    positions = [
        'menu',
        'play',
        'settings',
        'exit'
    ]
    menu = FatherList(positions, [0])
    screen = menu.place_list(screen)
    if menu.choice == 'play': 
        return
    elif menu.choice == 'settings':
        set_settings(screen)
    elif menu.choice == 'exit':
        exit()