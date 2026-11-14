# マップの描画、サイド画面、メニュー UI（FatherList / SideScreen）
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
from time import sleep

# 変数の定義
# karta: マップ（二次元リスト）、x_box: 各行が選択可能かどうか、right_dis: サイド画面用テキスト
# res: 表示範囲の基準値（マップ表示は res*4 x res*2 = 32x16 マス）
karta, x_box, right_dis = [], [], []
hero = "$"
enemy = "!"
res = 8
current_page = 1
x_rs = res * 4 + 2
xborder = x_rs - 1
yborder = res * 2 + 1
page_A = [
    'quests',
    'first',
    'back',
]
page_B = [
    'equipment',
    'first',
    'back',
]
page_C = [
    'items',
    'third',
    'back',
]
page_D = [
    'skills',
    'first',
    'back',
]
page_E = [
    'stats',
    'second',
    'back',
]
# サイドメニューのページ（各ページの先頭要素は見出し）
pages_list = [page_A, page_B, page_C, page_D, page_E]

# 画面の右半分（サイド画面）の枠を描画する
def side_screen(screen): 
    screen.clear_buffer(Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK,
                                xborder, 0, xborder, yborder)
    screen.move(xborder, 0)
    screen.draw(xborder * 2, 0, char=':')
    screen.draw(xborder * 2, yborder, char=':')
    screen.draw(xborder, yborder, char=':')
    screen.draw(xborder, 0, char=':')
    return screen

# サイド画面の初期表示（操作は受け付けない）
def init_right_window(screen):
    global player_choice
    player_choice = SideScreen(pages_list[current_page - 1], [0], 0, xborder + 1, 1)
    player_choice.view_list(screen)
    screen.print_at(f'< {current_page} / {len(pages_list)} >', x_rs + 11, yborder - 1, Screen.COLOUR_WHITE)
    return screen

# サイド画面のアクティブなメニュー（←/→ でページ切り替え、Q で閉じる）
def right_window(screen):
    global current_page, player_choice
    while True:
        player_choice = SideScreen(pages_list[current_page - 1], [0], 0, xborder + 1, 1)
        screen = side_screen(screen)
        change_page = f'< {current_page} / {len(pages_list)} >'
        screen.print_at(change_page, x_rs + 11, yborder - 1, Screen.COLOUR_WHITE)
        screen = player_choice.place_list(screen)
        if player_choice.choice == 'exit':
            screen.print_at(' ', player_choice.x + 1, player_choice.y + player_choice.position, Screen.COLOUR_WHITE)
            return screen
        if player_choice.choice == 'next':
            if current_page > len(pages_list) - 1:
                pass
            else:
                current_page += 1
        if player_choice.choice == 'previous':
            if current_page == 1:
                pass
            else:
                current_page -= 1

# マップをファイルから読み込み、二次元リスト（リストのリスト）として保持する
def generation():
    with open("mapLight.txt", encoding='utf-8') as symvol:
        lines = symvol.readlines()
        for line in lines:
            karta.append(list(line.strip("\n")))

# サイド画面用のテキストをファイルから読み込む
def read_whiteboard():
    with open("secondscreen.txt", encoding='utf-8') as symvol:
        lines = symvol.readlines()
        for line in lines:
            right_dis.append(line.strip("\n"))

