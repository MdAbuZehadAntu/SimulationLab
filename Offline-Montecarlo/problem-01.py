import random
import math
import matplotlib.pyplot as plt

trials = [100, 1000, 5000, 10000]

a, b = (-5), 5
c, d = (-5), 5
cx, cy = 0, 0
radius = 3
pi_val = list()
for item in trials:
    hits = 0
    hit_list_x = list()
    hit_list_y = list()
    miss_list_x = list()
    miss_list_y = list()

    area_list = list()
    for i in range(item):
        x = random.uniform(a, b)
        y = random.uniform(c, d)

        if math.sqrt((cx - x) ** 2 + (cy - y) ** 2) <= radius:
            hits += 1
            hit_list_x.append(x)
            hit_list_y.append(y)
        else:
            miss_list_x.append(x)
            miss_list_y.append(y)

    PI = ((abs(a - b) * abs(c - d)) / radius ** 2) * (hits / item)
    pi_val.append(PI)
    area = ((abs(a - b) * abs(c - d)) * (hits / item))
    area_list.append(area)
    print(f"For {item} trials : ")
    print()
    print(f'{"PI":<20} Area')
    print(f"{PI:<20.4f}{area:.4f}")
    print()
    print()

    plt.scatter(hit_list_x, hit_list_y, color="red")
    plt.scatter(miss_list_x, miss_list_y, color="green")
    plt.title(f" Iterations : {item}")
    plt.xlabel("X-Axis")
    plt.ylabel("y-Axis")
    plt.show()

plt.bar(trials, pi_val, color="red", width=300)
plt.plot(trials, [math.pi for i in trials], color="blue")
plt.xlabel("No. of Trials")
plt.ylabel("PI Values")
plt.show()
