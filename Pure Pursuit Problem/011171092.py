import math
from matplotlib import animation


class Car:

    def __init__(self, s, x, y, defender=None):
        self.shot = 0
        self.s = s
        self.x = []
        self.x.append(x)
        self.y = []
        self.y.append(y)
        self.defender = defender

    def dist(self, x_t, x_d, y_t, y_d, i):
        return math.sqrt(((x_t[i - 1] - x_d[i - 1]) ** 2) + ((y_t[i - 1] - y_d[i - 1]) ** 2))

    def sin(self, y_t, y_d, i, dist):
        return (y_t[i - 1] - y_d[i - 1]) / dist

    def cos(self, x_t, x_d, i, dist):
        return (x_t[i - 1] - x_d[i - 1]) / dist

    def x_new(self, x_d, s, cos, i):
        return x_d[i - 1] + s * cos

    def y_new(self, y_d, s, sin, i):
        return y_d[i - 1] + s * sin

    def _shot(self):
        self.shot += 1


A = Car(3, -10, 0, C)
D = Car(2, 0, 0, A)
B = Car(5, -10, 10, A)
C = Car(7, 10, 10, B)

ax = []
ay = []
bx = []
by = []
cx = []
cy = []
dx = []
dy = []

print(f'{"Defender":<15} {"Target":<15} {"Time":<15}{"Distance":}')

for i in range(1, 21):
    dist_BC = C.dist(C.x, B.x, C.y, B.y, i)
    dist_DB = B.dist(B.x, D.x, B.y, D.y, i)
    dist_AD = D.dist(D.x, A.x, D.y, A.y, i)

    if dist_BC < 5:
        C._shot()
        print(f"{'B':<15} {'C':<15} {i:<15}{dist_BC:.3f}")

    if dist_DB < 5:
        B._shot()
        print(f"{'D':<15} {'B':<15} {i:<15}{dist_DB:.3f}")

    if dist_AD < 5:
        D._shot()
        print(f"{'A':<15} {'D':<15} {i:<15}{dist_AD:.3f}")

    SIN = C.sin(C.y, B.y, i, dist_BC)
    COS = C.cos(C.x, B.x, i, dist_BC)

    B.x.append(B.x_new(B.x, B.s, COS, i))

    B.y.append(B.y_new(B.y, B.s, SIN, i))

    SIN = B.sin(B.y, D.y, i, dist_DB)
    COS = B.cos(B.x, D.x, i, dist_DB)

    D.x.append(D.x_new(D.x, D.s, COS, i))

    D.y.append(D.y_new(D.y, D.s, SIN, i))

    SIN = D.sin(D.y, A.y, i, dist_AD)
    COS = D.cos(D.x, A.x, i, dist_AD)

    A.x.append(A.x_new(A.x, A.s, COS, i))

    A.y.append(A.y_new(A.y, A.s, SIN, i))

    C.x.append(C.x[0])

    C.y.append(C.y[i - 1] + C.s)

import matplotlib.pyplot as plt

j = 0

print(f"A got shot {A.shot} times")
print(f"B got shot {B.shot} times")
print(f"C got shot {C.shot} times")
print(f"D got shot {D.shot} times")


def draw_graph(i):
    global j

    if j < 21:
        ax.append(A.x[j])
        ay.append(A.y[j])
        bx.append(B.x[j])
        by.append(B.y[j])
        cx.append(C.x[j])
        cy.append(C.y[j])
        dx.append(D.x[j])
        dy.append(D.y[j])
        j += 1
        plt.cla()
        plt.plot(ax, ay, color="red", label='Car A')
        plt.plot(bx, by, color="blue", label='Car B')
        plt.plot(cx, cy, color="green", label='Car C')
        plt.plot(dx, dy, color="orange", label='Car D')

        plt.legend()


anima = animation.FuncAnimation(plt.gcf(), draw_graph, interval=500)
plt.tight_layout()
plt.show()
