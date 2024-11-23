from exhibit import Exhibit
from animal import Animal

class Zoo:
    def __init__(self):
        self.exhibits = []
        self.staff = []
        self.animal_pool = []  

    def add_animal_to_pool(self, animal):
        if isinstance(animal, Animal):
            self.animal_pool.append(animal)
            print(f"Животное {animal.name} ({animal.species}) добавлено в распределитель.")
        else:
            print("Добавить можно только объект класса Animal или его подкласса.")

    def distribute_animals(self):
        if not self.exhibits:
            print("Нет вольеров для распределения животных.")
            return
        if not self.animal_pool:
            print("Распределитель животных пуст.")
            return

        print("\n=== Распределение животных ===")
        for animal in list(self.animal_pool):
            print(f"Животное: {animal.name} ({animal.species})")
            exhibit_name = input("Введите название вольера для этого животного (или оставьте пустым для пропуска): ")
            exhibit = next((e for e in self.exhibits if e.name == exhibit_name), None)
            if exhibit:
                exhibit.add_animal(animal)
                self.animal_pool.remove(animal)
                print(f"{animal.name} перемещен в вольер '{exhibit.name}'.")
            else:
                print("Вольер не найден. Животное остаётся в распределителе.")

    def show_all_animals(self):
        if not self.animal_pool and not any(exhibit.animal_list for exhibit in self.exhibits):
            print("В зоопарке пока нет животных.")
            return

        print("\n=== Все животные в зоопарке ===")

        if self.animal_pool:
            print("\nЖивотные в распределителе:")
            for animal in self.animal_pool:
                print(animal.get_info())
                print("-" * 30)

        for exhibit in self.exhibits:
            if exhibit.animal_list:
                print(f"\nВольер '{exhibit.name}' (Расположение: {exhibit.location}):")
                for animal in exhibit.animal_list:
                    print(animal.get_info())
                    print("-" * 30)

    def add_exhibit(self, exhibit):
        if any(e.name == exhibit.name for e in self.exhibits):
            print(f"Вольер с названием '{exhibit.name}' уже существует.")
            return
        self.exhibits.append(exhibit)
        print(f"Вольер '{exhibit.name}' добавлен в зоопарк.")
    
    def show_all_exhibits(self):
        if not self.exhibits:
            print("В зоопарке пока нет вольеров.")
        else:
            print("\nСписок всех вольеров и животных в них:")
            for exhibit in self.exhibits:
                print(f"\nВольер '{exhibit.name}' (Расположение: {exhibit.location}):")
                exhibit.show_all_animals()

    def show_all_staff(self):
        if not self.staff:
            print("В зоопарке пока нет сотрудников.")
        else:
            print("\n=== Все сотрудники зоопарка ===")
            for staff_member in self.staff:
                print(f"Имя: {staff_member.name}")
                print(f"Должность: {staff_member.position}")
                print(f"Возраст: {staff_member.age}")
                print("-" * 30)


    def remove_exhibit(self, exhibit_name):
        exhibit = next((e for e in self.exhibits if e.name == exhibit_name), None)
        if exhibit:
            if not exhibit.animal_list:
                self.exhibits.remove(exhibit)
                print(f"Вольер '{exhibit.name}' удалён из зоопарка.")
            else:
                print(f"Невозможно удалить вольер '{exhibit.name}', в нём ещё есть животные.")
        else:
            print(f"Вольер '{exhibit_name}' не найден.")
    
    def add_staff(self, staff):
        if any(s.name == staff.name for s in self.staff):  
            print(f"Сотрудник с именем '{staff.name}' уже работает в зоопарке.")
            return
        self.staff.append(staff)
        print(f"Сотрудник '{staff.name}' добавлен в зоопарк.")
    
    def remove_staff(self, staff_name):
        staff_member = next((s for s in self.staff if s.name == staff_name), None)
        if staff_member:
            self.staff.remove(staff_member)
            print(f"Сотрудник '{staff_name}' удалён из зоопарка.")
        else:
            print(f"Сотрудник '{staff_name}' не найден.")









        def save_data_to_file(self, file_name="zoo_data.txt"):
            with open(file_name, "w", encoding="utf-8") as file:
                # Сохраняем сотрудников
                file.write("Сотрудники:\n")
                for staff in self.staff:
                    file.write(f"{staff.name}|{staff.position}|{staff.age}\n")
                
                # Сохраняем животных из распределителя
                file.write("\nРаспределитель животных:\n")
                for animal in self.animal_pool:
                    file.write(f"{animal.name}|{animal.species}|{animal.age}|{animal.is_endangered}|{animal.food}\n")
                
                # Сохраняем вольеры и животных в них
                file.write("\nВольеры:\n")
                for exhibit in self.exhibits:
                    file.write(f"{exhibit.name}|{exhibit.location}\n")
                    for animal in exhibit.animal_list:
                        file.write(f"  {animal.name}|{animal.species}|{animal.age}|{animal.is_endangered}|{animal.food}\n")
            print(f"Данные зоопарка сохранены в файл {file_name}.")

        def load_data_from_file(self, file_name="zoo_data.txt"):
            if not os.path.exists(file_name):
                print(f"Файл {file_name} не найден. Начинаем с пустого зоопарка.")
                return

            with open(file_name, "r", encoding="utf-8") as file:
                lines = file.readlines()

            section = None
            for line in lines:
                line = line.strip()
                if line == "Сотрудники:":
                    section = "staff"
                elif line == "Распределитель животных:":
                    section = "animal_pool"
                elif line == "Вольеры:":
                    section = "exhibits"
                elif line.startswith("  "):  # Животное в вольере
                    if section == "exhibits" and self.exhibits:
                        data = line.strip().split("|")
                        animal = Animal(data[0], data[1], int(data[2]), data[3] == "True", data[4])
                        self.exhibits[-1].add_animal(animal)
                elif "|" in line:
                    data = line.split("|")
                    if section == "staff":
                        staff = Staff(data[0], data[1], int(data[2]))
                        self.staff.append(staff)
                    elif section == "animal_pool":
                        animal = Animal(data[0], data[1], int(data[2]), data[3] == "True", data[4])
                        self.animal_pool.append(animal)
                    elif section == "exhibits":
                        exhibit = Exhibit(data[0], data[1])
                        self.exhibits.append(exhibit)

            print(f"Данные зоопарка загружены из файла {file_name}.")