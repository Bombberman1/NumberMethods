def equation(x):
    return x ** 3 + x + 3


def derivative(x):
    return 1 + 3 * x ** 2


def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) > 0:
        raise ValueError("Функція має однаковий знак на кінцях інтервалу.")

    iteration = 0
    while (b - a) / 2 > tol and iteration < max_iter:
        c = (a + b) / 2
        if func(c) == 0:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iteration += 1

    return (a + b) / 2


a = -3
b = 2

result = bisection_method(equation, a, b)

print(f"Корінь рівняння на інтервалі [{a}, {b}] знаходиться при x = {result}")
