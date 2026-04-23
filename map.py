# import sidescreen as side
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
from time import sleep

# задаем переменные
karta = []
x_box = []
right_dis = []
hero = "$"
enemy = "!"
res = 8

#
def side_screen(screen):
    x = res * 4 + 2
    for i, stroka in enumerate(right_dis):
        screen.print_at(stroka, x, i + 1, Screen.COLOUR_WHITE)
    xborder = x - 1
    yborder = res * 2 + 1
    screen.move(xborder, 0)
    screen.draw(xborder * 2, 0, char=':')
    screen.draw(xborder * 2, yborder, char=':')
    screen.draw(xborder, yborder, char=':')
    screen.draw(xborder, 0, char=':')
    return screen

#получаем карту и индексируем ее через список списков, задаем область отображения экрана
def generation():
    with open("mapLight.txt", encoding='utf-8') as symvol:
        lines = symvol.readlines()
        for line in lines:
            karta.append(list(line.strip("\n")))

#читаем текст из файла 
def read_whiteboard():
    with open("secondscreen.txt", encoding='utf-8') as symvol:
        lines = symvol.readlines()
        for line in lines:
            right_dis.append(line.strip("\n"))

#функция для отображения списка с выбором на экране
def place_list(screen, options, captions=None, position=0, x=0, y=0):
    wide = 0
    for n, string in enumerate(options):
        if n in captions:
            x_box.append(False)
            s = len(string)
            if s > wide:
                wide = s
        else:
            x_box.append(True)
            s = len('( )' + string)
            if s > wide:
                wide = s
    p = 0
    while True: 
        if position + p < len(options) - 1: 
            p += 1
            if x_box[position + p]:
                position += p
                break
        else:
            break
    def check_for_caption(captions, option, i):
        if i in captions:
            return f'{option}'
        else:
            return f'( ) {option}'
    while True:
        screen.clear_buffer(Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK,
                            x, y, wide, len(options) - 1)
        # screen.print_at('X', wide, len(options) - 1, Screen.COLOUR_GREEN)
        for i, option in enumerate(options):
            stroka = check_for_caption(captions, option, i)
            screen.print_at(stroka, x, y + i, Screen.COLOUR_WHITE)
            if position == i:
                screen.print_at('X', x + 1, y + i, Screen.COLOUR_GREEN)
        screen.refresh()
        event = screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == ord("q"):
                return
            elif event.key_code in (10, 13, Screen.ctrl("m")):
                return options[position]
            elif event.key_code == Screen.KEY_UP:
                p = 0
                while True: 
                    if position - p > 0: 
                        p += 1
                        if x_box[position - p]:
                            position -= p
                            break
                    else:
                        break
            elif event.key_code == Screen.KEY_DOWN:
                p = 0
                while True: 
                    if position + p < len(options) - 1: 
                        p += 1
                        if x_box[position + p]:
                            position += p
                            break
                    else:
                        break
        sleep(0.05)

# обновление ВСЕГО дисплея!
def update(screen, center):
    screen.clear_buffer(Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK)
    point_first = [center[0] - res, center[1] - res * 2]
    for i in range(res * 2):
        stroka = ""
        for j in range(res * 4):
            stroka += karta[i + point_first[0]][j + point_first[1]]
        screen.print_at(stroka, 1, i + 1, Screen.COLOUR_WHITE)
    xborder = res * 4 + 1
    yborder = res * 2 + 1
    screen.move(0, 0)
    screen.draw(xborder, 0, char=':')
    screen.draw(xborder, yborder, char=':')
    screen.draw(0, yborder, char=':')
    screen.draw(0, 0, char=':')
    screen = side_screen(screen)
    screen.refresh()
    return

# находим координаты персонажа
def findhero():
    for i in range(len(karta)):
        for j in range(len(karta[i])):
            if karta[i][j] == hero:
                return [i, j]