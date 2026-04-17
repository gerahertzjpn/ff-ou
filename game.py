#импортируем модули
import msvcrt

#получаем карту и индексируем ее
symvol = open('map.txt')
lines = symvol.readlines()
karta = []
for line in lines:
    karta.append(list(line.strip()))
symvol.close()

#задаем координаты персонажа
hero = '$'
def findhero ():
    for i in range(len(karta)):
        for j in range(len(karta[i])):
            if karta[i][j] == hero:
                return [i, j]

heropos = findhero()
heropos[0] = heropos[0] - 1
print(heropos)
#вывод индексированной карты в консоль
for row in range(len(karta)):
    stroka = ''
    for colums in range(len(karta[row])):
        stroka += karta[row][colums]
    print(stroka)

#обновление карты
def mapupdate():
    a = 0
    return a

#реализуем передвижение персонажа по карте
# setup = 'w'
# setright = 'd'
# setdown = 's'
# setleft = 'a'
# exit = 'x'
# pbutton = ''

# def moveup():
#     a = 0
#     return a

# def moveright():
#     a = 0
#     return a

# def movedown():
#     a = 0
#     return a

# def moveleft():
#     a = 0
#     return a

# while pbutton != 'x':
#     pbutton = msvcrt.getwch()
#     if setup == pbutton:
#         moveup()
#         print('up')
#     elif setright == pbutton:
#         moveright()
#         print('right')
#     elif setdown == pbutton:
#         print('down')
#     elif setleft == pbutton:
#         print('left')

