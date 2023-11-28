def lu_decomposition(matrix):
    n = len(matrix)

    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for k in range(i, n):
            sum_ = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = matrix[i][k] - sum_

        for k in range(i, n):
            if i == k:
                L[i][i] = 1.0
            else:
                sum_ = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (matrix[k][i] - sum_) / U[i][i]

    return L, U


def forward_substitution(L, b):
    n = len(L)
    y = [0.0] * n

    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]

    return y


def backward_substitution(U, y):
    n = len(U)
    x = [0.0] * n

    for i in reversed(range(n)):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x


s = 0.02 * 13
B = 0.02 * 23

matrix = [
    [8.3, 2.62 + s, 4.1, 1.9],
    [3.92, 8.45, 7.78 - s, 2.46],
    [3.77, 7.21 + s, 8.04, 2.28],
    [2.21, 3.65 - s, 1.69, 6.69]
]

for i in range(len(matrix)):
    matrix[i].append(-10.65 + B) if i == 0 else matrix[i].append(12.21) if i == 1 else matrix[i].append(
        15.45 - B) if i == 2 else matrix[i].append(-8.35)

L, U = lu_decomposition(matrix)

y = forward_substitution(L, [row[-1] for row in matrix])
x = backward_substitution(U, y)

print("Розв'язки:")
for i, sol in enumerate(x):
    print(f"x{i + 1} = {sol}")
