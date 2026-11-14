# メインメニュー（play / settings / exit）
from map import FatherList

# 設定画面（未実装のため、メインメニューに戻る）
def set_settings(screen):
    start_screen(screen)

# メインメニューを表示し、選択に応じて処理する
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