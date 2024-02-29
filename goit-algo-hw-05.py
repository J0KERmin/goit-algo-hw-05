# 1:
def caching_fibonacci():
    cache = {}  # Створити порожній словник cache

    def fibonacci(n):
        if n <= 0:  # Якщо n <= 0, повернути 0
            return 0
        if n == 1:  # Якщо n == 1, повернути 1
            return 1
        if n in cache:  # Якщо n у cache, повернути cache[n]
            return cache[n]

        # Якщо число не знаходиться у кеші, обчислити його, зберегти у кеш та повернути результат
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci  # Повернути функцію fibonacci

fibonacci = caching_fibonacci()
print(fibonacci(10))  # Виведе 55
print(fibonacci(15))  # Виведе 6765

# 2:
import re
from typing import Callable

def generator_numbers(text: str):
    # Пошук усіх дійсних чисел у тексті за допомогою регулярного виразу
    pattern = r'\b\d+(?:\.\d+)?\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())  # Повернути знайдене число як дійсне

def sum_profit(text: str, func: Callable):
    # Виклик генератора generator_numbers та підсумування чисел
    return sum(func(text))

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів. Окрім того, він отримує премію у розмірі 5000.50 доларів за високі показники роботи та 100.00 доларів від компанії-партнера за успішне співробітництво."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

# 4:
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please."
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} with phone number {phone} has been added."


@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for {name} has been changed to {new_phone}."
    else:
        return f"Contact {name} not found."


@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"Phone number for {name} is {contacts[name]}."
    else:
        return f"Contact {name} not found."


@input_error
def show_all_contacts(args, contacts):
    if not contacts:
        return "Phone book is empty."
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


@input_error
def search_contact(args, contacts):
    name = args[0]
    if name in contacts:
        return f"Phone number for {name} is {contacts[name]}."
    else:
        return f"No contact with the name {name} found."


@input_error
def parse_input(input_str):
    tokens = input_str.strip().split()
    command = tokens[0].lower()
    args = tokens[1:]
    return command, args


def show_commands():
    return "Available commands:\n" \
           "add <name> <phone_number>: Add a new contact with the given name and phone number.\n" \
           "change <name> <new_phone_number>: Change the phone number for the contact with the given name.\n" \
           "phone <name>: Show the phone number for the contact with the given name.\n" \
           "search <name>: Search for a contact by name.\n" \
           "all: Show all contacts.\n" \
           "close or exit: Exit the program."


def main():
    phone_book = {}
    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)
        if command == "add":
            print(add_contact(args, phone_book))
        elif command == "change":
            print(change_contact(args, phone_book))
        elif command == "phone":
            print(show_phone(args, phone_book))
        elif command == "search":
            print(search_contact(args, phone_book))
        elif command == "all":
            print(show_all_contacts(args, phone_book))
        elif command == "commands":
            print(show_commands())
        elif command == "exit" or command == "close":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Type 'commands' for a list of available commands.")


if __name__ == "__main__":
    main()

