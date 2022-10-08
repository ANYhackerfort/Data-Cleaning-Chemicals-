import csv 
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.api as sm
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("/Users/matthewzhang/Downloads/DB_FMT_correction/ml_production_materials.csv")
print(df.head(3))