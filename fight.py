# 戦闘システムのプロトタイプ（単体で実行: python fight.py）
import cutie
import random

# 1 回分の戦闘を行う
def fight_screen():
    global enemy_hp, damage
    enemy_hp = 50

    fight_choice = [
        "attack",
        "skill",
        "item",
        "run",
    ]

    skill_choice = [
        "sword attack",
        "sing a song",
    ]

    # 戦闘画面での行動選択（敵の HP がなくなるまで繰り返す）
    while enemy_hp >= 0:
        print("The enemy has", enemy_hp, "HP. Choose your action.")
        choice = cutie.select(fight_choice, selected_index=1)
        # 通常攻撃
        if choice == 0:
            damage = random.randint(1, 10)
            print("\033[H\033[J")
            print("You dealt", damage, "damage!")
            damage_dealt()
        # スキル
        elif choice == 1:
            choice = cutie.select(skill_choice, selected_index=1)
            if choice == 0:
                damage = random.randint(5, 20)
                print("\033[H\033[J")
                print("You whacked the enemy with your trusty stick for", damage, "damage!")
                print("Don't stop now...")
                damage_dealt()
            elif choice == 1:
                damage = random.randint(1, 100)
                print("\033[H\033[J")
                print("Your singing dealt", damage, "damage to the enemy!")
                print("Please, never sing again.")
                damage_dealt()
        # アイテム
        elif choice == 2:
            print("\033[H\033[J")
            print(
                "You drank a health potion! Oh wait, it was a glass of kumis. You are filled with determination!!!"
            )
        # 逃げる
        elif choice == 3:
            print("\033[H\033[J")
            print("You got away!")
            break

# 与えたダメージを敵の HP から引き、勝敗を表示する
def damage_dealt():
    global damage, enemy_hp
    enemy_hp = enemy_hp - damage
    if enemy_hp <= 0:
        print("You won!")
    else:
        print("The enemy has", enemy_hp, "HP left!")

fight_screen()