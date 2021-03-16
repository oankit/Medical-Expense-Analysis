import pandas as pd
def load_and_process(address):
    df1 = (
          pd.read_csv(address)
          .dropna(subset=['bmi'])
          .round({"bmi":1})
          .sort_values('bmi',ascending=True)
          .reset_index(drop=True)
    )
    return df1

def average_bmi(df):
    average = df["bmi"].mean()
    print("Average bmi: ",average)
    return

def average_charges(df):
    average = df["charges"].mean()
    print("Average charges: ",average)
    return

def plotAvgBmi(df):
    g=sns.lmplot(x='age', y='bmi',data=df, 
          scatter_kws={'s': 100, 'linewidth': 1.0, 'edgecolor': 'w'})
    return g

def plotAvgCharges(df):
    g=sns.lmplot(x='age', y='charges',data=df, 
          scatter_kws={'s': 100, 'linewidth': 1.0, 'edgecolor': 'w'})
    return g