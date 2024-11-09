# Калькулятор для проведения арифметических операций
while True:
    print("\nДоступные операции:")
    print("+ - сложение")
    print("- - вычитание")
    print("* - умножение")
    print("/ - деление")
    print("^ - возведение в степень")
    print("% - остаток от деления")
    print("! - выход из программы")
    operation = input("Выберите операцию: ")
    if operation == '!':
        print("Выход из программы.")
        break
    mode = input("Выберите режим (i - целые числа, f - вещественные числа): ").lower()
    if mode not in ['i', 'f']:
        print("Некорректный режим. Пожалуйста, выберите 'i' или 'f'.")
        continue
    try:
        a = float(input("Введите первое число: ")) if mode == 'f' else int(input("Введите первое число: "))
        b = float(input("Введите второе число: ")) if mode == 'f' else int(input("Введите второе число: "))
    except ValueError:
        print("Введено неправильное значение. Попробуйте снова.")
        continue
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        result = "Ошибка: делить на ноль нельзя" if b == 0 else a / b
    elif operation == '^':
        result = a ** b
    elif operation == '%':
        result = "Ошибка: делить на ноль нельзя" if b == 0 else a % b
    else:
        result = "Неправильная операция!"
    print(f"Результат: {result}")
    continue_program = input("Хотите продолжить? (Y - Yes/N - No(в любом регистре)): ").lower()
    if continue_program == 'n':
        print("Выход из программы.")
        break
