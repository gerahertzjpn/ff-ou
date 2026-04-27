# импортируем модули
from map import karta as karta, hero as hero
import map
import mainmenu
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent

# задаем переменные
underhero = "."
map_height = 18
map_width = 34
current_page = 1

# клетки на которые нельзя перейти
blockedcells = ["/", "#", "T"]

#функция игры
def play_game(screen):
    # запускаем инициализацию
    map.read_whiteboard()
    map.generation()
    heropos = map.findhero()
    mainmenu.start_screen(screen)
    map.side_screen(screen)
    map.init_right_window(screen)


    # проверяем доступность перехода на некст клетку героем
    def checker(x):
        result = True
        for i in range(len(blockedcells)):
            if x == blockedcells[i]:
                return False
        return result


    # реализуем передвижение персонажа по карте
    def moveup():
        y, x = heropos
        if checker(karta[y - 1][x]):
            global underhero
            karta[y][x] = underhero
            heropos[0] = y - 1
            y = heropos[0]
            underhero = karta[y][x]
            karta[y][x] = hero
            return


    def moveright():
        y, x = heropos
        if checker(karta[y][x + 1]):
            global underhero
            karta[y][x] = underhero
            heropos[1] = x + 1
            x = heropos[1]
            underhero = karta[y][x]
            karta[y][x] = hero
            return


    def movedown():
        y, x = heropos
        if checker(karta[y + 1][x]):
            global underhero
            karta[y][x] = underhero
            heropos[0] = y + 1
            y = heropos[0]
            underhero = karta[y][x]
            karta[y][x] = hero
            return

    def moveleft():
        y, x = heropos
        if checker(karta[y][x - 1]):
            global underhero
            karta[y][x] = underhero
            heropos[1] = x - 1
            x = heropos[1]
            underhero = karta[y][x]
            karta[y][x] = hero
            return

    while True:
        map.update(screen, heropos) 
        key = screen.get_event()
        if isinstance(key, KeyboardEvent):
            if key.key_code == Screen.KEY_UP:
                moveup()
            elif key.key_code == Screen.KEY_RIGHT:
                moveright()
            elif key.key_code == Screen.KEY_DOWN:
                movedown()
            elif key.key_code == Screen.KEY_LEFT:
                moveleft()
            elif key.key_code == Screen.KEY_ESCAPE:
                return
            elif key.key_code == ord('e'):
                screen = map.right_window(screen)

#запуск функции игры
Screen.wrapper(play_game)