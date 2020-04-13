import pandas as pd
import numpy as np
s = pd.Series([1.0, 3.0, 5.0, 7.0, 9.0])
print(s)
print(s.shape)

df_a = pd.DataFrame(s)
#dataframe은 열 X 행의 형태로 데이터를 저장 
print('dataframe:')
print(df_a)
print(df_a.shape)
