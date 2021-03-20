import random
import math
import matplotlib.pyplot as plt

n = [100, 1000, 5000, 10000]
x1, x2 = 0, 8
y1, y2 = 0, 4
for item in n:
    hits = 0
    hit_x = list()
    hit_y = list()
    miss_x = list()
    miss_y = list()
    for i in range(item):
        x = random.uniform(x1, x2)
        y = random.uniform(y1, y2)

        if x <= 4:
            if y ** 2 <= 4 * x:
                hits += 1
                hit_x.append(x)
                hit_y.append(y)
            else:
                miss_y.append(y)
                miss_x.append(x)

        else:
            if y <= 8 - x:
                hits += 1
                hit_x.append(x)
                hit_y.append(y)
            else:
                miss_y.append(y)
                miss_x.append(x)

    area = (abs(x1 - x2) * abs(y1 - y2)) * (hits / item)

    print(f"Area for {item} trials is {area} ")

    plt.scatter(hit_x, hit_y, color="red", label="Hits")
    plt.scatter(miss_x, miss_y, color="green", label="Misses")
    plt.title(f" Iterations : {item}")
    plt.xlabel("X-Axis")
    plt.ylabel("y-Axis")
    plt.legend(loc="upper right")
    plt.show()
