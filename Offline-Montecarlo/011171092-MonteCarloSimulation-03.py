import math
import matplotlib.pyplot as plt
import random

trials = [100, 1000, 5000, 10000]  # changes may be needed

x1, x2 = 0, 8  # changes
y1, y2 = 0, 4  # changes

print(f"{'Trials':<17}{'Area':}")
for n in trials:
    hit = 0
    hit_x = list()
    hit_y = list()
    miss_x = list()
    miss_y = list()
    for i in range(n):
        x = random.uniform(x1, x2)
        y = random.uniform(y1, y2)

        if x <= 4:

            if y ** 2 <= 4 * x:  # changes
                hit += 1
                hit_x.append(x)
                hit_y.append(y)
            else:
                miss_x.append(x)
                miss_y.append(y)
        else:
            if y <= 8 - x:  # changes
                hit += 1
                hit_x.append(x)
                hit_y.append(y)
            else:
                miss_x.append(x)
                miss_y.append(y)

    area = (abs(x1 - x2) * abs(y1 - y2)) * (hit / n)
    print(f"{n:<13}{area:.3f} unit sq.")

    plt.scatter(hit_x, hit_y, color='red', label="Hits")
    plt.scatter(miss_x, miss_y, color="green", label="Misses")
    plt.legend(loc="upper right")
    plt.show()
