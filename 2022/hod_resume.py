#%%
import pandas as pd
import polars as pl

#%%
pd_df = pd.read_parquet('noahs.parquet')
pd_df['ordered_date'] = pd_df.ordered.dt.date
pd_df = pd_df.astype({
    'customerid': 'int',
    'name': 'string',
    'address': 'string',
    'citystatezip': 'string',
    'birthdate': 'datetime64[ns]',
    'phone': 'string',
    'orderid': 'int',
    'ordered': 'datetime64[ns]',
    'ordered_date': 'datetime64[ns]',
    'shipped': 'datetime64[ns]',
    'total': 'float',
    'qty': 'int',
    'unit_price': 'float',
    'sku': 'string',
    'desc': 'string',
    'wholesale_cost': 'float'
})

#%%
df = pl.read_parquet('noahs.parquet', use_pyarrow=True)
df = df.with_columns([
    pl.col('customerid').cast(pl.Int64),
    pl.col('name').cast(pl.Utf8),
    pl.col('address').cast(pl.Utf8),
    pl.col('citystatezip').cast(pl.Utf8),
    pl.col('birthdate').cast(pl.Datetime),
    pl.col('phone').cast(pl.Utf8),
    pl.col('orderid').cast(pl.Int64),
    pl.col('ordered').cast(pl.Datetime),
    pl.col('shipped').cast(pl.Datetime),
    pl.col('total').cast(pl.Float64),
    pl.col('qty').cast(pl.Int64),
    pl.col('unit_price').cast(pl.Float64),
    pl.col('sku').cast(pl.Utf8),
    pl.col('desc').cast(pl.Utf8),
    pl.col('wholesale_cost').cast(pl.Float64),
    pl.col('ordered').cast(pl.Date).alias('ordered_date')
])

#%%
df.select([pl.col('ordered').cast(pl.Date)])
