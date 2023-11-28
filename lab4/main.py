import math


def f(x):
    return x / (3 + 2 * x ** 2)


def F(x):
    return (1 / 4) * math.log(x ** 2 + (3 / 2))


def simpson_method(a, b, m):
    h = (b - a) / (2 * m)
    result = f(a) + f(b)

    for i in range(1, 2 * m):
        x = a + i * h
        result += 4 * f(x) if i % 2 == 1 else 2 * f(x)

    result *= h / 3
    return result


a = 1
b = 2
m = 10

result_simpson = simpson_method(a, b, m)

F_a = F(a)
F_b = F(b)

print(f"Результат методу Сімпсона: {result_simpson}")
exact_result = (1 / 4) * math.log(b ** 2 + 3 / 2) - (1 / 4) * math.log(a ** 2 + 3 / 2)
print(f"Точний результат: {exact_result}")
print(f"Значення первісної на межах [{a}, {b}]: F({a}) = {F_a}, F({b}) = {F_b}")
