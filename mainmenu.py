from map import place_list

def set_settings(screen):
    start_screen(screen)

def start_screen(screen):
    positions = [
        'menu',
        'play',
        'settings',
        'exit'
    ]
    respond = place_list(screen, positions, [0])
    if respond == 'play': 
        return
    elif respond == 'settings':
        set_settings(screen)
    elif respond == 'exit':
        exit()