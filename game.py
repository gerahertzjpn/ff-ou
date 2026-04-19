#импортируем модули
import msvcrt
from map import (karta as karta, hero as hero)
import map
import mainmenu

#задаем переменные
setup_sp = 'H'
setup = 'w'
setright_sp = 'M'
setright = 'd'
setdown_sp = 'P'
setdown = 's'
setleft_sp = 'K'
setleft = 'a'
exit_button = 'x'
key = ''
underhero = '.'

#клетки на которые нельзя перейти
blockedcells = ['/', '#']

#запускаем инициализацию
mainmenu.start_screen()
map.generation()
heropos = map.findhero()

#проверяем доступность перехода на некст клетку героем
def checker(x):
    for i in range(len(blockedcells)):
        if x == blockedcells[i]:
            return False
        else:
            result = True
    return result

#реализуем передвижение персонажа по карте
def moveup():
    if checker(karta[heropos[0] - 1][heropos[1]]):
        global underhero
        karta[heropos[0]][heropos[1]] = underhero
        heropos[0] = heropos[0] - 1 
        underhero = karta[heropos[0]][heropos[1]]
        karta[heropos[0]][heropos[1]] = hero
        return 
    else:
        return

def moveright():
    if checker(karta[heropos[0]][heropos[1] + 1]):
        global underhero
        karta[heropos[0]][heropos[1]] = underhero
        heropos[1] = heropos[1] + 1 
        underhero = karta[heropos[0]][heropos[1]]
        karta[heropos[0]][heropos[1]] = hero
        return 
    else:
        return

def movedown():
    if checker(karta[heropos[0] + 1][heropos[1]]):
        global underhero
        karta[heropos[0]][heropos[1]] = underhero
        heropos[0] = heropos[0] + 1 
        underhero = karta[heropos[0]][heropos[1]]
        karta[heropos[0]][heropos[1]] = hero
        return 
    else:
        return

def moveleft():
    if checker(karta[heropos[0]][heropos[1] - 1]):
        global underhero
        karta[heropos[0]][heropos[1]] = underhero
        heropos[1] = heropos[1] - 1 
        underhero = karta[heropos[0]][heropos[1]]
        karta[heropos[0]][heropos[1]] = hero
        return 
    else:
        return

while key != exit_button:
    map.update(heropos)
    print('для экзита нажми x')
    key = msvcrt.getwch()
    if setup == key:
        moveup()
    elif setright == key:
        moveright()
    elif setdown == key:
        movedown()
    elif setleft == key:
        moveleft()
    elif key in ('\x00', '\xe0'):
        key = msvcrt.getwch()
        if setup_sp == key:
            moveup()
        elif setright_sp == key:
            moveright()
        elif setdown_sp == key:
            movedown()
        elif setleft_sp == key:
            moveleft()