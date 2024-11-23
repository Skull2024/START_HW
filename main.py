from exhibit import Exhibit
from animal import Lion, Elephant, Penguin, Tiger
from staff import Zookeeper, Vet, Zootech
from zoo import Zoo

def main():
    city_zoo = Zoo()
    while True:
        print("\n=== Меню Зоопарка ===")
        print("1. Добавить вольер")
        print("2. Удалить вольер")
        print("3. Добавить животное")
        print("4. Удалить животное")
        print("5. Добавить сотрудника")
        print("6. Удалить сотрудника")
        print("7. Показать все вольеры и животных в них")
        print("8. Показать всех животных (+ распределитель)")
        print("9. Показать всех сотрудников")
        print("10. Распределить животных по вольерам")
        print("11. Выполнить ежедневную работу")
        print("12. Завершить и выйти")
        try:
            choice = int(input("Выберите действие: "))
        except ValueError:
            print("Некорректный ввод. Введите число.")
            continue

        if choice == 1:
            name = input("Введите название вольера: ").strip().lower()
            location = input("Введите расположение вольера: ")
            exhibit = Exhibit(name, location)
            city_zoo.add_exhibit(exhibit)

        elif choice == 2:
            exhibit_name = input("Введите название вольера для удаления: ")
            city_zoo.remove_exhibit(exhibit_name)

        elif choice == 3:
            species = input("Введите вид животного (Лев, Слон, Пингвин, Тигр): ").strip().lower()
            name = input("Введите имя животного: ")
            try:
                age = int(input("Введите возраст животного: "))
            except ValueError:
                print("Возраст должен быть числом.")
                continue
            endangered = input("Животное под угрозой исчезновения? (да/нет): ").strip().lower() == "да"
            if species == "лев":
                animal = Lion(name, age, endangered)
            elif species == "слон":
                animal = Elephant(name, age, endangered)
            elif species == "пингвин":
                animal = Penguin(name, age, endangered)
            elif species == "тигр":
                animal = Tiger(name, age, endangered)
            else:
                print("Неизвестный вид животного!")
                continue
            city_zoo.add_animal_to_pool(animal)

        elif choice == 4:
            animal_name = input("Введите имя животного для удаления: ")
            for animal in city_zoo.animal_pool:
                if animal.name == animal_name:
                    city_zoo.animal_pool.remove(animal)
                    print(f"Животное {animal_name} удалено из распределителя.")
                    break
            else:
                print("Животное не найдено в распределителе. Проверьте вольеры.")
                for exhibit in city_zoo.exhibits:
                    for animal in exhibit.animal_list:
                        if animal.name == animal_name:
                            exhibit.remove_animal(animal)
                            print(f"Животное {animal_name} удалено из вольера '{exhibit.name}'.")
                            break

        elif choice == 5:
            position = input("Введите должность (Смотритель, Ветеринар, Зоотехник): ").strip().lower()
            name = input("Введите имя сотрудника: ")
            try:
                age = int(input("Введите возраст сотрудника: "))
            except ValueError:
                print("Возраст должен быть числом.")
                continue
            if position == "смотритель":
                staff = Zookeeper(name, age)
            elif position == "ветеринар":
                staff = Vet(name, age)
            elif position == "зоотехник":
                staff = Zootech(name, age)
            else:
                print("Неизвестная должность!")
                continue
            city_zoo.add_staff(staff)

        elif choice == 6:
            staff_name = input("Введите имя сотрудника для удаления: ")
            city_zoo.remove_staff(staff_name)

        elif choice == 7:
            city_zoo.show_all_exhibits()

        elif choice == 8:
            city_zoo.show_all_animals()

        elif choice == 9:
            city_zoo.show_all_staff()

        elif choice == 10:
            city_zoo.distribute_animals().strip().lower()

        elif choice == 11:
            print("Ежедневные операции начались...")
            for staff_member in city_zoo.staff:
                staff_member.work()
            print("Ежедневные операции завершены.")

        elif choice == 12:
            print("Выход из программы. До свидания!")
            break

        else:
            print("Некорректный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
