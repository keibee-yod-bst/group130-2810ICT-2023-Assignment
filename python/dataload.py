import pandas as pd

df = pd.read_csv("victoriaaccidents.csv")

objectid = df['OBJECTID']
date = df['ACCIDENT_DATE']
temp = df['Temperature']

