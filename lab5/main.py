import math
import matplotlib.pyplot as plt

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
t_integration = 0.2
h = 0.00001

U2_initial = 0
I_L2_initial = 0


def U1(t):
    return Umax * math.sin(2 * math.pi * f * t)


def system_eq(t, U2, I_L2):
    dU2_dt = (1 / (L2 * C1)) * (U1(t) - U2 - R2 * I_L2)
    dI_L2_dt = (1 / L2) * (U2 - R2 * I_L2)
    return dU2_dt, dI_L2_dt


def implicit_euler(U2, I_L2, t, h):
    dU2_dt, dI_L2_dt = system_eq(t, U2, I_L2)
    U2_new = U2 + h * dU2_dt
    I_L2_new = I_L2 + h * dI_L2_dt
    return U2_new, I_L2_new


time_values = [0]
U2_values = [U2_initial]

for t in range(int(t_integration / h)):
    U2, I_L2 = implicit_euler(U2_values[-1], I_L2_initial, time_values[-1], h)
    U2_values.append(U2)
    time_values.append(time_values[-1] + h)

plt.plot(time_values, U2_values)
plt.title('Перехідний процес вихідної напруги U2')
plt.xlabel('Час (с)')
plt.ylabel('U2 (В)')
plt.grid(True)
plt.show()
