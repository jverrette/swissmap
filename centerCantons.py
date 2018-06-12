from getlonglat import f as latlong
import numpy as np
import pandas as pd

df = pd.read_csv('languages.csv')

latlonger = []
for canton in df['Code'].values:
    latlonger.append(latlong(canton, 'Switzerland'))

latter=[]
longer=[]
for index in range(len(df)):
    latter.append(latlonger[index][0])
    longer.append(latlonger[index][1])


df['Longitude'] = longer
df['Latitude'] = latter
df =df.set_index('Code')
df=df[['Longitude', 'Latitude']]
df.to_csv('longitudelatitude.csv', index=True)

locations = pd.read_csv('longitudelatitude.csv', index_col=0)
