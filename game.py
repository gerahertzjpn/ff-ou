#импортируем модули
import msvcrt

#задаем переменные
karta = []
hero = '$'
setup = 'w'
setright = 'd'
setdown = 's'
setleft = 'a'
exit = 'x'
pbutton = ''
underhero = '.'

#клетки на которые нельзя перейти
blockedcells = ['/', '#']

#получаем карту и индексируем ее
symvol = open('map.txt')
lines = symvol.readlines()
for line in lines:
    karta.append(list(line.strip()))
symvol.close()

#находим координаты персонажа
def findhero ():
    for i in range(len(karta)):
        for j in range(len(karta[i])):
            if karta[i][j] == hero:
                return [i, j]
heropos = findhero()

#вывод индексированной карты в консоль
# for row in range(len(karta)):
#     stroka = ''
#     for colums in range(len(karta[row])):
#         stroka += karta[row][colums]
#     print(stroka)

#обновление карты
def mapupdate():
    for row in range(len(karta)):
        stroka = ''
        for colums in range(len(karta[row])):
            stroka += karta[row][colums]
        print(stroka)
    return
mapupdate()
print('для экзита нажми x')

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
        mapupdate()
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
        mapupdate()
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
        mapupdate()
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
        mapupdate()
        return 
    else:
        return

while pbutton != exit:
    pbutton = msvcrt.getwch()
    if setup == pbutton:
        moveup()
    elif setright == pbutton:
        moveright()
    elif setdown == pbutton:
        movedown()
    elif setleft == pbutton:
        moveleft()