import random
import math
hits=0
n=5000
for i in range(n):
    x = random.uniform(1, 8)
    y = random.uniform(1, 9)

    if math.sqrt(math.pow((3 - x), 2) + (5 - y) ** 2) <= 1.5:
        hits+=1



print(hits)
g = 56/(1.5**2)*(hits/n)
a=56*(hits/n)
# a=(hits/item)*48
# pi.append(g)
print(f"Value of PI is {g:>5.4f}")
print(f"Area is {a:>5.4f}")