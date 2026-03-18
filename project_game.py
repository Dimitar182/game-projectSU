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
    "money": 0,
    "degree": False,
    "major": "",
    "in_university": False,
    "university_year": 0,
    "university_duration": 0,
    "studied_this_year": False
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
    print(f"Диплома: {'Да' if player['degree'] else 'Не'}")
    if player["in_university"]:
        print(f"Специалност: {player['major']}")
        print(f"Курс: {player['university_year']} / {player['university_duration']}")
        print(f"Учи тази година: {'Да' if player['studied_this_year'] else 'Не'}")
    if player["major"] and player["degree"] == True:
        print(player["major"])
    print("-" * 30)


def next_year():
    if player["in_university"] and not player["studied_this_year"]:
        print("\nНе можеш да минеш година напред, без да си учил в университета.")
        return True 

    player["age"] += 1
    player["energy"] -= 10
    print(f"\nМина още една година. Вече си на {player['age']} години.")

    if player["age"] > 100:
        death_chance = 0.05
        if random.random() < death_chance:
            print("Героят умря от старост. Играта свърши.")
            score = player["money"] + (player["intelligence"] * 10) + (player["age"] * 50)
            print(f"ПОЧИВАЙ В МИР, {player['name']}")
            print(f"Доживя до {player['age']} години.")
            print(f"Твоят финален резултат е: {score} точки!")
            exit()

    if player["in_university"]:
        if random.random() < 0.75:
            print("Успешно премина университетската година.")
            player["university_year"] += 1
        else:
            print("Не успя да преминеш всички изпити и повтаряш курса.")

        player["studied_this_year"] = False

        if player["university_year"] > player["university_duration"]:
            print(f"\nПоздравления! Завърши '{player['major']}' успешно!")
            player["degree"] = True
            player["in_university"] = False
            player["university_year"] = 0
            player["major"] = "Бакалавър по " + player["major"]
            player["university_duration"] = 0
            player["studied_this_year"] = False

    maybe_random_event(0.9)
    return True


def study():
    print("\nТи избра да учиш.")
    player["intelligence"] += 5
    player["energy"] -= 10
    player["happiness"] -= 5
    print("Научи нещо ново!\n+5 интелигентност -10 енергия -5 щастие")


def play():
    print("\nТи избра да играеш.")
    player["happiness"] += 10
    player["energy"] -= 10
    print("Забавлява се!\n+10 щастие -10 енергия")


def sport():
    print("\nТи избра да спортуваш.")
    player["health"] += 5
    player["energy"] -= 15
    player["happiness"] += 5
    print("Тренира успешно!\n+5 здраве +5 щастие -15 енергия")


def rest():
    print("\nТи избра да почиваш.")
    player["energy"] += 20
    player["health"] += 5
    print("Почина си добре.\n+20 енергия +5 здраве")


def work():
    if player["age"] < 18:
        print("\nТвърде млад си, за да работиш.")
        return

    print("\nТи избра да работиш.")

    if player["degree"]:
        earned_money = random.randint(120, 220)
        print("Имаш диплома и получаваш по-добро заплащане.")
    else:
        earned_money = random.randint(50, 120)
        print("Работиш без диплома и получаваш стандартно заплащане.")

    player["money"] += earned_money
    player["energy"] -= 20
    player["happiness"] -= 5

    print(f"Изкара {earned_money} лв.\n-20 енергия -5 щастие")

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
            print("Ти си купи Книга! Интелигентността ти се покачи.\n+10 Интелигентност")
        else:
            print("Нямаш достатъчно пари за това!")
    elif choice == "2":
        if player["money"] >= 10:
            player["money"] -= 10
            player["energy"] += 20
            player["health"] -= 5
            print("Изпи Енергийна напитка! Имаш повече енергия, но не е много здравословно.\n+20 Енергия, -5 Здраве")
        else:
            print("Нямаш достатъчно пари за това!")
    elif choice == "3":
        if player["money"] >= 50:
            player["money"] -= 50
            player["health"] += 15
            player["energy"] -= 10
            print("Купи си Фитнес карта и тренира здраво! Здравето ти се подобри.\n+15 Здраве, -10 Енергия")
        else:
            print("Нямаш достатъчно пари за това!")
    elif choice == "4":
        if player["money"] >= 40:
            player["money"] -= 40
            player["happiness"] += 20
            player["energy"] -= 5
            print("Купи си нова Видеоигра! Много се забавлява.\n+20 Щастие, -5 Енергия")
        else:
            print("Нямаш достатъчно пари за това!")
    elif choice == "5":
        print("Излезе от магазина.")
    else:
        print("Невалиден избор!")

def crime():
    if player["intelligence"] <70:
        if random.randint(1, 10) > 4: # 60% шанс за успех (60% success chance)
            stolen = random.randint(200, 1000)
            player["money"] += stolen
            player["energy"] -= 15
            player["intelligence"] += 10
            print(f"Успешен обир! Ти открадна {stolen} пари.\n+10 Интелигентност, -15 Енергия")
        else:
            player["age"] += 3 # Губиш 3 години в затвора (Lose 3 years in prison)
            player["happiness"] = 0
            print("Хванаха те! Прекара 3 години в затвора и загуби всичкото си щастие.")
    else:
        if random.randint(1, 10) > 2: # 60% шанс за успех (60% success chance)
            stolen = random.randint(700, 4000)
            player["money"] += stolen
            player["energy"] -= 15
            player["intelligence"] += 10
            print(f"Успешен обир! Ти открадна {stolen} пари.\n+10 Интелигентност, -15 Енергия")
        else:
            player["age"] += 3 # Губиш 3 години в затвора (Lose 3 years in prison)
            player["happiness"] = 0
            print("Хванаха те! Прекара 3 години в затвора и загуби всичкото си щастие.")

