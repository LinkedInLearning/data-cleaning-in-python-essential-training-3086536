# %%
import pandas as pd

df = pd.read_csv('orders.csv', parse_dates=['time'])
df

# %%
def is_valid_row(row):
    if row['time'] < pd.Timestamp('1900'):
        return False

    if pd.isnull(row['symbol']) or row['symbol'].strip() == '':
        return False

    if row['price'] <= 0:
        return False

    return True


ok_df = df[df.apply(is_valid_row, axis=1)]

# %%
num_bad = len(df) - len(ok_df)
percent_bad = num_bad/len(df) * 100
print(f'{percent_bad:.2f}% bad rows')
if num_bad > 0:
    bad_rows = df[~df.index.isin(ok_df.index)]
    print('bad rows:')
    print(bad_rows)