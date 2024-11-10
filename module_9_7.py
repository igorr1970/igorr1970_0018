def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        for i in range(2, number):
            if number % i == 0:
                print("Составное")
                break
        else:
            print("Простое")

        return number

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)


def is_prime(func):
    def wrapper(*args):
        result = func(*args)  # Вызываем оригинальную функцию
        if result < 2:
            print("Составное")
            return result
        for i in range(2, int(result**0.5) + 1):
            if result % i == 0:
                print("Составное")
                return result
        print("Простое")
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

# Пример использования
result = sum_three(2, 3, 6)
print(result)