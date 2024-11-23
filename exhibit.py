from animal import Animal

class Exhibit:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.animal_list = []

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            print("Добавить можно только объект класса Animal или его подкласса.")
            return
        if animal not in self.animal_list:
            self.animal_list.append(animal)
            print(f"{animal.name} добавлен в вольер {self.name}.")
        else:
            print(f"{animal.name} уже находится в вольере {self.name}.")

    def remove_animal(self, animal):
        if animal in self.animal_list:
            self.animal_list.remove(animal)
            print(f"{animal.name} удалён из вольера {self.name}.")
        else:
            print(f"{animal.name} не найден в вольере {self.name}.")

    def show_all_animals(self):
        if not self.animal_list:
            print(f"В вольере {self.name} пока нет животных.")
        else:
            print(f"В вольере {self.name} находятся следующие животные:")
            for animal in self.animal_list:
                print(f"  - {animal.name} ({animal.species})")

    def show_full_info_all_animals(self):
        if not self.animal_list:
            print(f"В вольере '{self.name}' пока нет животных.")
        else:
            print(f"\nПолная информация о животных в вольере '{self.name}':")
            for animal in self.animal_list:
                print(animal.get_info())
                print("-" * 30)


    def __str__(self):
        return f"Вольер '{self.name}' в локации '{self.location}' содержит {len(self.animal_list)} животных."
