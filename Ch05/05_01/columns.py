# %%
import pandas as pd

df = pd.read_csv('weather.csv', parse_dates=['DATE'])
df
# %%
df.rename(columns={
    'DATE': 'date',
    'TMIN': 'min_temp',
    'TMAX': 'max_temp',
}, inplace=True)
df
# %%
df = pd.read_csv('donations.csv')
df
# %%
import re


def fix_col(col):
    """Fix column name
    >>> fix_col('1. First Name')
    'first_name'
    """
    return (
        re.sub(r'\d+\.\s+', '', col)
        .lower()
        .replace(' ', '_')
    )

df.rename(columns=fix_col, inplace=True)
df