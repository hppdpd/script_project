# Імпорт потрібних функцій з модуля lib
from lib import add_numbers, greet_user


def main():
    """
    Головна функція для демонстрації роботи імпортованих методів.
    """
    # Виклик функції привітання
    greeting = greet_user("Версія 1.0")
    print(greeting)

    # Виклик математичної функції
    sum_result = add_numbers(15.5, 4.5)
    print(f"Результат сумування: {sum_result}")


if __name__ == "__main__":
    main()