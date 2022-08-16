# %%
import pandas as pd

df = pd.read_csv('workshops.csv')
df

# %% Fill Year & Month
"""
Fix the data frame. At the end, row should have the following columns:
- start: pd.Timestemap
- end: pd.Timestamp
- name: str
- topic: str (python or go)
- earnings: np.float64
"""
df['Year'].fillna(method='ffill', inplace=True)
df['Month'].fillna(method='ffill', inplace=True)
df

# %% Drop year & month rows
df = df[pd.notnull(df['Earnings'])].copy()
df

# %%
def as_date(row, col):
    year = int(row['Year'])
    month = row['Month']
    day = int(row[col])
    ts = f'{month} {day}, {year}'
    return pd.to_datetime(ts, format='%B %d, %Y')

df['start'] = df.apply(as_date, axis=1, args=('Start',))
df['end'] = df.apply(as_date, axis=1, args=('End',))
df

# %% Extract topic
def topic(name):
    if 'go' in name:
        return 'go'
    if 'python' in name:
        return 'python'

df['topic'] = df['Name'].str.lower().apply(topic)
df

# %% Earnings
import numpy as np
df['earnings'] = pd.to_numeric(
    df['Earnings'].str.replace(r'[$,]', '')
).astype(np.float64)
df

# %% Cleanup
df = df[['start', 'end', 'Name', 'topic', 'earnings']]
df.rename(columns={'Name': 'name'}, inplace=True)
df