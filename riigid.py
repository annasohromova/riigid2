from module1 import *




# Файл словаря
file_path = "dictionary.txt"

while True:
    print("-------- Меню --------")
    print("1. Отобразить столицу или страну")
    print("2. Добавить значение в словарь")
    print("3. Исправить значение в словаре")
    print("4. Проверить знания")
    print("5. Сохранить словарь и выйти")

    choice = input("Введите номер выбранной опции: ")

    if choice == "1":
        input_value = input("Введите название страны или столицы: ")
        display_capital_or_country(dictionary, input_value)
    elif choice == "2":
        country = input("Введите название страны: ")
        capital = input("Введите название столицы: ")
        add_to_dictionary(dictionary, country, capital)
    elif choice == "3":
        incorrect_country = input("Введите неправильно введенную страну: ")
        new_country = input("Введите правильное название страны: ")
        new_capital = input("Введите правильное название столицы: ")
        correct_dictionary(dictionary, incorrect_country, new_country, new_capital)
    elif choice == "4":
        test_knowledge(dictionary)
    elif choice == "5":
        save_dictionary(dictionary, file_path)
        print("Словарь сохранен. Программа завершена.")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите опцию из меню.")
