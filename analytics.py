import pandas as pd
import matplotlib.pyplot as plt


def export_books_to_csv(books, filename="books.csv"):
    if not books.empty:
        books.to_csv(filename, index=False)
        print(f"Данные успешно экспортированы в {filename}.")
    else:
        print("Нет данных для экспорта.")

def visualize_books(books, by="genre"):
    """
    Создаёт график распределения книг.
    :param books: DataFrame с данными о книгах.
    :param by: Поле для группировки ('genre', 'author', 'year').
    """
    column_mapping = {"genre": "genre", "author": "author", "year": "year"}
    group_by_column = column_mapping.get(by)

    if not group_by_column:
        print("Некорректный параметр 'by'. Используйте 'genre', 'author' или 'year'.")
        return

    if books.empty:
        print("Нет данных для отображения.")
        return

    try:
        counts = books[group_by_column].value_counts()
        counts.plot(kind="bar", title=f"Распределение книг по {group_by_column}")
        plt.xlabel(group_by_column.capitalize())
        plt.ylabel("Количество")
        plt.xticks(rotation=45)
        plt.show()
    except KeyError:
        print(f"Ошибка: столбец '{group_by_column}' отсутствует в данных.")

