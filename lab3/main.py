import math


def f(x1, x2):
    eq1 = 1 - math.exp(-x1) * math.cos(x2) - x1
    eq2 = math.exp(-x1) * math.sin(x2) + 1 - x2
    return [eq1, eq2]


def jacobian(x1, x2):
    df1_dx1 = math.exp(-x1) * math.cos(x2) - 1
    df1_dx2 = x1 * math.exp(-x1) * math.sin(x2)
    df2_dx1 = -x1 * math.exp(-x1) * math.sin(x2)
    df2_dx2 = math.exp(-x1) * math.cos(x2) - 1
    return [[df1_dx1, df1_dx2], [df2_dx1, df2_dx2]]


def gauss_elimination(A, B):
    n = len(A)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_index][i]):
                max_index = j

        A[i], A[max_index] = A[max_index], A[i]
        B[i], B[max_index] = B[max_index], B[i]

        for j in range(i + 1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= ratio * A[i][k]
            B[j] -= ratio * B[i]

    X = [0] * n
    for i in range(n - 1, -1, -1):
        X[i] = B[i] / A[i][i]
        for j in range(i - 1, -1, -1):
            B[j] -= A[j][i] * X[i]

    return X


def newton_method(x1_0, x2_0, epsilon, max_iter):
    x1 = x1_0
    x2 = x2_0

    for iteration in range(max_iter):
        F = f(x1, x2)
        J = jacobian(x1, x2)

        delta = gauss_elimination(J, F)

        x1 -= delta[0]
        x2 -= delta[1]

        if abs(delta[0]) < epsilon and abs(delta[1]) < epsilon:
            break

    return x1, x2, iteration + 1


x1_0 = 0.1
x2_0 = 0.1

epsilon = 1e-5
max_iter = 100

result = newton_method(x1_0, x2_0, epsilon, max_iter)

print("Результат:")
print("x1 =", result[0])
print("x2 =", result[1])
print("Кількість ітерацій:", result[2])
