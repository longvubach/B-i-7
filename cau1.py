import numpy as np
import pandas as pd
from randomint import ngaunhien as rn
array1 = np.array(rn(35,1,9))
serries1 = pd.Series(array1)
print("5 số đầu:")
print(serries1.head())
print("5 số cuối:")
print(serries1.tail())
print("Các phần tử của Serries:")
print(serries1.values)
print("Thông tin thống kê chung:")
print(serries1.describe())
print("Tổng các giá trị trong serries:")
print(serries1.sum())
print("Phần tử xuất hiện nhiều nhất:")
print(serries1.mode())