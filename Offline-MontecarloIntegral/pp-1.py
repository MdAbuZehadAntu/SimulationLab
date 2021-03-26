import numpy as np
import math
import matplotlib.pyplot as plt

el = []

for it in [100, 1000, 5000, 10000]:
    f1 = 0
    f2 = 0

    for i in range(it):
        x = np.random.uniform(0, 2)
        t=x ** 2 * math.exp(x) * math.log(x)
        f1 += t
        f2 += t ** 2
    
    p=(2 / math.sqrt(it)) * math.sqrt(f2 / it - (f1 / it) ** 2)
    el.append(p)
    print(
        f"For {it} iteration : integral val = {(f1 / it) * 2} and error = {p}")

plt.plot([100, 1000, 5000, 10000], el)
plt.show()
