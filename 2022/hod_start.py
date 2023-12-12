import numpy as np
import pandas as pd
import sqlite3

con = sqlite3.connect('noahs.sqlite')
df = pd.read_sql_query('''
select
  c.*,
  o.orderid,
  o.ordered,
  o.shipped,
  o.total,
  i.qty,
  i.unit_price,
  p.sku,
  p.desc,
  p.wholesale_cost
from
  customers c
  join orders o on c.customerid = o.customerid
  join orders_items i on o.orderid = i.orderid
  join products p on i.sku = p.sku''',
  con,
  parse_dates=['ordered','shipped'])
dtypes = {col: 'category' for col, dtype in df.dtypes.to_dict().items() if dtype != np.dtype('datetime64[ns]')}
dtypes['orderid'] = 'int'

#df.astype(dtypes).memory_usage(deep=True).sum()
#df.memory_usage(deep=True).sum()
# ^^ ~10% mem usage after type conversion

df = df.astype(dtypes)
