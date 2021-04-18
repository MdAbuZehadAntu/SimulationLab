x_t = [100, 110, 120, 129, 140, 149, 158, 168, 179, 188,198 ,209, 219, 226, 234, 240]

y_t = [0, 3, 6, 10, 15, 20, 26, 32, 37, 34,30,27,23,19 ,16 ,14]
x_d = [0]
y_d = [60]

s = 20

import math
import numpy as np

for i in range(1, 13):
    try:
        dist = math.sqrt(((x_t[i - 1] - x_d[i - 1]) ** 2) + ((y_t[i - 1] - y_d[i - 1])** 2))
    except:
        print(i)
        print(x_t[i])
        quit()
    if dist<10:
        print(f"Destroyed at {i} min with distance {dist}")
        break
    sin = (y_t[i-1]-y_d[i-1])/dist
    cos = (x_t[i-1]-x_d[i-1])/dist
    x_d.append(x_d[i-1]+s*cos)
    y_d.append(y_d[i-1]+s*sin)

print(x_b)
