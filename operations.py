class MathOperations:
    def add(self, numbers):
        return sum(numbers)

    def subtract(self, numbers):
        result = numbers[0]
        for n in numbers[1:]:
            result -= n
        return result

    def multiply(self, numbers):
        result = 1
        for n in numbers:
            result *= n
        return result

    def divide(self, numbers):
        result = numbers[0]
        for n in numbers[1:]:
            if n == 0:
                return "Ошибка: делить на ноль нельзя"
            result /= n
        return result

    def power(self, a, b):
        return a ** b

    def remainder(self, a, b):
        if b == 0:
            return "Ошибка: делить на ноль нельзя"
        return a % b

    def sqrt(self, a):
        return math.sqrt(a)

    def percentage(self, a, b):
        return a * (b / 100)