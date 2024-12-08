import sqlite3
import pandas as pd
from tabulate import tabulate


class Bookstore:
    def __init__(self, db_name="library.db"):
        """
        Инициализация объекта Bookstore.
        Загружает данные из базы данных в DataFrame.
        """
        self.db_name = db_name
        self.books = self.load_books()

    def load_books(self):
        """
        Загружает книги из базы данных в DataFrame.
        """
        try:
            with sqlite3.connect(self.db_name) as connection:
                query = "SELECT * FROM books"
                books = pd.read_sql_query(query, connection)
                # Приведение типов
                books['title'] = books['title'].astype(str)
                books['author'] = books['author'].astype(str)
                books['year'] = books['year'].astype(int)
                books['genre'] = books['genre'].astype(str)
                books['price'] = books['price'].astype(float)
                books['amount'] = books['amount'].astype(int)
            return books
        except Exception as e:
            print(f"Ошибка загрузки данных: {e}")
            return pd.DataFrame(columns=['id', 'title', 'author', 'year', 'genre', 'price', 'amount'])


    def sync_with_db(self):
        """
        Синхронизирует DataFrame с базой данных.
        """
        try:
            with sqlite3.connect(self.db_name) as connection:
                self.books.to_sql("books", connection, if_exists="replace", index=False)
                print("Данные успешно синхронизированы с базой данных.")
        except sqlite3.Error as e:
            print(f"Ошибка синхронизации с базой данных: {e}")

    def add_book(self, title, author, year, genre, price, quantity):
        """
        Добавляет книгу в базу данных и обновляет DataFrame.
        """
        if not self.books.empty and title.strip().lower() in self.books['title'].str.lower().values:
            print(f"Книга '{title}' уже существует.")
            return

        try:
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO books (title, author, year, genre, price, amount)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (title.strip(), author.strip(), year, genre.strip(), price, quantity))
                connection.commit()
                print(f"Книга '{title}' успешно добавлена!")

                # Обновляем DataFrame
                self.books = self.load_books()
        except sqlite3.Error as e:
            print(f"Ошибка добавления книги: {e}")

    def delete_books(self):
        """
        Удаляет книги по выбранному пользователем критерию: ID, названию или автору.
        """
        print("\nВыберите способ удаления:")
        print("1. Показать все книги и выбрать ID")
        print("2. Удалить книги по названию")
        print("3. Удалить книги по автору")

        choice = input("Ваш выбор: ")

        if choice == "1":
            # Показать книги и выбрать ID для удаления
            self.display_books()
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                if book_id in self.books['id'].values:
                    self.books = self.books[self.books['id'] != book_id].reset_index(drop=True)
                    print(f"Книга с ID {book_id} успешно удалена.")
                    self.sync_with_db()
                else:
                    print("Книга с указанным ID не найдена.")
            except ValueError:
                print("Некорректный ввод ID. Пожалуйста, введите число.")

        elif choice == "2":
            # Удалить книги по названию
            title = input("Введите название книги для удаления: ").strip().lower()
            books_to_delete = self.books[self.books['title'].str.lower() == title]
            if not books_to_delete.empty:
                self.books = self.books[self.books['title'].str.lower() != title].reset_index(drop=True)
                print(f"Все книги с названием '{title}' успешно удалены.")
                self.sync_with_db()
            else:
                print(f"Книга с названием '{title}' не найдена.")

        elif choice == "3":
            # Удалить книги по автору
            author = input("Введите автора для удаления всех его книг: ").strip().lower()
            books_to_delete = self.books[self.books['author'].str.lower() == author]
            if not books_to_delete.empty:
                self.books = self.books[self.books['author'].str.lower() != author].reset_index(drop=True)
                print(f"Все книги автора '{author}' успешно удалены.")
                self.sync_with_db()
            else:
                print(f"Книги автора '{author}' не найдены.")

        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")

    def display_books(self, books=None):
        """
        Выводит список книг в формате таблицы.
        :param books: DataFrame с книгами для отображения. Если None, отображает весь каталог.
        """
        books_to_display = books if books is not None else self.books
        if not books_to_display.empty:
            print(tabulate(books_to_display, headers='keys', tablefmt='grid', showindex=False))
        else:
            print("Нет книг для отображения.")


    def search_books(self, criteria, query):
        """
        Ищет книги по заданным критериям и возвращает DataFrame с результатами.
        :param criteria: Критерий поиска ('Название', 'Автор', 'Год', 'Жанр').
        :param query: Запрос для поиска.
        """
        query = query.strip().lower()
        column_mapping = {
            "Название": "title",
            "Автор": "author",
            "Год": "year",
            "Жанр": "genre"
        }
        column = column_mapping.get(criteria)
        if not column:
            print("Некорректный критерий поиска.")
            return pd.DataFrame()

        try:
            # Преобразуем значения столбца в строки перед использованием `.str`
            results = self.books[self.books[column].astype(str).str.lower() == query]
            if results.empty:
                print("Книги не найдены.")
            return results
        except KeyError:
            print(f"Ошибка: столбец '{column}' отсутствует в данных.")
            return pd.DataFrame()

    def buy_book(self):
        """
        Позволяет пользователю выбрать способ покупки книги: по ID, названию или автору.
        """
        print("\nВыберите способ покупки книги:")
        print("1. Показать все книги и выбрать ID")
        print("2. Найти книгу по названию")
        print("3. Найти книгу по автору")

        choice = input("Ваш выбор: ")

        if choice == "1":
            # Показать все книги и выбрать ID
            self.display_books()
            try:
                book_id = int(input("Введите ID книги для покупки: "))
                self._process_purchase_by_id(book_id)
            except ValueError:
                print("Некорректный ввод. ID должно быть числом.")

        elif choice == "2":
            # Покупка по названию
            title = input("Введите название книги для покупки: ").strip().lower()
            matching_books = self.books[self.books['title'].str.lower() == title]
            if not matching_books.empty:
                self.display_books(matching_books)
                if len(matching_books) == 1:
                    book_id = matching_books.iloc[0]['id']
                    self._process_purchase_by_id(book_id)
                else:
                    try:
                        book_id = int(input("Несколько книг с этим названием. Введите ID книги: "))
                        self._process_purchase_by_id(book_id)
                    except ValueError:
                        print("Некорректный ввод. ID должно быть числом.")
            else:
                print(f"Книга с названием '{title}' не найдена.")

        elif choice == "3":
            # Покупка по автору
            author = input("Введите имя автора для покупки книги: ").strip().lower()
            matching_books = self.books[self.books['author'].str.lower() == author]
            if not matching_books.empty:
                self.display_books(matching_books)
                try:
                    book_id = int(input("Введите ID книги для покупки: "))
                    self._process_purchase_by_id(book_id)
                except ValueError:
                    print("Некорректный ввод. ID должно быть числом.")
            else:
                print(f"Книги автора '{author}' не найдены.")

        else:
            print("Некорректный выбор. Попробуйте снова.")

    def _process_purchase_by_id(self, book_id):
        """
        Обрабатывает покупку книги по ID.
        :param book_id: ID книги для покупки.
        """
        if book_id not in self.books['id'].values:
            print(f"Книга с ID {book_id} не найдена.")
            return

        try:
            # Проверяем количество книг в DataFrame
            amount = self.books.loc[self.books['id'] == book_id, 'amount'].iloc[0]
            if amount > 0:
                # Уменьшаем количество в базе данных
                with sqlite3.connect(self.db_name) as connection:
                    cursor = connection.cursor()
                    cursor.execute("UPDATE books SET amount = amount - 1 WHERE id = ?", (book_id,))
                    connection.commit()

                # Обновляем DataFrame
                self.books.loc[self.books['id'] == book_id, 'amount'] -= 1
                print("Покупка прошла успешно!")

                # Если количество стало равно 0, уведомляем пользователя
                if self.books.loc[self.books['id'] == book_id, 'amount'].iloc[0] == 0:
                    print(f"Книга с ID {book_id} больше не доступна (количество: 0).")
            else:
                print("Книга закончилась!")
        except sqlite3.Error as e:
            print(f"Ошибка при покупке книги: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