def apply_to_university():
    if player["age"] < 18:
        print("\nТвърде млад си, за да кандидатстваш в университет.")
        return

    if player["degree"]:
        print("\nТи вече имаш университетска диплома.")
        return

    if player["in_university"]:
        print("\nВече учиш в университет.")
        return

    print("\n=== УНИВЕРСИТЕТ ===")
    print("Избери специалност:")
    print("1. Компютърни науки (4 години)")
    print("2. Медицина (5 години)")
    print("3. Бизнес (3 години)")
    print("4. Право (4 години)")

    choice = input("Избери специалност: ")

    if choice == "1":
        player["major"] = "Компютърни науки"
        player["university_duration"] = 4
    elif choice == "2":
        player["major"] = "Медицина"
        player["university_duration"] = 5
    elif choice == "3":
        player["major"] = "Бизнес"
        player["university_duration"] = 3
    elif choice == "4":
        player["major"] = "Право"
        player["university_duration"] = 4
    else:
        print("Невалиден избор.")
        return

    player["in_university"] = True
    player["university_year"] = 1
    player["studied_this_year"] = False

    print(f"\nТи се записа в специалност '{player['major']}'!")

def study_university():
    if not player["in_university"]:
        print("\nТи не учиш в университет.")
        return

    if player["studied_this_year"]:
        print("\nТази година вече учи в университета.")
        return

    print(f"\nТи учиш в университет - {player['major']}, курс {player['university_year']}.")

    player["intelligence"] += 5
    player["energy"] -= 15
    player["happiness"] -= 5
    player["studied_this_year"] = True

    print("Учи успешно тази година в университета.\n+5 интелект -15 енергия -5 щастие")
    maybe_random_event(0.5)


def random_event():
    age = player["age"]

    if player["in_university"]:
        events = [
            ("Взе труден изпит успешно!", {"intelligence": 3, "happiness": 5}),
            ("Не спа преди изпит.", {"energy": -10}),
            ("Запозна се с нови колеги в университета.", {"happiness": 6}),
            ("Имаше много учене тази седмица.", {"energy": -8, "intelligence": 2}),
            ("Получи висока оценка на проект.", {"intelligence": 4, "happiness": 4}),
        ]

    elif age <= 4:
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
        ]

    else:
        events = [
            ("Намери временна работа.", {"money": 50, "happiness": 4}),
            ("Имаше тежък ден.", {"energy": -10}),
            ("Излезе с приятели.", {"happiness": 8, "money": -20}),
            ("Научи ново полезно умение.", {"intelligence": 3}),
        ]

    event = random.choice(events)
    text, effects = event

    print(f"\nСлучайно събитие: {text}\n{effects}")

    for stat, value in effects.items():
        player[stat] += value


def maybe_random_event(chance=0.5):
    if random.random() < chance:
        random_event()

def check_stats():
    # Ограничаваме стойностите да не стават прекалено големи или отрицателни
    for stat in ["health", "happiness", "intelligence", "energy"]:
        if player[stat] > 100:
            player[stat] = 100
        if player[stat] < 0:
            player[stat] = 0

    if player["money"] < 0:
        player["money"] = 0


def is_game_over():
    if player["health"] <= 0:
        print("\nГероят се разболя твърде много. Играта свърши.")
        score = player["money"] + (player["intelligence"] * 10) + (player["age"] * 50)
        print(f"\nПОЧИВАЙ В МИР, {player['name']}")
        print(f"Доживя до {player['age']} години.")
        print(f"Твоят финален резултат е: {score} точки!")
        return True
    return False


def show_menu():
    if player["energy"] <= 0:
        print("\nТи си прекалено изморен. Можеш само да почиваш.")

        print("\n=== МЕНЮ ===")
        print("1. Почивай")
        print("2. Покажи статус")

        choice = input("Избери действие: ")

        if choice == "1":
            rest()
        elif choice == "2":
            show_status()
        else:
            print("Невалиден избор.")

        return True

    if player["age"] <= 4:
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

    elif player["age"] <= 17:
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


    elif player["age"] >= 18:
        print("\n=== МЕНЮ ===")
        print("1. Следваща година")
        print("2. Работи")
        if player["in_university"]:
            print("3. Учи в университет")
        elif not player["degree"]:
            print("3. Кандидатствай в университет")
        print("4. Спортувай")
        print("5. Магазин")
        print("6. Престъпление")
        print("7. Почивай")
        print("8. Покажи статус")
        print("9. Изход")

        choice = input("Избери действие: ")

        if choice == "1":
            next_year()
        elif choice == "2":
            work()
        elif choice == "3":
            if player["in_university"]:
                study_university()
            elif not player["degree"]:
                apply_to_university()
            else:
                print("Невалиден избор.")
        elif choice == "4":
            sport()
        elif choice == "5":
            shop()
        elif choice == "6":
            crime()
        elif choice == "7":
            rest()
        elif choice == "8":
            show_status()
        elif choice == "9":
            print("Излезе от играта.")
            return False
        else:
            print("Невалиден избор, опитай пак.")

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
