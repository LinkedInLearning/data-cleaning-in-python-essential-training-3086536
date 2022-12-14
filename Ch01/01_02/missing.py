# %%
import pandas as pd

# %%
df = pd.read_csv('cart.csv', parse_dates=['date'])
df

# %%
df['amount'].astype('Int32')

# %%
df.isnull()

# %%
df.isnull().any(axis=1)

# %%
