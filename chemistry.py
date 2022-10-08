from cmath import nan
import csv
from dataclasses import replace
from math import prod
from re import L
from turtle import xcor 
import numpy as np
from sqlalchemy import column
import statsmodels.formula.api as smf
import statsmodels.api as sm
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from fpdf import FPDF
import random 

xColumn = np.array([0.5, 1, 1.5, 2.0])
yColumn = np.array([28.3, 27.6, 26.8, 26]) 
# yColumn = [] 
# xColumn = [] 



# for item in yColumn1:
#     yColumn.append(float(item)) 

# for item in xColumn1:
#     xColumn.append(float(item))

a, b = np.polyfit(xColumn, yColumn, 1)
plt.scatter(xColumn, yColumn)
plt.xlabel('Time(min)')
plt.ylabel('Temperature(C)')
plt.plot(xColumn, float(a)*xColumn+b)
print(str(float(a)*0 + b))
plt.show()