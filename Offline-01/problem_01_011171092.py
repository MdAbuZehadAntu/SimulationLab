# -*- coding: utf-8 -*-
"""problem-01-01111092.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_cVjm6amTY_EllMbNYEuN4Zrb8maSIol
"""

str1=input("Enter the string input : ");

str1=list(str1)

for i in range(1,len(str1)):
  if str1[i]==str1[0]:
    str1[i]="$"
  
str1="".join(str1)
print("Output: ",str1)