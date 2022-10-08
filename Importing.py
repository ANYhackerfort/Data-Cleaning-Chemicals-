from cmath import nan
import csv
from dataclasses import replace
from math import prod
from re import L 
import numpy as np
from sqlalchemy import column
import statsmodels.formula.api as smf
import statsmodels.api as sm
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from fpdf import FPDF


productionMaterialsML = pd.read_csv("/Users/matthewzhang/Desktop/Data/ml_production_materials.csv")
correctVersion = pd.read_csv("/Users/matthewzhang/Desktop/Data/FMT_post_200.csv")
manualMaterials = pd.read_csv("/Users/matthewzhang/Desktop/Data/jager.csv")

correctEletroID = correctVersion['Electrolyte ID']
mlEletroID = productionMaterialsML['electrolyte_id']
placementML = []

i = -1 
for item in mlEletroID:
    i = -1 
    for litem in correctEletroID:
        i += 1 
        if item == litem:
            placementML.append(i)
            break 

def replaceCorrectMl(incorrect, correct): 
    replacementGenerationMethod = []
    bob = []
    mlGenerationMethod = productionMaterialsML[incorrect]
    correctGenerationMethod = correctVersion[correct]
    # replaceCorrectMl.getTest = bob 
    i = -1 
    for item in mlGenerationMethod:
        jitem = str(item)
        i += 1 
        if str(correctGenerationMethod[int(placementML[i])]) == str(nan):
            bob.append(item)
            continue 
        if jitem == str(correctGenerationMethod[int(placementML[i])]):
            bob.append(item)
            continue
        if jitem != str(correctGenerationMethod[placementML[i]]):
            bob.append(str(correctGenerationMethod[int(placementML[i])]))
            continue
    return bob

correctColumn = []
mlColumn = []
sameColumn = []
sameColumnCorrect = []
for row in correctVersion:
    correctColumn.append(row)
for row in productionMaterialsML:
    mlColumn.append(row)

for item in mlColumn:
    for jitem in correctColumn:
        cleanedItem = str(item).capitalize()
        cleanedItem = str(cleanedItem.replace("_", " "))
        if cleanedItem == str(jitem).capitalize():
            sameColumn.append(item)
            sameColumnCorrect.append(jitem)

unchecked = mlColumn

for jitem in sameColumn:
    unchecked.remove(jitem) 

print(unchecked)
print("========")
def writeColumn(name, row):
    productionMaterialsML[name] = row
    productionMaterialsML.to_csv(r"/Users/matthewzhang/Desktop/Mallory - Stat/emptyCSV.csv")

# print(replaceCorrectMl('LiPF6', 'LiPF6'))
# print(str(len(productionMaterialsML['LiPF6'])))
# # print(str(len(replaceCorrectMl('LiPF6', 'LiPF6'))))
def sameColumnReplace():
    for x in range(len(sameColumn)):
        print(sameColumn[x])
        writeColumn(str(sameColumn[x]), replaceCorrectMl(sameColumn[x], sameColumnCorrect[x]))

def uncheckedcolumnReplace(incorrect, correct):
    print(incorrect)
    writeColumn(str(incorrect), replaceCorrectMl(incorrect, correct))
sameColumnReplace()
uncheckedcolumnReplace('total_mass(g)', 'total mass / g')




