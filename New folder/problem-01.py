import random
import math
import matplotlib.pyplot as plt

trials=[100,1000,5000,10000]
x1,x2=0,2
error=[]
for trial in trials:
    fx_list=list()
    f2x_list=list()

    for i in range(trial):
        x=random.uniform(min(x1,x2),max(x1,x2))
        fx=x**2*math.exp(x)*math.log(x)
        fx_list.append(fx)
        f2x_list.append(fx**2)

    avg_fx=sum(fx_list)/len(fx_list)
    avg_f2x=sum(f2x_list)/len(f2x_list)
    err = (abs(x2 - x1) / math.sqrt(trial) * math.sqrt(avg_f2x - avg_fx ** 2))
    error.append(err)
    print(f"For {trial} iterations : ")
    print()

    print(f"{'Integral Value':<30}{'Error':}")
    print(f"{avg_fx*abs(x2-x1):<30}{err}")
    print()
    print()

trials=[str(item) for item in trials]

plt.bar(trials,error,color='red')
plt.title("Bar Chart of Trail vs Error ")
plt.xlabel("No. of trials")
plt.ylabel("Calculated error")
plt.show()

plt.plot(trials,error,color='red')
plt.title("Plotting of Trail vs Error ")
plt.xlabel("No. of trials")
plt.ylabel("Calculated error")
plt.show()

