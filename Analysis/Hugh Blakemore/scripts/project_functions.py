import pandas as pd
def load_and_process(url):
    df1 = (
          pd.read_csv(url)
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )
    return df2