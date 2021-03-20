import random
import matplotlib.pyplot as plt
import math

trials = [100, 1000, 5000, 10000]
x1, x2 = 0, 3
y1, y2 = 0, 5
for item in trials:
    hits = 0
    hit_x = list()
    hit_y = list()
    miss_x = list()
    miss_y = list()
    for i in range(item):
        x = random.uniform(x1, x2)
        y = random.uniform(y1, y2)

        if y <= x + 2:
            hits += 1
            hit_x.append(x)
            hit_y.append(y)

        else:
            miss_x.append(x)
            miss_y.append(y)

    area = (abs(x1 - x2) * abs(y1 - y2)) * (hits / item)

    print(f"Area for {item} trials is {area} ")

    plt.scatter(hit_x, hit_y, color="red", label="Hits")
    plt.scatter(miss_x, miss_y, color="green", label="Misses")
    plt.title(f" Iterations : {item}")
    plt.xlabel("X-Axis")
    plt.ylabel("y-Axis")
    plt.legend(loc="upper right")
    plt.show()


