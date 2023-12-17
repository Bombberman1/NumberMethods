import matplotlib.pyplot as plt
from math import sin, pi

'''
    L1    R1                  R2
0--^^^^^|___|--------|-------|____|-------|----------0
^                    |                    |          ^
|                    >                  _____        |
|                    < L2           C1  _____     U2 |
| U1                 >                    |          |
|                    <                    |          |
|                    |                    |          |
0--------------------|--------------------|----------0
'''

Umax = 100
f = 50
R1 = 5
R2 = 4
R3 = 7
R4 = 2
L1 = 0.01
L2 = 0.02
C1 = 300 * 10 ** (-6)
C2 = 150 * 10 ** (-6)
t_integration = 0.2
h = 0.00001


U1 = lambda t: Umax * sin(2 * pi * f * t)
U2_0 = 0
I_L1_0 = 0
I_L2_0 = 0
U_C1_0 = 0


def dU2_dt(U1, U2, I_L1, I_L2, U_C1):
    return (U1 - U2 - R1 * I_L1) / L1


def euler_method(U1, U2_0, I_L1_0, I_L2_0, U_C1_0, t_integration, h):
    num_steps = int(t_integration / h)
    U1_values = [U1(i * h) for i in range(num_steps + 1)]
    U2_values = [U2_0]

    for i in range(1, num_steps + 1):
        t = i * h


        U2_1 = U2_0 + h * dU2_dt(U1(t), U2_0, I_L1_0, I_L2_0, U_C1_0)


        U2_values.append(U2_1)


        U2_0 = U2_1

    return U1_values, U2_values


U1_values, U2_values = euler_method(U1, U2_0, I_L1_0, I_L2_0, U_C1_0, t_integration, h)


time_values = [i * h for i in range(len(U2_values))]
plt.plot(time_values, U1_values, label='Вхідна напруга U1')
plt.plot(time_values, U2_values, label='Вихідна напруга U2')
plt.xlabel('Час (сек)')
plt.ylabel('Напруга (В)')
plt.legend()
plt.show()
