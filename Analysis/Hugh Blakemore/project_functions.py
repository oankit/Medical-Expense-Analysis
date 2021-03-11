<<<<<<< HEAD
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("ticks")
sns.set_theme("paper")
=======

>>>>>>> a5484ef00e79e6993b42b565b0e75aad8f2f5a88
def load_and_process(url):
    import pandas as pd
    df1 = (
          pd.read_csv(url)
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
<<<<<<< HEAD
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .assign(Over_BMI= np.where(df1['bmi'] > 24.9 ,'Yes','No'))
         .assign(Under_BMI= np.where(df1['bmi'] < 18.5 ,'Yes','No'))
=======
>>>>>>> a5484ef00e79e6993b42b565b0e75aad8f2f5a88
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )
    return df2
<<<<<<< HEAD

def Health(url):
    df1 = (
          pd.read_csv(url)
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfH=(df2[(df2['bmi'] >= 18.5) & (df2['bmi'] <=24.9 ) &(df2['smoker'] == 'no') ])
    return dfH

def unHealth(url):
    df1 = (
          pd.read_csv(url)
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['bmi'] < 18.5) | (df2['bmi'] >24.9 ) | (df2['smoker'] == 'yes') ])
    return dfuH




def plotAvC(df):
    g=sns.lmplot(x='age', y='charges',data=df, 
          scatter_kws={'s': 100, 'linewidth': 0.5, 'edgecolor': 'w'})
    return g
def brpltEC(df):
    g = sns.countplot(x="Excess_charges",data=df)
    return g
def BrPltECD(df):
    g=sns.histplot(
    df, x="Excess_charges", element="bars",
    stat="density",multiple="dodge"
    )
    return g

def BrPltECDh(df):
    g=sns.histplot(
    df, x="Excess_charges", element="bars",
    stat="density",multiple="dodge",hue="smoker"
    )
    return g
def BrPltECDB(df):
    g=sns.histplot(
    df, x="Excess_charges", element="bars",
    stat="density",multiple="dodge",hue="bmi"
    )
    return g
def smoker(url):
    df1 = (
          pd.read_csv(url)
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['smoker'] == 'yes') ])
    return dfuH

def underBmi(url):
    df1 = (
          pd.read_csv(url)
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['bmi'] < 18.5)])
    return dfuH

def overBmi(url):
    df1 = (
          pd.read_csv(url)
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['bmi'] >24.9 )])
    return dfuH
def BoxPlts(df):
    g=sns.boxplot(x='smoker',y='charges',data=df)
    return g
def BoxPltub(df):
    g=sns.boxplot(x='Under_BMI',y='charges',data=df)
    return g
def BoxPltob(df):
    g=sns.boxplot(x='Over_BMI',y='charges',data=df)
    return g

def kdPlt(df):
    g=sns.kdeplot(df['charges'])
    return g 
=======
>>>>>>> a5484ef00e79e6993b42b565b0e75aad8f2f5a88
