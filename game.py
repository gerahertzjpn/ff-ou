# ゲームのエントリーポイント（python game.py で起動）

# モジュールのインポート
import mainmenu
import map
from asciimatics.event import KeyboardEvent
from asciimatics.screen import Screen
from map import hero as hero
from map import karta as karta

# 変数の定義（underhero: 主人公の足元にあるマス）
underhero = "."
map_height = 18
map_width = 34
current_page = 1

# 通行できないマス
blockedcells = ["/", "#", "T"]

# ゲーム本体の関数
def play_game(screen):
    # 初期化処理（テキスト・マップの読み込み、メインメニュー、サイド画面の表示）
    map.read_whiteboard()
    map.generation()
    heropos = map.findhero()
    mainmenu.start_screen(screen)
    map.side_screen(screen)
    map.init_right_window(screen)


    # 主人公が次のマスに移動できるかを判定する
    def checker(x):
        result = True
        for i in range(len(blockedcells)):
            if x == blockedcells[i]:
                return False
        return result


    # マップ上でのキャラクターの移動
    def moveup():
        y, x = heropos
        if checker(karta[y - 1][x]):
            global underhero
            karta[y][x] = underhero
            heropos[0] = y - 1
            y = heropos[0]
            underhero = karta[y][x]
            karta[y][x] = hero
            return


    def moveright():
        y, x = heropos
        if checker(karta[y][x + 1]):
            global underhero
            karta[y][x] = underhero
            heropos[1] = x + 1
            x = heropos[1]
            underhero = karta[y][x]
            karta[y][x] = hero
            return


    def movedown():
        y, x = heropos
        if checker(karta[y + 1][x]):
            global underhero
            karta[y][x] = underhero
            heropos[0] = y + 1
            y = heropos[0]
            underhero = karta[y][x]
            karta[y][x] = hero
            return

    def moveleft():
        y, x = heropos
        if checker(karta[y][x - 1]):
            global underhero
            karta[y][x] = underhero
            heropos[1] = x - 1
            x = heropos[1]
            underhero = karta[y][x]
            karta[y][x] = hero
            return

    # メインループ：マップを描画し、キー入力を処理する
    # 矢印キー: 移動 / E: サイドメニュー / Esc: 終了
    while True:
        map.update(screen, heropos) 
        key = screen.get_event()
        if isinstance(key, KeyboardEvent):
            if key.key_code == Screen.KEY_UP:
                moveup()
            elif key.key_code == Screen.KEY_RIGHT:
                moveright()
            elif key.key_code == Screen.KEY_DOWN:
                movedown()
            elif key.key_code == Screen.KEY_LEFT:
                moveleft()
            elif key.key_code == Screen.KEY_ESCAPE:
                return
            elif key.key_code == ord('e'):
                screen = map.right_window(screen)

# ゲームを起動
Screen.wrapper(play_game)