from cmath import nan
import csv
from dataclasses import replace
from math import prod
from re import L 
import numpy as np
from sqlalchemy import column, false
import statsmodels.formula.api as smf
import statsmodels.api as sm
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from fpdf import FPDF

incorrect = pd.read_csv("/Users/matthewzhang/Desktop/Data/DB_LCE.csv")
correct = pd.read_csv("/Users/matthewzhang/Desktop/Data/Sheets_data.csv")

#Identification of placements 

correctID = correct['Electrolyte ID']
incorrectID = incorrect['Electrolyte ID']
placements = []


i = -1 
if len(correctID) > len(incorrectID):
    for item in incorrectID:
        i = -1 
        for litem in correctID:
            i += 1 
            if item == litem:
                placements.append(i)
if len(correctID) < len(incorrectID):
    for item in correctID:
        i = -1 
        for litem in incorrectID:
            i += 1 
            if item == litem:
                placements.append(i)   

#Idendification of columns

incorrectCols = [] 
correctCols = []
for col in incorrect:
    if str(col) != "Electrolyte ID":
        incorrectCols.append(col)
for col in correct:
    if str(col) != "Electrolyte ID":
        correctCols.append(col)

same = []
for item in incorrectCols:
   if item in correctCols:
       same.append(item)

print(len(correctID))
print(len(placements))

def checkColumn(inco, co):
    # columnIncorrect = incorrect[inco]
    # columnCorrect = correct[co]
    columnCorrect = incorrect[inco]
    columnIncorrect = correct[co]
    incorrectList = []
    for x in range(len(columnIncorrect)):
        if str(columnCorrect[placements[x]]) == str(columnIncorrect[x]):
            continue
        try:
            t = columnIncorrect[x]
            g = columnCorrect[placements[x]] 
            np.double(columnIncorrect[x])
            np.double(columnCorrect[placements[x]])
            if float(columnCorrect[placements[x]]) == float(columnIncorrect[x]):
                continue 
            if (abs(np.double(t) - np.double(g))) < (0.05 * np.double(t)):
                continue
        except Exception:
            list = [] 
        #EX: Electrolyte ID 21-7-100 Voltage: Sheets 4V/DB 3V
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if any(letter in str(columnIncorrect[x]) for letter in letters) == False or any(letter in str(columnCorrect[placements[x]]) for letter in letters) == False:
            incorrectList.append(str(correctID[placements[x]]) + " " + str(inco) + ": " + "Should be: " + 
            str(columnIncorrect[placements[x]]) + " But is: " + str(columnCorrect[x]))
    return incorrectList

def putToPDF(name, other):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    list = checkColumn(name, name)
    for item in list:
        pdf.cell(200, 10, txt = item,ln = 1, align = 'C')
    pdf.output(other)  

def putAllPDF():
    for item in same:
        putToPDF(item, item)

putAllPDF() 
            
        