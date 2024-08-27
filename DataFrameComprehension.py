'''
1.	Conditional Column Creation:
	•	Create a new column in a DataFrame based on conditions applied to existing columns.
	•	Example: For a DataFrame with columns ['A', 'B'], create a new column C that contains
	'High' if A > B, 'Low' otherwise.
'''
import numpy as np
import pandas as pd
data = {'A': [10, 20, 30, 40],
        'B': [15, 25, 5, 35]}
df=pd.DataFrame(data)
print(df)
df['C']=np.where(df['A']>df['B'],'Low', 'High')