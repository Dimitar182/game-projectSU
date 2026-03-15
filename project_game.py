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
    while True:
        player["name"] = input("Въведи име на героя: ")
        if len(player["name"]) > 30:
            print("Името не може да е по-дълго от 30 символа!")
        else:
            break
    player["birthplace"] = input("Въведи място на раждане: ")
    while True:
        question = input("Искате ли да започнете от определени години? (Да/Не) или (Yes/No)")
        if question == "Да" or question == "да" or question == "Yes" or question == "yes":
            player["age"] = int(input("Въведи години на героя: "))
            if player["age"] > 100:
                print(f"Въведи по-малко от 100 години")
            else:
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
    if player["money"] > 0:
        player["money"] = int(player["money"] * 1.05) # 5% годишна лихва
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


def work():
    if player["intelligence"] > 50:
        print("\nТи работиш като Софтуерен Инженер! +100 пари")
        player["money"] += 100
    else:
        print("\nТи работиш като Касиер. +30 пари")
        player["money"] += 30
    player["energy"] -= 20

def shop():
    print("\n=== МАГАЗИН ===")
    print(f"Разполагаш с: {player['money']} пари")
    print("1. Книга (20 пари) -> +10 Интелигентност")
    print("2. Енергийна напитка (10 пари) -> +20 Енергия, -5 Здраве")
    print("3. Фитнес карта (50 пари) -> +15 Здраве, -10 Енергия")
    print("4. Видеоигра (40 пари) -> +20 Щастие, -5 Енергия")
    print("5. Изход от магазина")

    choice = input("Какво искаш да купиш? (1-5): ")

    if choice == "1":
        if player["money"] >= 20:
            player["money"] -= 20
            player["intelligence"] += 10
            print("Ти си купи Книга! Интелигентността ти се покачи.")
        else:
            print("Нямаш достатъчно пари за това!")
    elif choice == "2":
        if player["money"] >= 10:
            player["money"] -= 10
            player["energy"] += 20
            player["health"] -= 5
            print("Изпи Енергийна напитка! Имаш повече енергия, но не е много здравословно.")
        else:
            print("Нямаш достатъчно пари за това!")
    elif choice == "3":
        if player["money"] >= 50:
            player["money"] -= 50
            player["health"] += 15
            player["energy"] -= 10
            print("Купи си Фитнес карта и тренира здраво! Здравето ти се подобри.")
        else:
            print("Нямаш достатъчно пари за това!")
    elif choice == "4":
        if player["money"] >= 40:
            player["money"] -= 40
            player["happiness"] += 20
            player["energy"] -= 5
            print("Купи си нова Видеоигра! Много се забавлява.")
        else:
            print("Нямаш достатъчно пари за това!")
    elif choice == "5":
        print("Излезе от магазина.")
    else:
        print("Невалиден избор!")


def random_event():
    age = player["age"]

    if age <= 4:
        events = [
            ("Научи се да казваш нова дума.", {"intelligence": 2, "happiness": 3}),
            ("Падна, докато тичаше.", {"health": -5}),
            ("Играхте си с нова играчка.", {"happiness": 5}),
            ("Не спа добре и си изморен.", {"energy": -5}),
            ("Родителите ти те заведоха в парка.", {"happiness": 7}),
        ]

    elif age <= 6:
        events = [
            ("Започна да учиш нови неща в детската градина.", {"intelligence": 3}),
            ("Скара се с друго дете.", {"happiness": -5}),
            ("Рисува много добре днес.", {"happiness": 5, "intelligence": 2}),
            ("Настина леко.", {"health": -5}),
            ("Играхте навън цял ден.", {"happiness": 6, "energy": -5}),
        ]

    elif age <= 17:
        events = [
            ("Изкара отлична оценка в училище!", {"intelligence": 5, "happiness": 5}),
            ("Забрави си домашното.", {"happiness": -5}),
            ("Запозна се с нов приятел.", {"happiness": 10}),
            ("Стоя до късно и си изморен.", {"energy": -10}),
            ("Участва в състезание и се представи добре!", {"happiness": 10, "intelligence": 5}),
            ("Получи похвала от учител.", {"happiness": 7, "intelligence": 3}),
            ("Разболя се преди контролно.", {"health": -10, "happiness": -5}),
        ]

    else:
        events = [
            ("Намери малка работа и изкара пари.", {"money": 50, "happiness": 5}),
            ("Имаше тежък ден и си изморен.", {"energy": -10}),
            ("Погрижи се за себе си и се чувстваш по-добре.", {"health": 5, "happiness": 5}),
            ("Научи ново полезно умение.", {"intelligence": 4}),
            ("Излезе с приятели.", {"happiness": 10, "money": -20}),
            ("Похарчи пари за нещо неочаквано.", {"money": -30}),
            ("Получаваш добра възможност за работа.", {"money": 70, "happiness": 5}),
        ]

    event = random.choice(events)
    text = event[0]
    effects = event[1]

    print(f"\nСлучайно събитие: {text}")

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
        score = player["money"] + (player["intelligence"] * 10) + (player["age"] * 50)
        print(f"\n🪦 ПОЧИВАЙ В МИР, {player['name']} 🪦")
        print(f"Доживя до {player['age']} години.")
        print(f"Твоят финален резултат е: {score} точки!")
        return True
    return False


def show_menu():
    age = player["age"]

    if age <= 4:
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

    elif age < 18:
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

    elif age >= 18:
        print("\n=== МЕНЮ ===")
        print("1. Следваща година")
        print("2. Работи")
        print("3. Играй")
        print("4. Спортувай")
        print("5. Почивай")
        print("6. Магазин")
        print("7. Покажи статус")
        print("8. Изход")

        choice = input("Избери действие: ")

        if choice == "1":
            next_year()
        elif choice == "2":
            work()
        elif choice == "3":
            play()
        elif choice == "4":
            sport()
        elif choice == "5":
            rest()
        elif choice == "6":
            shop()
        elif choice == "7":
            show_status()
        elif choice == "8":
            print("Излезе от играта.")
            return False
        else:
            print("Невалиден избор, опитай пак.")

    else:
        print("Невалидни години!!!")

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
