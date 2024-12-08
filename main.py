from utils import initialize_database
from bookstore import Bookstore
from person import Person

def main():
    initialize_database()
    bookstore = Bookstore()

    print("Добро пожаловать в книжный магазин!")
    while True:
        print("\nВыберите роль:")
        print("1. Продавец")
        print("2. Покупатель")
        role_choice = input("Ваш выбор: ")

        if role_choice == "1":
            code = input("Введите код продавца: ")
            try:
                person = Person(bookstore, "продавец", code)
                break
            except PermissionError:
                print("Неверный код доступа! Попробуйте снова.")
        elif role_choice == "2":
            person = Person(bookstore, "покупатель")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

    # Переходим в меню в зависимости от роли
    person.menu()

if __name__ == "__main__":
    main()
