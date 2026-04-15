import map, settings

print('main menu')
print('1 play')
print('2 settings')
print('created by yarick')

selected = int(input())
if selected == 1:
    print(map.mapgeneration())
else:
    if selected == 2:
        settings.settings()
    else:
        print('пошел нахуй')