import map
import settings

print("main menu")
print("1 play")
print("2 settings")
print("created by yarick+andrew")

while True:
    selected = int(input())
    if selected == 1:
        print(map.mapgeneration())
        break
    elif selected == 2:
        settings.settings()
        break
    else:
        print("Нет, из игры нельзя выйти, пиши заново")
