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
    menu = FatherList()
    respond = menu.place_list(screen, positions, [0])
    if respond == 'play': 
        return
    elif respond == 'settings':
        set_settings(screen)
    elif respond == 'exit':
        exit()