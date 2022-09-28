import pandas as pd
import numpy as np
from randomfloat import ngaunhien as rn
b1 = pd.read_csv('Book1.csv')
df1 = pd.DataFrame(b1)
df1['TBTK'] = round((df1['TK1']+df1['TK2']+df1['TK3'])/3,1)
df1['GK'] = pd.Series(np.array(rn(20,1.0,10.0)))
df1['CK'] = pd.Series(np.array(rn(20,1.0,10.0)))
df1['Trung bình'] = round(df1['TBTK']*0.2 + df1['GK']*0.3 + df1['CK']*0.5,1)
df1.to_csv('Book2.csv', index = False)
print(df1.head())
print(df1)
dau = df1.loc[(df1['CK']>=3) & (df1['Trung bình']>=4)]
dau.to_csv('dau.csv', index = False)
rot = df1.loc[(df1['CK']<3) | (df1['Trung bình']<3)]
rot.to_csv('rot.csv', index = False)
a = dau['Trung bình'].max()
print(dau.loc[dau['Trung bình'] == a])