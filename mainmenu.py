import cutie

def start_screen():
    menu_choice = [
    "main menu",
    "play",
    "settings",
    "exit",
    ]
    #тут определяем заголовки, которые нельзя будет выбрать
    captions = [0]
    #получаем выбор от игрока
    choice = cutie.select(menu_choice, caption_indices=captions, selected_index=1)
    if choice == 1:
        return
    elif choice == 2:
        print("\033[H\033[J")
        print('а нет настроек еще')
        start_screen()
    elif choice == 3:
        exit()