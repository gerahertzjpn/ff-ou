# from asciimatics.screen import Screen
# from asciimatics.event import KeyboardEvent

# #задаем переменные
# sss = []

# #экран выбора на боковой панели
# def sidescreen_navigation():
#     sidemenu_choice = [
#     "equipment",
#     "quest",
#     ]
#     #получаем выбор от игрока
#     choice = cutie.select(sidemenu_choice)
#     if choice == 0:
#         return
#     elif choice == 1:
#         return

# #обновление боковой панели
# def secondwindow(map_height, map_width):
#     global seconddis
#     symvol = open("secondscreen.txt", "r", encoding="utf-8")
#     lines = symvol.readlines()
#     for line in lines:
#         sss.append(list(line.strip("\n")))
#     symvol.close()
#     seconddis = curses.newwin(map_height, map_width, 0, map_width)
# def updateside():
#     curses.curs_set(False)
#     global seconddis
#     seconddis.clear()
#     seconddis.border()
#     for i in range(len(sss)):
#         stroka = ""
#         for j in range(len(sss[i])):
#             stroka += sss[i][j]
#         seconddis.addstr(i + 1, 1, stroka)
#         seconddis.refresh()
#     return

# #определяем переменные
# screen = []

# # 
# def read_whiteboard():
#     symvol = open("secondscreen.txt")
#     lines = symvol.readlines()
#     for line in lines:
#         screen.append(list(line.strip("\n")))
#     symvol.close()

# def active_screen():
#     text = 'aboba'
#     y1, x1 = [1, 1]
#     y2, x2 = [len(screen) - 1, len(screen[len(screen) - 1]) - 1]
#     print(text)
#     for i in range(y2 - y1):
#         for j in range(x2 - x1):
#             print(text[j][i])
#             screen[j + y1][i + x1] == text[j][i]

# def sidescreen_stroka(i):
#     active_screen() 
#     stroka = ""
#     for j in range(len(screen[i])):
#         stroka += screen[i][j]
#     return stroka
# read_whiteboard()
# sidescreen_stroka(1)