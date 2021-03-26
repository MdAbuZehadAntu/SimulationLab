import random
import math
import matplotlib.pyplot as plt
fx_list=[]
f2x_list=[]

for i in range(5000):
    x=random.uniform(0,4)

    if x<=2:
        fx=x
        fx_list.append(fx)
        f2x_list.append(fx**2)
    else:
        fx=4-x
        fx_list.append(fx)
        f2x_list.append(fx**2)

avg_fx=sum(fx_list)/len(fx_list)
avg_f2x=sum(f2x_list)/len(f2x_list)

print(f"Integral = : {avg_fx*4}")
print(f"Error = : {(4/math.sqrt(5000))*math.sqrt(avg_f2x-avg_fx**2)}")

