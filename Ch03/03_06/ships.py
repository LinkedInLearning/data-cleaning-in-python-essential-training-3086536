# %%
import numpy as np
import pandera as pa
import pandas as pd

df = pd.read_csv('ships.csv')
df
# %%

schema = pa.DataFrameSchema({
    'name': pa.Column(
        pa.String,
        nullable=False,
        checks=[
            pa.Check.str_length(min_value=2)
        ]
    ),
    'lat': pa.Column(
        pa.Float,
        nullable=False,
        checks=[
            pa.Check.ge(-90),
            pa.Check.le(90)
        ]
    ),
    'lng': pa.Column(
        pa.Float,
        nullable=False,
        checks=[
            pa.Check.ge(-180),
            pa.Check.le(180)
        ]
    ),
})

schema.validate(df)