# 画面上に選択式のリストを表示するクラス
# captions に指定した行は見出しとして表示され、カーソルでは選択できない
class FatherList:

    def __init__(self, options=None, captions=None, position=0, x=0, y=0):
        self.x = x
        self.y = y
        self.exitconfirm = False
        self.options = options
        self.captions = captions
        self.position = position

    # キー入力の処理：↑/↓ でカーソル移動（見出し行はスキップ）、Enter で決定
    def _move_in_event(self, screen):
        position = self.position
        event = screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code in (10, 13, Screen.ctrl("m")):
                self.choice = self.options[position]
                self.exitconfirm = True
            elif event.key_code == Screen.KEY_UP:
                p = 0
                while True: 
                    if position - p > 0: 
                        p += 1
                        if x_box[position - p]:
                            position -= p
                            break
                    else:
                        break
            elif event.key_code == Screen.KEY_DOWN:
                p = 0
                while True: 
                    if position + p < len(self.options) - 1: 
                        p += 1
                        if x_box[position + p]:
                            position += p
                            break
                    else:
                        break
        self.position = position
        return screen
    
    # 見出し行はそのまま、選択肢には "( )" を付けて表示する
    def _check_for_caption(self, option, i):
        if i in self.captions:
            return f'{option}'
        else:
            return f'( ) {option}'

    # リストを表示し、決定されるまで入力を待つ（結果は self.choice に入る）
    def place_list(self, screen):
        self.choice = ''
        wide = 0
        for n, string in enumerate(self.options):
            if n in self.captions:
                x_box.append(False)
                s = len(string)
                if s > wide:
                    wide = s
            else:
                x_box.append(True)
                s = len('( )' + string)
                if s > wide:
                    wide = s
        p = 0
        while True: 
            if self.position + p < len(self.options) - 1: 
                if x_box[self.position + p]:
                    self.position += p
                    break
                p += 1
            else:
                break
        
        while True:
            screen.clear_buffer(Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK,
                                self.x, self.y, wide, len(self.options))
            for i, option in enumerate(self.options):
                stroka = self._check_for_caption(option, i)
                screen.print_at(stroka, self.x, self.y + i, Screen.COLOUR_WHITE)
                if self.position == i:
                    screen.print_at('X', self.x + 1, self.y + i, Screen.COLOUR_GREEN)
            screen.refresh()
            screen = self._move_in_event(screen)   
            if self.exitconfirm:
                return screen       
            sleep(0.05)

    # 入力は受け付けず、リストを表示するだけ
    def view_list(self, screen):
        for i, option in enumerate(self.options):
                stroka = self._check_for_caption(option, i)
                screen.print_at(stroka, self.x, self.y + i, Screen.COLOUR_WHITE)
        return screen

# FatherList を継承し、内部メソッド _move_in_event をオーバーライドする
# 結果は、リストの選択肢のいずれか、Q キーによる終了（'exit'）、
# またはページ切り替え（'next' / 'previous'）のいずれかになる
class SideScreen(FatherList):
    def _move_in_event(self, screen):
        position = self.position
        event = screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code in (10, 13, Screen.ctrl("m")):
                self.choice = self.options[position]
                self.exitconfirm = True
            elif event.key_code == Screen.KEY_UP:
                p = 0
                while True: 
                    if position - p > 0: 
                        p += 1
                        if x_box[position - p]:
                            position -= p
                            break
                    else:
                        break
            elif event.key_code == Screen.KEY_DOWN:
                p = 0
                while True: 
                    if position + p < len(self.options) - 1: 
                        p += 1
                        if x_box[position + p]:
                            position += p
                            break
                    else:
                        break
            elif event.key_code == Screen.KEY_RIGHT:
                self.choice = 'next'
                self.exitconfirm = True
            elif event.key_code == Screen.KEY_LEFT:
                self.choice = 'previous'
                self.exitconfirm = True
            elif event.key_code == ord('q'):
                self.choice = 'exit'
                self.exitconfirm = True
        self.position = position
        return screen

# 表示中のマップを更新する（主人公を中心にスクロール表示）
def update(screen, center):
    xborder = res * 4 + 1
    yborder = res * 2 + 1
    screen.clear_buffer(Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK,
                        1, 1, xborder - 1, yborder - 1)
    point_first = [center[0] - res, center[1] - res * 2]
    for i in range(res * 2):
        stroka = ""
        for j in range(res * 4):
            stroka += karta[i + point_first[0]][j + point_first[1]]
        screen.print_at(stroka, 1, i + 1, Screen.COLOUR_WHITE)
    screen.move(0, 0)
    screen.draw(xborder, 0, char=':')
    screen.draw(xborder, yborder, char=':')
    screen.draw(0, yborder, char=':')
    screen.draw(0, 0, char=':')
    screen.refresh()
    return

# マップ上の主人公の座標 [y, x] を探す
def findhero():
    for i in range(len(karta)):
        for j in range(len(karta[i])):
            if karta[i][j] == hero:
                return [i, j]