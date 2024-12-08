import sqlite3

def initialize_database(db_name: str = "library.db") -> None:
    """Создаёт базу данных и таблицу books, если они отсутствуют."""
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    year INTEGER NOT NULL,
                    genre TEXT NOT NULL,
                    price REAL NOT NULL,
                    amount INTEGER NOT NULL
                )
            """)
            print(f"База данных '{db_name}' успешно инициализирована.")
    except sqlite3.Error as e:
        print(f"Ошибка при инициализации базы данных: {e}")
