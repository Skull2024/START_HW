class Staff:
    def __init__(self, name, position, age):
        self.name = name
        self.position = position
        self.age = age

    def work(self):
        print(f"{self.name} ({self.position}) работает.")

    def report(self, exhibit):
        print(f"{self.name} готовит отчет о состоянии вольера '{exhibit.name}':")
        exhibit.show_all_animals()

class Zookeeper(Staff):
    def __init__(self, name, age):
        super().__init__(name, "Смотритель", age)

    def work(self):
        print(f"{self.name} кормит животных.")

    def feed_animal(self, animal, food):
        print(f"{self.name} кормит {animal.name} ({animal.species}) {food}.")

class Vet(Staff):
    def __init__(self, name, age):
        super().__init__(name, "Ветеринар", age)

    def work(self):
        print(f"{self.name} проверяет здоровье животных.")

    def check_health(self, animal):
        print(f"{self.name} проверяет здоровье {animal.name} ({animal.species}).")
        health_status = "здоров" if not animal.is_endangered else "требует особого внимания"
        print(f"Здоровье {animal.name}: {health_status}.")

class Zootech(Staff):
    def __init__(self, name, age):
        super().__init__(name, "Зоотехник", age)

    def work(self):
        print(f"{self.name} занимается разведением животных.")

    def animal_breeding(self, animal):
        print(f"{self.name} занимается разведением и уходом за {animal.name} ({animal.species}).")
        if animal.is_endangered:
            print(f"Особое внимание уделяется {animal.name}, так как он под угрозой исчезновения.")
