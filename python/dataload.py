import pandas as pd

df = pd.read_csv("victoriaaccidents.csv")

accidentid = df['OBJECTID']
accidentdate = df['ACCIDENT_DATE']
accidenttime = df['ACCIDENT_TIME']
accidentday = df['DAY_OF_WEEK']
accidentalcohol = df['ALCOHOLTIME']
