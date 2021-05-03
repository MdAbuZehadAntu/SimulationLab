import math
import matplotlib.pyplot as plt
import random

trials = [100, 1000, 5000, 10000]  # changes may be needed

X, Y = 0, 0  # changes
radius = 3  # changes
x1, x2 = -5, 5  # changes
y1, y2 = -5, 5  # changes
PI_list = list()
circle_area_list = list()
print(f"{'Trials':<17}{'PI Value':<25}{'Area':}")
for n in trials:
    hit = 0
    hit_x = list()
    hit_y = list()
    miss_x = list()
    miss_y = list()
    for i in range(n):
        x = random.uniform(x1, x2)
        y = random.uniform(y1, y2)

        if math.sqrt((X - x) ** 2 + (Y - y) ** 2) <= radius:  # changes
            hit += 1
            hit_x.append(x)
            hit_y.append(y)
        else:
            miss_x.append(x)
            miss_y.append(y)
    PI = (((abs(x1 - x2) * abs(y1 - y2)) / radius ** 2) * (hit / n))
    PI_list.append(PI)
    area = PI * radius ** 2
    circle_area_list.append(area)
    print(f"{n:<18}{PI:<22.3f}{area:.3f}")

    plt.scatter(hit_x, hit_y, color='red', label="Hits")
    plt.scatter(miss_x, miss_y, color="green", label="Misses")
    plt.legend(loc="upper right")
    plt.show()

trials=[str(item) for item in trials]
plt.bar(trials,PI_list,color="red")
plt.show()
plt.bar(trials,circle_area_list,color="red")
plt.show()
