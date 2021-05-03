import math
import random
import matplotlib.pyplot as plt

trials=[100,1000,5000,10000]
error=list()
x1,x2=0,2
for trial in trials:
    fx_list=list()
    f2x_list=list()
    for i in range(trial):
        x=random.uniform(min(x2,x1),max(x2,x1))
        fx=x**2*math.exp(x)*math.log(x)
        fx_list.append(fx)
        f2x_list.append(fx**2)
    avg_fx=sum(fx_list)/len(fx_list)
    # print(avg_fx)
    avg_f2x=sum(f2x_list)/len(f2x_list)
    # print(avg_f2x)
    # quit()
    integral_val=avg_fx*abs(x2-x1)
    err= (abs(x2-x1)/math.sqrt(trial))*math.sqrt(avg_f2x-avg_fx**2)

    print(f"For {trial} iterations : ")
    print()
    print(f"{'Integral Value':<30}{'Error'}")
    print(f"{integral_val:<30}{err}")
    print()
    print()
    error.append(err)

trials=[str(item) for item in trials]

plt.plot(trials,error,color="red")
plt.title("Plotting of Trial vs Error")
plt.xlabel("No. of trials")
plt.ylabel("Value of Error")
plt.show()

plt.bar(trials,error,color="red")
plt.title("Bar chart of Trial vs Error")
plt.xlabel("No. of trials")
plt.ylabel("Value of Error")
plt.show()

