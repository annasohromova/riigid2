import random

def load_dictionary(file_path):
    dictionary = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip().split(":")
            country = line[0]
            capital = line[1]
            dictionary[country] = capital
    return dictionary

def save_dictionary(dictionary, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        for country, capital in dictionary.items():
            file.write(f"{country}:{capital}\n")

def display_capital_or_country(dictionary, input_value):
    if input_value in dictionary:
        print("Столица:", dictionary[input_value])
    elif input_value in dictionary.values():
        print("Страна:", list(dictionary.keys())[list(dictionary.values()).index(input_value)])
    else:
        print("Введенное значение отсутствует в словаре.")

def add_to_dictionary(dictionary, country, capital):
    if country in dictionary:
        print("Это значение уже есть в словаре.")
    else:
        dictionary[country] = capital
        print("Значение добавлено в словарь.")

def correct_dictionary(dictionary, incorrect_country, new_country, new_capital):
    if incorrect_country in dictionary:
        dictionary[new_country] = dictionary.pop(incorrect_country)
        dictionary[new_country] = new_capital
        print("Значение в словаре исправлено.")
    else:
        print("Введенное значение отсутствует в словаре.")

def test_knowledge(dictionary):
    total_questions = len(dictionary)
    correct_answers = 0

    questions = list(dictionary.keys())
    random.shuffle(questions)

    for question in questions:
        answer = input(f"Введите столицу страны {question}: ")
        if answer.lower() == dictionary[question].lower():
            correct_answers += 1
            print("Правильно!")
        else:
            print("Неправильно!")

    percentage = (correct_answers / total_questions) * 100
    print(f"\nВы правильно ответили на {percentage:.2f}% вопросов.")