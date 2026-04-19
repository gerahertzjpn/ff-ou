import cutie
import random


def fight_screen():
    global enemy_hp
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
            print("вы нанесли ", damage, " урона!")
            enemy_hp = enemy_hp - damage
            if enemy_hp <= 0:
                print("Вы победили!")
                break
            else:
                print("у врага осталось ", enemy_hp, " хп!")
        elif choice == 1:
            choice = cutie.select(skill_choice, selected_index=1)
            if choice == 0:
                damage = random.randint(5, 20)
                print("своим дрыном вы нанесли ", damage, " урона!")
                print("не останавливайтесь...")
                enemy_hp = enemy_hp - damage
                if enemy_hp <= 0:
                    print("Вы победили!")
                    break
                else:
                    print("у врага осталось ", enemy_hp, " хп!")
            elif choice == 1:
                damage = random.randint(1, 100)
                print("вы нанесли врагу ", damage, " урона своим пением!")
                print("пожалуйста больше не пойте")
                enemy_hp = enemy_hp - damage
                if enemy_hp <= 0:
                    print("Вы победили!")
                    break
                else:
                    print("у врага осталось ", enemy_hp, " хп!")
        elif choice == 2:
            print(
                "Вы выпили зелье здоровья! А нет, это был стакан кумыса. Вы наполняетесь решимостью!!!"
            )
        elif choice == 3:
            print("Вы смогли сбежать!")
            break
