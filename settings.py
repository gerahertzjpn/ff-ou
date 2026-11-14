# 実験用のコード（すべてコメントアウト済み・現在は未使用）

# class Person:
 
#     def __init__(self, name):
#         self.__name = name   # 人の名前
 
#     @property
#     def name(self):
#         return self.__name
     
#     @property
#     def display_info(self):
#         print(f"Name: {self.__name} ")

# class Coder(Person):

#     def setlevel(self, nowlevel):
#         self.__level = nowlevel

#     @property
#     def level(self):
#         return self.__level

# p = Coder(input())
# p.setlevel(input())
# print(p.name + ' ' + p.level)

# from asciimatics.screen import Screen
# from asciimatics.event import KeyboardEvent
# from time import sleep


# def demo(screen):
#     x = 10
#     y = 5

#     while True:
#         for i in range(10):
#             screen.clear_buffer(Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK)
#             screen.print_at("Press <- ->, Q to quit", 3, 2, Screen.COLOUR_WHITE)
#             event = screen.get_event()
            # if isinstance(event, KeyboardEvent):
            #     if event.key_code in (ord("q"), ord("Q")):
            #         return
            #     elif event.key_code == Screen.KEY_LEFT:
            #         x -= 1
            #     elif event.key_code == Screen.KEY_RIGHT:
            #         x += 1
#             screen.print_at(i, i, 1, Screen.COLOUR_RED)
#             screen.print_at("@", x, y, Screen.COLOUR_WHITE)
#             screen.refresh()
#             sleep(0.1)

# Screen.wrapper(demo)