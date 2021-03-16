import pandas as pd
import numpy as np
import seaborn as sns
def load_and_process(address):
    df1 = (
          pd.read_csv(address)
          .dropna(subset=['charges'])
        .rename(columns={'region':'area'})
        .replace({'southwest': 'SW', 'southeast': 'SE', 'northeast': 'NE', 'northwest': 'NW'})
          .round({"bmi":2,"charges":2})
          .sort_values('bmi',ascending=True)
          .reset_index(drop=True)
    )
    return df1
