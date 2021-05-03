import random
import math
import matplotlib.pyplot as plt
trials = [100,1000,5000,10000] #changes may be needed
x1,x2=0,8 #changes may be needed
integral = list()
error = list()
print(f"{'Trial':<15}{'Integral Value':<25}{'Error':<10}")
for n in trials:
    fx = list()
    fxx = list()
    for i in range(n):
        x = random.uniform(min(x1,x2),max(x1,x2))
        if x<=4:

            f = math.sqrt(4*x) #change according to the given function
            fx.append(f)
            fxx.append(f**2)
        else:
            f = 8-x  # change according to the given function
            fx.append(f)
            fxx.append(f ** 2)

    avg_fx = sum(fx)/len(fx)
    avg_fxx = sum(fxx)/len(fxx)
    integral_value = avg_fx*abs(x1-x2)
    error_value = (abs(x1-x2)/math.sqrt(n))*math.sqrt(avg_fxx-avg_fx**2)
    error.append(error_value)


    print(f"{n:<18}{integral_value:<22.3f}{error_value:.3f}")

plt.xlabel("Errors")
plt.ylabel("n")
plt.plot(trials,error,color="blue") #change may be needed
plt.title("Plotting Trial vs Error graph")
plt.show()

trials=[str(item) for item in trials]
plt.bar(trials,error,color="red")
plt.title("Bar chart of Trial vs Error")
plt.xlabel("No. of trials")
plt.ylabel("Value of Error")
plt.show()
