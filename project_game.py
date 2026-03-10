import random

# Създаване на героя
player = {
    "name": "",
    "birthplace": "",
    "age": 0,
    "health": 100,
    "happiness": 100,
    "intelligence": 10,
    "energy": 100,
    "money": 0
}


def create_character():
    print("=== СЪЗДАВАНЕ НА ГЕРОЙ ===")
    player["name"] = input("Въведи име на героя: ")
    player["birthplace"] = input("Въведи място на раждане: ")
    while True:
        question = input("Искате ли да започнете от определени години? (Да/Не) или (Yes/No)")
        if question == "Да" or question == "да" or question == "Yes" or question == "yes":
            player["age"] = int(input("Въведи години на героя: "))
            break
        elif question == "Не" or question == "не" or question == "No" or question == "no":
            print(f"Вие току що излезнате на този свят.")
            break
        else:
            print("Невалиден вход , опитай пак.")
    print(f"\nГероят {player['name']} е създаден успешно!")
    if player["age"] > 0:
        print(f"{player["name"]} е на {player["age"]} години.")
    print(f"Място на раждане: {player['birthplace']}")
    print("-" * 30)


def show_status():
    print("\n=== СТАТУС НА ГЕРОЯ ===")
    print(f"Име: {player['name']}")
    print(f"Място на раждане: {player['birthplace']}")
    print(f"Възраст: {player['age']}")
    print(f"Здраве: {player['health']}")
    print(f"Щастие: {player['happiness']}")
    print(f"Интелигентност: {player['intelligence']}")
    print(f"Енергия: {player['energy']}")
    if player["age"] >= 18:
        print(f"Пари: {player['money']}")
    print("-" * 30)


def next_year():
    player["age"] += 1
    player["energy"] -= 10
    print(f"\nМина още една година. Вече си на {player['age']} години.")
    random_event()


def study():
    print("\nТи избра да учиш.")
    player["intelligence"] += 5
    player["energy"] -= 10
    player["happiness"] -= 5
    print("Научи нещо ново! +5 интелигентност")


def play():
    print("\nТи избра да играеш.")
    player["happiness"] += 10
    player["energy"] -= 10
    print("Забавлява се! +10 щастие")


def sport():
    print("\nТи избра да спортуваш.")
    player["health"] += 5
    player["energy"] -= 15
    player["happiness"] += 5
    print("Тренира успешно! +5 здраве, +5 щастие")


def rest():
    print("\nТи избра да почиваш.")
    player["energy"] += 20
    player["health"] += 5
    print("Почина си добре. +20 енергия, +5 здраве")


def random_event():
    events = [
        ("Изкара отлична оценка в училище!", {"intelligence": 5, "happiness": 5}),
        ("Настина и се почувства зле.", {"health": -10}),
        ("Запозна се с нов приятел.", {"happiness": 10}),
        ("Стоя до късно и си изморен.", {"energy": -10}),
        ("Участва в състезание и се представи добре!", {"happiness": 10, "intelligence": 5}),
    ]

    event = random.choice(events)
    text = event[0]
    effects = event[1]

    print(f"Случайно събитие: {text}")

    for stat, value in effects.items():
        player[stat] += value


def check_stats():
    # Ограничаваме стойностите да не стават прекалено големи или отрицателни
    for stat in ["health", "happiness", "intelligence", "energy"]:
        if player[stat] > 100:
            player[stat] = 100
        if player[stat] < 0:
            player[stat] = 0


def is_game_over():
    if player["health"] <= 0:
        print("\nГероят се разболя твърде много. Играта свърши.")
        return True
    if player["energy"] <= 0:
        print("\nГероят е напълно изтощен. Играта свърши.")
        return True
    return False


def show_menu():
    if player["age"] == 0 or player["age"] <= 4:
        print("\n=== МЕНЮ ===")
        print("1. Следваща година")
        print("2. Играй")
        print("3. Почивай")
        print("4. Покажи статус")
        print("5. Изход")

        choice = input("Избери действие: ")

        if choice == "1":
            next_year()
        elif choice == "2":
            play()
        elif choice == "3":
            rest()
        elif choice == "4":
            show_status()
        elif choice == "5":
            print("Излезе от играта.")
            return False
        else:
            print("Невалиден избор, опитай пак.")
    elif player["age"] > 4:
        print("\n=== МЕНЮ ===")
        print("1. Следваща година")
        print("2. Учи")
        print("3. Играй")
        print("4. Спортувай")
        print("5. Почивай")
        print("6. Покажи статус")
        print("7. Изход")

        choice = input("Избери действие: ")

        if choice == "1":
            next_year()
        elif choice == "2":
            study()
        elif choice == "3":
            play()
        elif choice == "4":
            sport()
        elif choice == "5":
            rest()
        elif choice == "6":
            show_status()
        elif choice == "7":
            print("Излезе от играта.")
            return False
        else:
            print("Невалиден избор, опитай пак.")
    else:
        print("Невалидни години!!")
    return True


def main():
    create_character()

    while True:
        check_stats()

        if is_game_over():
            break

        if not show_menu():
            break


main()
