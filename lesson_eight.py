import numpy as np
import pandas as pd

np.random.seed(42)  # Установить зерно функции random библиотеки numpy
np_array = np.random.randint(low=-15, high=20, size=4)

print('type(np_array)', type(np_array))

print(pd.Series(np_array))

date_range = pd.date_range('20190101', periods=10)
pd_series = pd.Series(np.random.rand(10), date_range)
print(pd_series)

print(date_range)
print(type(date_range))



pd_series_2 = pd.Series(np_array, index=['1st day', '2nd day', '3rd day', '4th day'])
print(pd_series_2)
date_range = pd.date_range('20190101', periods=40)
print(date_range)
