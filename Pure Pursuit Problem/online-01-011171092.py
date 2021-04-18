ax = [-10]
bx = [0]
cx = [-10]
dx = [0]

ay = [0]
by = [-10]
cy = [-10]
dy = [0]

va = 3
vb = 5
vc = 7
vd = 4

a = 0
b = 0
c = 0
d = 0

import math
w=0
print(f"Ar Time {0} A({ax[0]},{ay[0]}) , B({bx[0]},{by[0]}) , C({cx[0]},{cy[0]}), D({dx[0]},{dy[0]})")
for i in range(1, 11):
    w+=1


    dist_ca = math.sqrt(((cx[i - 1] - ax[i - 1]) ** 2) + ((cy[i - 1] - ay[i - 1]) ** 2))

    dist_dc = math.sqrt(((dx[i - 1] - cx[i - 1]) ** 2) + ((dy[i - 1] - cy[i - 1]) ** 2))
    dist_bd = math.sqrt(((bx[i - 1] - dx[i - 1]) ** 2) + ((by[i - 1] - dy[i - 1]) ** 2))
    dist_ab = math.sqrt(((ax[i - 1] - bx[i - 1]) ** 2) + ((ay[i - 1] - by[i - 1]) ** 2))

    sin = (ay[i - 1] - cy[i - 1]) / dist_ca
    cos = (ax[i - 1] - cx[i - 1]) / dist_ca

    cx.append(cx[i - 1] + vc * cos)
    cy.append(cy[i - 1] + vc * sin)

    sin = (cy[i - 1] - dy[i - 1]) / dist_dc
    cos = (cx[i - 1] - dx[i - 1]) / dist_dc

    dx.append(dx[i - 1] + vd * cos)
    dy.append(dy[i - 1] + vd * sin)

    sin = (dy[i - 1] - by[i - 1]) / dist_bd
    cos = (dx[i - 1] - bx[i - 1]) / dist_bd

    bx.append(bx[i - 1] + vb * cos)
    by.append(by[i - 1] + vb * sin)

    sin = (by[i - 1] - ay[i - 1]) / dist_ab
    cos = (bx[i - 1] - ax[i - 1]) / dist_ab

    ax.append(ax[i - 1] + va * cos)
    ay.append(ay[i - 1] + va * sin)

    print(f"At Time {i} A({ax[i]},{ay[i]}) , B({bx[i]},{by[i]}) , C({cx[i]},{cy[i]}), D({dx[i]},{dy[i]})")

    if dist_ca < 4.5:
        print(f"C shoots at A at {i} time with distance {dist_ca}")
        a += 1
    if dist_dc < 4.5:
        print(f"D shoots at C at {i} time with distance {dist_dc}")
        c += 1
    if dist_bd < 4.5:
        print(f"B shoots at D at {i} time with distance {dist_bd}")
        d += 1
    if dist_ab < 4.5:
        print(f"A shoots at B at {i} time with distance {dist_ab}")
        b += 1



import matplotlib.pyplot as plt

plt.plot(ax, ay, color="red")
plt.plot(bx, by, color="blue")
plt.plot(cx, cy, color="green")
plt.plot(dx, dy, color="black")

plt.show()

print(f"A got shot {a} times")
print(f"B got shot {b} times")
print(f"C got shot {c} times")
print(f"D got shot {d} times")
