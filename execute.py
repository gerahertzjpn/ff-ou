import map
import settings

print("main menu")
print("1 play")
print("2 settings")
print("created by yarick+andrew")

selected = int(input())
if selected == 1:
    print(map.mapgeneration())
elif selected == 2:
    settings.settings()
else:
    print("бан")
