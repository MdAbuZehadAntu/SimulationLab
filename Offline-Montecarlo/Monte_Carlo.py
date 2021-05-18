import random
import math
import matplotlib.pyplot as plt
l=[1000,5000,10000]
pi=[]
for item in l:
    hits=0
    hit_lx=[]
    hit_ly=[]
    miss_lx=[]
    miss_ly=[]
    for i in range(item):
        x=random.uniform(2,8)
        y=random.uniform(0,8)

        if math.sqrt(math.pow((5-x),2)+(5-y)**2)<=2:
            hits+=1
            hit_lx.append(x)
            hit_ly.append(y)
        else:
            miss_lx.append(x)
            miss_ly.append(y)
    g=(56/(1.5**2))*(hits/item)
    a=(hits/item)*56
    pi.append(g)
    print(f"Value of PI is {g:>5.4f} for n= {item}")
    print(f"Area of the circle is {a} for n={item}")
    plt.scatter(hit_lx,hit_ly,color="red",label="hits")
    plt.scatter(miss_lx,miss_ly,color="green",label="misses")
    plt.legend(loc="upper right")
    plt.show()
# print(pi)
plt.bar(l,pi,width=600,color="orange")
plt.plot(l,[math.pi for i in l],color="black")

plt.xlabel("Iterations")
plt.ylabel("Values of PI")
plt.show()