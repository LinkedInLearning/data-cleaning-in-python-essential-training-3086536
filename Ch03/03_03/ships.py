# %%
import pandas as pd

df = pd.read_csv('ships.csv')
df

# %%
df[df.isnull().any(axis=1)]
# %%
df.iloc[-1]['name']
# %%
df['name'] = df['name'].str.strip()
df.iloc[-1]['name']

# %%
df[df.isnull().any(axis=1)]

# %%
import numpy as np
mask = df['name'].str.strip() == ''
df.loc[mask, 'name'] = np.nan
# %%

df[df.isnull().any(axis=1)]