# %%
import pandas as pd

df = pd.read_csv('heights.csv')
df

# %%
max_heights = pd.DataFrame([
[1, 32],
], columns=['grade', 'max_height'])
max_heights

# %%
mdf = pd.merge(df, max_heights, how='left')
mdf

# %%
df[mdf['height'] > mdf['max_height']]