symvol = open('map.txt')
lines = symvol.readlines()
karta = []
for line in lines:
    karta.append(list(line.strip()))
symvol.close()

for row in range(len(karta)):
    stroka = ''
    for colums in range(len(karta[row])):
        stroka += karta[row][colums]
    print(stroka)

spawn = karta[1][4]
hero = spawn