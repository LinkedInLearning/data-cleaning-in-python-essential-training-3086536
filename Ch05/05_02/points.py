# %%
import pandas as pd

df = pd.read_csv('points.csv')
df.dtypes

# %%
def asint(val):
    return int(val, base=0)

df['color'] = df['color'].apply(asint)
df.dtypes

# %%
bools = {
    'yes': True,
    'no': False,
}
df['visible'] = df['visible'].map(bools)
df.dtypes

# %%
df