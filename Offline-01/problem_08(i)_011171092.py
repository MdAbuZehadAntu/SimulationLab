# -*- coding: utf-8 -*-
"""problem-08(i)-011171092.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_cVjm6amTY_EllMbNYEuN4Zrb8maSIol
"""

import pandas as pd
import matplotlib.pyplot as plt


data={
    "Month No.":[1,2,3,4,5,6],
    "Toothpaste":[2500,2630,2140,3400,3600,2760],
    "Facewash":[1500,1200,1340,1130,1740,1555],
    "Shampoo":[5200,5100,4550,5870,4560,4890],
    "Moisturizer":[9200,6100,9550,8870,7760,7490],
    "Soap":[1200,2100,3550,1870,1560,1890]
  }

plt.xlabel("Month no:")
plt.ylabel("Sales unit")
plt.plot(data["Month No."],data["Toothpaste"],color="blue")
plt.plot(data["Month No."],data["Facewash"],color="orange")
plt.plot(data["Month No."],data["Shampoo"],color="green")
plt.plot(data["Month No."],data["Moisturizer"],color="red")
plt.plot(data["Month No."],data["Soap"],color="purple")
plt.legend(["Toothpaste","Facewash","Shampoo","Moisturizer","Soap"],loc="upper right")
plt.show()