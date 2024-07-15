import re

# Імпорт модулів з реалізованими командами та парсером
import commands as cmd
import parcer as p

"""
    Функція main з усією логікою інтерфейсу бота для обробки телефонної книги.
    """


def main():
    print("Welcome to the assistant bot!")
    contact_list = {}

    # Запуск циклу обробки введеного користувачем запита.
    while True:
        user_input = input().strip().lower()
        # Форматування запиту для отримання параметрів команди.
        command, parsed_input = p.parse_input(user_input)

        # Виконання команди з перевіркою її валідності
        try:
            # Привітання
            if command == "hello":
                print("How can I help you?")

            # Додавання контакту
            elif command == 'add':
                print(cmd.add_contact(parsed_input, contact_list))

            # Зміна контакту
            elif command == 'change':
                print(cmd.change_contact(parsed_input, contact_list))

            # Відображення контакту
            elif command == 'phone':
                print(cmd.phone_contact(parsed_input, contact_list))

            # Видалення контакту
            elif command == 'delete':
                print(cmd.delete_contact(parsed_input, contact_list))

            # Виведення контакту за іменем
            elif command == 'show':
                print(cmd.show_contact(parsed_input, contact_list))

            # Виведення всіх контактів
            elif command == 'all':
                print(contact_list)

            # Вихід з бота
            elif user_input == "exit" or user_input == "close":
                print("Good bye!")
                exit(0)

            else:
                print("Invalid command.")

        except ValueError as ve:
            print(f"Error: {ve}")


# Виклик функції main, якщо скрипт запущений як основне завдання.
if __name__ == "__main__":
    main()
