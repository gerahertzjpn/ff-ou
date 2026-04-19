# задаем переменные
karta = []
hero = "$"
enemy = "!"
res = 8


# получаем карту и индексируем ее через список списков
def generation():
    symvol = open("mapLight.txt")
    lines = symvol.readlines()
    for line in lines:
        karta.append(list(line.strip("\n")))
    symvol.close()


# обновление отображаемой карты
def update(center):
    print("\033[H\033[J")
    point_first = [center[0] - res, center[1] - res * 2]
    for i in range(res * 2):
        stroka = ""
        for j in range(res * 4):
            stroka += karta[i + point_first[0]][j + point_first[1]]
        print(stroka)
    return


# находим координаты персонажа
def findhero():
    for i in range(len(karta)):
        for j in range(len(karta[i])):
            if karta[i][j] == hero:
                return [i, j]


# отобразить всю карту
def display_all_map():
    print("\033[H\033[J")
    for row in range(len(karta)):
        stroka = ""
        for colums in range(len(karta[row])):
            stroka += karta[row][colums]
        print(stroka)
    return
