import pandas as pd
from IPython.display import display

def stats(data, others=dict()):
    if not isinstance(data, pd.DataFrame):
        data = data.to_frame()
    stats = pd.concat([data.nunique(), data.dtypes, data.isnull().sum()], axis=1)
    stats.columns = ['Unique', 'Dtypes', 'NaN Count']
    for k,v in others.items():
        stats[k] = v(data)
    return stats

def page(data, wrap_cols=14):
    if not isinstance(data, pd.DataFrame):
        data = data.to_frame().T
    for i in range(wrap_cols, data.shape[1]+wrap_cols, wrap_cols):
        print ('Columns', i-wrap_cols, '-', min(i-1,data.shape[1]-1))
        display(data.iloc[:, i-wrap_cols:i])
