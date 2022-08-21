# %%
import pandas as pd
import numpy as np

size = 5
df = pd.DataFrame({
    'time': pd.date_range('2021', freq='17s', periods=size),
    'name': ['cpu'] * size,
    'value': np.random.rand(size) * 40,
})
df

# %%
import pyarrow as pa

schema = pa.schema([
    ('time', pa.timestamp('ms')),
    ('name', pa.string()),
    ('value', pa.float64()),
])

# %%
out_file = 'metrics.parquet'
df.to_parquet(out_file, schema=schema)

# %%
pd.read_parquet(out_file)

# %%
df['time'] = df['time'].astype(str)
df.to_parquet(out_file, schema=schema)