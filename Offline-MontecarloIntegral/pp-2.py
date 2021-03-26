import math
import random
import matplotlib.pyplot as plt

for it in [100,1000,5000,10000]:
    f1=0
    f2=0
    for i in range(int(it/2)):
        x=random.uniform(0,4)
        t=math.sqrt(4*x)
        f1+=t
        f2+=t**2
    intg1=(f1/(it/2)*4)
    p1 = (4 / math.sqrt(int(it/2))) * math.sqrt(f2 / int(it/2) - (f1 / int(it/2)) ** 2)
    f1 = 0
    f2 = 0
    for i in range(int(it/2)):
        x=random.uniform(4,8)
        t=8-x
        f1+=t
        f2+=t**2

    intg2 = (f1 / int(it / 2) * 4)
    p2 = (4 / math.sqrt(int(it / 2))) * math.sqrt(f2 / int(it / 2) - (f1 / int(it / 2)) ** 2)

    intg=intg2+intg1
    p=p1+p2

    print(
        f"For {it} iteration : integral val = {intg} and error = {p}")
