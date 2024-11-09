class Sotrudnik:
    def __init__(self, name, position, base_zp):
        self.name = name
        self.position = position
        self.base_zp = base_zp

    def total_info(self):
        print(f"Имя: {self.name}")
        print(f"Позиция: {self.position}")
        print(f"Базовая зарплата: {self.base_zp}")


class Razrab(Sotrudnik):
    def __init__(self, name, base_zp, project_bonus):
        super().__init__(name, "Разработчик", base_zp)
        self.project_bonus = project_bonus

    def total_zp(self):
        return self.base_zp + self.project_bonus

    def total_info(self):
        print(f"Имя: {self.name}")
        print(f"Позиция: {self.position}")
        print(f"Базовая зарплата: {self.base_zp}")
        print(f"Премия за проект: {self.project_bonus}")
        print(f"Итоговая зарплата: {self.total_zp()}")


class TeamLead(Razrab):
    def __init__(self, name, base_zp, project_bonus, leadership_bonus):
        super().__init__(name, base_zp, project_bonus)
        self.position = "TeamLead"
        self.leadership_bonus = leadership_bonus

    def total_zp(self):
        return super().total_zp() + self.leadership_bonus

    def total_info(self):
        print(f"Имя: {self.name}")
        print(f"Позиция: {self.position}")
        print(f"Базовая зарплата: {self.base_zp}")
        print(f"Бонус за проект: {self.project_bonus}")
        print(f"Бонус за лидерство: {self.leadership_bonus}")
        print(f"Итоговая зарплата: {self.total_zp()}")


class Director(Sotrudnik):
    def __init__(self, name, base_zp):
        super().__init__(name, "Директор", base_zp)

    def total_info(self):
        print(f"Имя: {self.name}")
        print(f"Позиция: {self.position}")
        print(f"Базовая зарплата: {self.base_zp}")


class HR(Sotrudnik):
    def __init__(self, name, base_zp):
        super().__init__(name, "HR", base_zp)

    def total_info(self):
        print(f"Имя: {self.name}")
        print(f"Позиция: {self.position}")
        print(f"Базовая зарплата: {self.base_zp}")


class Manager(Sotrudnik):
    def __init__(self, name, base_zp, bonus):
        super().__init__(name, "Менеджер", base_zp)
        self.bonus = bonus

    def total_zp(self):
        return self.base_zp + self.bonus

    def total_info(self):
        print(f"Имя: {self.name}")
        print(f"Позиция: {self.position}")
        print(f"Базовая зарплата: {self.base_zp}")
        print(f"Бонус: {self.bonus}")
        print(f"Итоговая зарплата: {self.total_zp()}")

director = Director("Bekzat", 3000000)
HR_comp = HR("Altynai", 2000000)
Razrab1 = Razrab("Fedor", 1800000, 300000)
Razrab2 = Razrab("Rustam", 1750000, 250000)
Razrab3 = Razrab("Botagoz", 1850000, 350000)
Razrab4 = Razrab("Sanzhar", 1500000, 200000)
teamlead = TeamLead("Rakhym", 2200000, 450000, 100000)
manager1 = Manager("Helene", 1500000, 100000)
manager2 = Manager("Oleg", 1500000, 100000)

director.total_info()
print("\n______________________\n")
HR_comp.total_info()
print("\n______________________\n")
Razrab1.total_info()
print("\n______________________\n")
Razrab2.total_info()
print("\n______________________\n")
Razrab3.total_info()
print("\n______________________\n")
Razrab4.total_info()
print("\n______________________\n")
teamlead.total_info()
print("\n______________________\n")
manager1.total_info()
print("\n______________________\n")
manager2.total_info()
print("\n______________________\n")