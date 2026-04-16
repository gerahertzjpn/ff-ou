import map
import settings

print("main menu")
print("1 play")
print("2 settings")
print("3 exit")
print("created by yarick+andrew")

while True:
    selected = int(input())
    if selected == 1:
        print(map.mapgeneration())
        break
    elif selected == 2:
        settings.settings()
        break
    elif selected == 3:
        exit()
        break
    else:
        print("Дожмекаешься щас тут, пиши заново 1, 2 или 3")
