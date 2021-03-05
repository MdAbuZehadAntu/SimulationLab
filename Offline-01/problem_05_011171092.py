# -*- coding: utf-8 -*-
"""problem-05-011171092.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_cVjm6amTY_EllMbNYEuN4Zrb8maSIol
"""

import math
while(True):
  try:
    a,b,c=map(float,input("Enter the three sides length of the triangle : ").split())
    if a+b>=c and a+c>=b and b+c>=a:
      break;
    else:
      print("Invalid length input!!!")
  except Exception as e:
    print(e)

def area_triangle(a,b,c):
  p=(a+b+c)/2
  return math.sqrt(p*(p-a)*(p-b)*(p-c))

print(f"Area of the triangle : {area_triangle(a,b,c):.3f}")