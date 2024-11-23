class Animal:
    def __init__(self, name, species, age, is_endangered, food):
        self.name = name
        self.species = species
        self.age = age
        self.is_endangered = is_endangered
        self.food = food
    
    def make_sound(self):
        print(f"{self.name} издает звуки!")

    def eat(self):
        print(f"{self.name} ({self.species}) ест {self.food}.")

    def sleep(self):
        print(f"{self.name} ({self.species}) спит.")

    def get_info(self):
        endangered_status = "под угрозой исчезновения" if self.is_endangered else "не под угрозой"
        return (f"Имя: {self.name}\n"
                f"Вид: {self.species}\n"
                f"Возраст: {self.age} лет\n"
                f"Статус: {endangered_status}\n"
                f"Еда: {self.food}")
    
class Lion(Animal):
    def __init__(self, name, age, is_endangered):
        super().__init__(name, "Лев", age, is_endangered, "мясо")

    def make_sound(self):
        print("Ррр!")

    def hunt(self):
        print(f"{self.name} охотится на дичь!")

class Elephant(Animal):
    def __init__(self, name, age, is_endangered):
        super().__init__(name, "Слон", age, is_endangered, "фрукты и трава")

    def make_sound(self):
        print("Ууууу!")

    def spray_water(self):
        print(f"{self.name} разбрызгивает воду из хобота!")

class Penguin(Animal):
    def __init__(self, name, age, is_endangered):
        super().__init__(name, "Пингвин", age, is_endangered, "рыба")

    def make_sound(self):
        print("Куик куик!")

    def swim(self):
        print(f"{self.name} плывёт в ледяной воде!")

class Tiger(Animal):
    def __init__(self, name, age, is_endangered):
        super().__init__(name, "Тигр", age, is_endangered, "мясо")

    def make_sound(self):
        print("КРРррррр!")

    def swim(self):
        print(f"{self.name} высоко прыгает!")
