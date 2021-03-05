# -*- coding: utf-8 -*-
"""problem-08(iii)-011171092.ipynb

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

df=pd.DataFrame(data).to_numpy()[:,1:]
sales=list()
for i in range(df.shape[0]):
  sales.append(sum(df[i]))



plt.bar(data["Month No."],sales,color="maroon")

plt.xlabel("Month no.")
plt.ylabel("Total Sales")
plt.show()