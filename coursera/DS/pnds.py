import pandas as pd
import math

df = pd.DataFrame({'num': range(2), 'chars':['a']*2})

print(df.shape)
df['isS'] = [False, True]
df['isS'] = False, True
df['isS'] = (False, True)
# df['isS'] = False True
print(df)
print('*' * 50)
print(int.__doc__)