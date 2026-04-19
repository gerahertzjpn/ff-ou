import cutie
import random

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

    # Выбор действия на экране сражения
    while enemy_hp >= 0:
        print("У врага ", enemy_hp, " здоровья, выберите действие.")
        choice = cutie.select(fight_choice, selected_index=1)
        if choice == 0:
            damage = random.randint(1, 10)
            print("\033[H\033[J")
            print("вы нанесли ", damage, " урона!")
            damage_dealt()
        elif choice == 1:
            choice = cutie.select(skill_choice, selected_index=1)
            if choice == 0:
                damage = random.randint(5, 20)
                print("\033[H\033[J")
                print("своим дрыном вы нанесли ", damage, " урона!")
                print("не останавливайтесь...")
                damage_dealt()
            elif choice == 1:
                damage = random.randint(1, 100)
                print("\033[H\033[J")
                print("вы нанесли врагу ", damage, " урона своим пением!")
                print("пожалуйста больше не пойте")
                damage_dealt()
        elif choice == 2:
            print("\033[H\033[J")
            print(
                "Вы выпили зелье здоровья! А нет, это был стакан кумыса. Вы наполняетесь решимостью!!!"
            )
        elif choice == 3:
            print("\033[H\033[J")
            print("Вы смогли сбежать!")
            break

def damage_dealt():
    global damage, enemy_hp
    enemy_hp = enemy_hp - damage
    if enemy_hp <= 0:
        print("Вы победили!")
    else:
        print("у врага осталось ", enemy_hp, " хп!")

fight_screen()