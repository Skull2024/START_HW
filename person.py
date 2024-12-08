from bookstore import Bookstore
from analytics import export_books_to_csv, visualize_books


class Person:
    def __init__(self, bookstore, role, code=None):
        """
        Инициализация пользователя с заданной ролью.
        :param bookstore: объект класса Bookstore
        :param role: роль пользователя ("продавец" или "покупатель")
        :param code: код доступа для продавца
        """
        self.bookstore = bookstore
        self.role = role
        if self.role == "продавец" and code != "12345":
            raise PermissionError("Неверный код доступа!")

    def menu(self):
        """
        Основное меню пользователя в зависимости от его роли.
        """
        if self.role == "покупатель":
            self.buyer_menu()
        elif self.role == "продавец":
            self.seller_menu()

    def buyer_menu(self):
        """
        Меню для покупателя. Позволяет искать, просматривать и покупать книги.
        """
        while True:
            print("\nМеню покупателя:")
            print("1. Показать книги")
            print("2. Найти книгу")
            print("3. Купить книгу")
            print("4. Выйти")

            choice = input("Выберите опцию: ")
            if choice == "1":
                # Показать список всех книг
                self.bookstore.display_books()
            elif choice == "2":
                # Найти книгу
                self.search_books()
            elif choice == "3":
                # Купить книгу
                self.bookstore.buy_book()
            elif choice == "4":
                # Выход из меню
                break
            else:
                print("Некорректный выбор.")


    def seller_menu(self):
        """
        Меню для продавца. Позволяет добавлять, удалять книги, просматривать аналитику и экспортировать данные.
        """
        while True:
            print("\nМеню продавца:")
            print("1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Показать книги")
            print("4. Просмотреть аналитику")
            print("5. Экспортировать данные в CSV")
            print("6. Выйти")

            choice = input("Выберите опцию: ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                try:
                    book_id = int(input("Введите ID книги для удаления: "))
                    self.bookstore.delete_book(book_id)
                except ValueError:
                    print("Некорректный ввод ID.")
            elif choice == "3":
                self.bookstore.display_books()
            elif choice == "4":
                self.view_analytics()
            elif choice == "5":
                export_books_to_csv(self.bookstore.books)
            elif choice == "6":
                break
            else:
                print("Некорректный выбор.")

    def add_book(self):
        """
        Добавление книги в магазин (доступно только для продавца).
        """
        title = input("Название: ")
        author = input("Автор: ")
        try:
            year = int(input("Год: "))
            price = float(input("Цена: "))
            amount = int(input("Количество: "))
        except ValueError:
            print("Некорректный ввод данных.")
            return
        genre = input("Жанр: ")
        self.bookstore.add_book(title, author, year, genre, price, amount)

    def search_books(self):
        """
        Поиск книг по заданным критериям.
        """
        print("\nКритерии поиска:")
        print("1. Название")
        print("2. Автор")
        print("3. Год")
        print("4. Жанр")

        choice = input("Выберите критерий: ")
        mapping = {"1": "Название", "2": "Автор", "3": "Год", "4": "Жанр"}
        criteria = mapping.get(choice)
        if not criteria:
            print("Некорректный выбор.")
            return

        query = input(f"Введите {criteria.lower()}: ")
        results = self.bookstore.search_books(criteria, query)
        if not results.empty:
            print("Найденные книги:")
            self.bookstore.display_books(results)
        else:
            print("Книги не найдены.")

    def view_analytics(self):
        """
        Просмотр аналитики. Визуализация книг по жанрам, авторам и годам.
        """
        while True:
            print("\nМеню аналитики:")
            print("1. Визуализация книг по жанрам")
            print("2. Визуализация книг по авторам")
            print("3. Визуализация книг по годам")
            print("4. Назад")

            choice = input("Выберите опцию: ")
            if choice == "1":
                visualize_books(self.bookstore.books, by="genre")
            elif choice == "2":
                visualize_books(self.bookstore.books, by="author")
            elif choice == "3":
                visualize_books(self.bookstore.books, by="year")
            elif choice == "4":
                break
            else:
                print("Некорректный выбор.")
    def search_books(self):
        """
        Поиск книг по заданным критериям.
        """
        print("\nКритерии поиска:")
        print("1. Название")
        print("2. Автор")
        print("3. Год")
        print("4. Жанр")

        choice = input("Выберите критерий: ")
        mapping = {"1": "Название", "2": "Автор", "3": "Год", "4": "Жанр"}
        criteria = mapping.get(choice)
        if not criteria:
            print("Некорректный выбор.")
            return

        query = input(f"Введите {criteria.lower()}: ")
        results = self.bookstore.search_books(criteria, query)
        if not results.empty:
            print("Найденные книги:")
            self.bookstore.display_books(results)  # Передача найденных книг в display_books
        else:
            print("Книги не найдены.")