def input_error(func):
    """Декоратор для handler функцій"""
    def inner(*args, **kwargs):
        """Перевіряє наявність KeyError, ValueError, IndexError в будь-якій з команд.

            Параметри:
                args (list[str]): Список з іменем та номером бажаного контакту.
                kwargs (dict): Словник (телефонна книга) з контактами та їх телефонами.

            Повертає:
                str: Повідомлення про помилку.
            """

        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please indicate a name and a phone."
        except KeyError:
            return "No such contact found."
        except IndexError:
            return "Please indicate a name and a phone."

    return inner


"""
    Додає контакт до книги.

    Параметри:
    args (list[str]): Список з іменем та номером бажаного контакту.
    contacts (dict): Словник (телефонна книга) з контактами та їх телефонами.

    Повертає:
    str: Результат додавання контакту.
    """


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


"""
    Змінює номер телефону контакту у книзі.

    Параметри:
    args (list[str]): Список з іменем та номером бажаного контакту.
    contacts (dict): Словник (телефонна книга) з контактами та їх телефонами.

    Повертає:
    str: Результат зміни контакту або результат невдачі.
    """


@input_error
def change_contact(args, contacts):
    contacts.update({args[0]: args[1]})
    return "Contact changed"


"""
    "Телефонує" заданому контакту з книги.

    Параметри:
    args (list[str]): Список з іменем бажаного контакту.
    contacts (dict): Словник (телефонна книга) з контактами та їх телефонами.

    Повертає:
    str: Результат телефонування контакту або результат невдачі.
    """


@input_error
def phone_contact(args, contacts):
    return contacts[args[0]]


"""
    Відображає номер телефону контакту у книзі.

    Параметри:
    args (list[str]): Список з іменем бажаного контакту.
    contacts (dict): Словник (телефонна книга) з контактами та їх телефонами.

    Повертає:
    str: Рядок з ім'ям та номером контакту або результат невдачі.
    """


@input_error
def show_contact(args, contacts):
    return f"{args[0]}'s phone number: {contacts[args[0]]}"


"""
    Видаляє контакт у книзі.

    Параметри:
    args (list[str]): Список з іменем бажаного контакту.
    contacts (dict): Словник (телефонна книга) з контактами та їх телефонами.

    Повертає:
    str: Результат видалення контакту або результат невдачі.
    """


@input_error
def delete_contact(args, contacts):
    del contacts[args[0]]
    return "Contact deleted"
