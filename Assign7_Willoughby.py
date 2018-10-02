# This program demonstrates the basics of Python's numpy and pandas library.

import numpy as np
import pandas as pd

column_names = ['ID','Age','Height','Weight','Year']

path = 'Athlete.csv'
df = pd.read_csv(path)
a1=df[:5]
a1
print("1. Display the first 5 rows (including headers) of the data.")
print()
print(a1)
print()

arr=np.array([[1,24,180,80,1992],[2,23,170,60,2012],[5,21,185,82,1988],
              [5,21,185,82,1988],[5,25,185,82,1992],[5,25,185,82,1992],
              [5,27,185,82,1994],[5,27,185,82,1994],[6,31,188,75,1992],
              [6,31,188,75,1992],[6,31,188,75,1992],[6,31,188,75,1992],
              [6,33,188,75,1994],[6,33,188,75,1994],[6,33,188,75,1994],
              [6,33,188,75,1994],[7,31,183,72,1992],[7,31,183,72,1992],
              [7,31,183,72,1992],[7,31,183,72,1992],[7,33,183,72,1994],
              [7,33,183,72,1994],[7,33,183,72,1994],[7,33,183,72,1994],
              [9,26,186,96,2002],[11,22,182,76.5,1980],[12,31,172,70,2000]])
df2 = pd.DataFrame(arr, columns=column_names)
df2.shape
print("2. Create a NumPy array for the data. Show how many rows and columns there are in the data.")
print()
df2 = pd.DataFrame(arr, columns=column_names)
print(df2)
print()
print('Row:Columns=',df2.shape)
print()

arr[0,0]=1993
a2=arr[:,:1]

print("3. Overwrite the Year value of the 2nd row (that is, the athlete whose ID is 1) with 1993. Display only the Year column to check if the value has been successfully changed.")
print()
print('    ID')
print(a2)
print()

a3=df2['Weight']-10

print("4. Deduct 10 from all athletes’ weights and show results.")
print()
print('    Weight')
print(a3)
print()

df3 = df2.assign(Ratio = df.Weight / df.Height)

print("5. Add a new column to the array to show the ratio of weight to height of each athlete.")
print()
print(df3)
