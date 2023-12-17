import matplotlib.pyplot as plt


def runge_kutta_system(x0, y0, x_end, h):
    x_values = []
    y1_values = []
    y2_values = []
    y3_values = []

    x = x0
    y1, y2, y3 = y0

    while x < x_end:
        x_values.append(x)
        y1_values.append(y1)
        y2_values.append(y2)
        y3_values.append(y3)

        k1 = h * f1(x, y1, y2, y3)
        l1 = h * f2(x, y1, y2, y3)
        m1 = h * f3(x, y1, y2, y3)

        k2 = h * f1(x + h / 2, y1 + k1 / 2, y2 + l1 / 2, y3 + m1 / 2)
        l2 = h * f2(x + h / 2, y1 + k1 / 2, y2 + l1 / 2, y3 + m1 / 2)
        m2 = h * f3(x + h / 2, y1 + k1 / 2, y2 + l1 / 2, y3 + m1 / 2)

        k3 = h * f1(x + h / 2, y1 + 2 * k2 - k1, y2 + 2 * l2 - l1, y3 + 2 * m2 - m1)
        l3 = h * f2(x + h / 2, y1 + 2 * k2 - k1, y2 + 2 * l2 - l1, y3 + 2 * m2 - m1)
        m3 = h * f3(x + h / 2, y1 + 2 * k2 - k1, y2 + 2 * l2 - l1, y3 + 2 * m2 - m1)

        y1 = y1 + (k1 + 4 * k2 + k3) / 6
        y2 = y2 + (l1 + 4 * l2 + l3) / 6
        y3 = y3 + (m1 + 4 * m2 + m3) / 6

        x = x + h

    return x_values, y1_values, y2_values, y3_values


def u1(x):
    a = 0.003
    if x % (6 * a) <= 1.5 * a:
        return (x % (6 * a)) * 10 / (1.5 * a)
    elif x % (6 * a) <= 3 * a:
        return 20 - 10 * (x % (6 * a)) / (1.5 * a)
    elif x % (6 * a) <= 4 * a:
        return 30 - 10 * (x % (6 * a)) / a
    elif x % (6 * a) <= 5 * a:
        return -10
    elif x % (6 * a) <= 6 * a:
        return 10 * (x % (6 * a)) / a - 60


def L2(y3):
    L_min = 0.2
    L_max = 2
    R1 = 17
    R2 = 23
    i_min = 1
    i_max = 2
    a0 = (L_min * i_max ** 2 - L_min * i_min ** 2 - L_max * i_max ** 2 + L_max * i_min ** 2) / (i_max ** 2 - i_min ** 2)
    a1 = a0 + R1 * i_min
    a2 = a0 + R1 * i_max
    a3 = a0 + R2 * i_max

    if abs(y3) <= 1:
        return 2
    elif abs(y3) <= 2:
        return a0 + a1 * (abs(y3)) + a2 * (abs(y3) ** 2) + a3 * (abs(y3) ** 3)
    else:
        return 0.2


def f1(x, y1, y2, y3):
    return (u1(x) - y1 + y3 * 70) / ((70 + 17) * 0.3 * 10 ** (-3))


def f2(x, y1, y2, y3):
    return y3 / (2 * 10 ** (-3))


def f3(x, y1, y2, y3):
    return (((u1(x) - y1 + y3 * 70) / (70 + 17) - y3) * 70 - y3 * (31 + 17) + y2)/L2(y3)


x0 = 0
y0 = [0, 0, 0]
x_end = 0.09
h = 0.000225

x_values, y1_values, y2_values, y3_values = runge_kutta_system(x0, y0, x_end, h)


plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.plot(x_values, y1_values)
plt.title("Напруга на конденсаторі 1 (y1)")
plt.xlabel("Час")
plt.ylabel("Значення")

plt.subplot(3, 2, 2)
plt.plot(x_values, y2_values)
plt.title("Напруга на конденсаторі 2 (y2)")
plt.xlabel("Час")
plt.ylabel("Значення")

plt.subplot(3, 2, 3)
plt.plot(x_values, y3_values)
plt.title("Струм в індуктивності (y3)")
plt.xlabel("Час")
plt.ylabel("Значення")

plt.subplot(3, 2, 4)
plt.plot(x_values, [elem * 110 for elem in y3_values])
plt.title("Напруга  U2 (110*y3)")
plt.xlabel("Час")
plt.ylabel("Значення")

plt.subplot(3, 2, 5)
plt.plot(x_values, [u1(elem) for elem in x_values])
plt.title("Напруга  U1 (x)")
plt.xlabel("Час")
plt.ylabel("Значення")
plt.tight_layout()
plt.show()