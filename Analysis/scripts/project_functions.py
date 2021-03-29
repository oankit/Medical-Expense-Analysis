import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
sns.set_style("ticks")
sns.set_theme("paper")
def load_and_process(cwd):
    os.chdir('../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .assign(Over_BMI= np.where(df1['bmi'] > 24.9 ,'Yes','No'))
         .assign(Under_BMI= np.where(df1['bmi'] < 18.5 ,'Yes','No'))
         .assign(Healthy = np.where( ( (df1['bmi'] <= 24.9)& (df1['smoker'] == 'no') & (df1['bmi'] >= 18.5 ) ),'yes','no'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )
    os.chdir(cwd)
    
    return df2


def Health(cwd):
    os.chdir('../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .assign(Healthy = np.where( ( (df1['bmi'] <= 24.9)& (df1['smoker'] == 'no') & (df1['bmi'] >= 18.5 ) ),'yes','no'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfH=(df2[(df2['bmi'] >= 18.5) & (df2['bmi'] <=24.9 ) &(df2['smoker'] == 'no') ])
    dfH= dfH.reset_index(drop=True)
    os.chdir(cwd)
    return dfH

def unHealth(cwd):
    os.chdir('../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .assign(Healthy = np.where( ( (df1['bmi'] <= 24.9)& (df1['smoker'] == 'no') & (df1['bmi'] >= 18.5 ) ),'yes','no'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    
    dfuH = (df2[(df2['bmi'] < 18.5) | (df2['bmi'] >24.9 ) | (df2['smoker'] == 'yes') ])
    dfuH = dfuH.reset_index(drop=True)
    os.chdir(cwd)
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
def smoker(cwd):
    os.chdir('../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['bmi'] >= 18.5) & (df2['bmi'] <= 24.9 ) & (df2['smoker'] == 'yes') ])
    dfuH = dfuH.reset_index(drop=True)
    os.chdir(cwd)
    return dfuH

def underBmi(cwd):
    os.chdir('../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['bmi'] < 18.5) & (df2['smoker'] == 'no') ])
    dfuH = dfuH.reset_index(drop=True)
    os.chdir(cwd)
    return dfuH

def overBmi(cwd):
    os.chdir('../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['bmi'] > 24.9 ) & (df2['smoker']=='no')])
    dfuH = dfuH.reset_index(drop=True)
    os.chdir(cwd)
    return dfuH

def BoxPlt(df):
    g=sns.boxplot(x='Healthy',y='charges',data=df)
    return g
def BoxPlts(df):
    g=sns.boxplot(x='smoker',y='charges',data=df)
    return g
def BoxPltub(df):
    df1=(df[(df['bmi'] <=24.9 ) &(df['smoker'] == 'no') ])
    g=sns.boxplot(x='Under_BMI',y='charges',data=df1)
    return g
def BoxPltob(df):
    df1=(df[(df['bmi'] >=18.5 ) &(df['smoker'] == 'no') ])
    g=sns.boxplot(x='Over_BMI',y='charges',data=df1)
    return g
def mean(df):
    dfm=df['charges'].mean()
    dfmr = round(dfm,2)
    return dfmr
def allsmoker(cwd):
    os.chdir('../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['smoker'] == 'yes')])
    dfuH = dfuH.reset_index(drop=True)
    os.chdir(cwd)
    return dfuH

def obese(cwd):
    os.chdir('../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .assign(Over_BMI= np.where(df1['bmi'] > 24.9 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['bmi'] > 40.0 ) & (df2['smoker']=='no')])
    dfuH = dfuH.reset_index(drop=True)
    os.chdir(cwd)
    return dfuH

def RawDir():
    cwd=os.getcwd()
    os.chdir('../..')
    cwdm=os.getcwd()
    dir = os.chdir("Data/Raw")
    return dir
    
def returnDir(cwd):
    dir = os.chdir(cwd)
    return dir


#submitted data loading

def load_and_processS(cwd):
    os.chdir('../../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .assign(Over_BMI= np.where(df1['bmi'] > 24.9 ,'Yes','No'))
         .assign(Under_BMI= np.where(df1['bmi'] < 18.5 ,'Yes','No'))
         .assign(Healthy = np.where( ( (df1['bmi'] <= 24.9)& (df1['smoker'] == 'no') & (df1['bmi'] >= 18.5 ) ),'yes','no'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )
    os.chdir(cwd)
    
    return df2


def HealthS(cwd):
    os.chdir('../../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .assign(Healthy = np.where( ( (df1['bmi'] <= 24.9)& (df1['smoker'] == 'no') & (df1['bmi'] >= 18.5 ) ),'yes','no'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfH=(df2[(df2['bmi'] >= 18.5) & (df2['bmi'] <=24.9 ) &(df2['smoker'] == 'no') ])
    dfH= dfH.reset_index(drop=True)
    os.chdir(cwd)
    return dfH

def unHealthS(cwd):
    os.chdir('../../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .assign(Healthy = np.where( ( (df1['bmi'] <= 24.9)& (df1['smoker'] == 'no') & (df1['bmi'] >= 18.5 ) ),'yes','no'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    
    dfuH = (df2[(df2['bmi'] < 18.5) | (df2['bmi'] >24.9 ) | (df2['smoker'] == 'yes') ])
    dfuH = dfuH.reset_index(drop=True)
    os.chdir(cwd)
    return dfuH

def smokerS(cwd):
    os.chdir('../../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['bmi'] >= 18.5) & (df2['bmi'] <= 24.9 ) & (df2['smoker'] == 'yes') ])
    dfuH = dfuH.reset_index(drop=True)
    os.chdir(cwd)
    return dfuH

def underBmiS(cwd):
    os.chdir('../../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['bmi'] < 18.5) & (df2['smoker'] == 'no') ])
    dfuH = dfuH.reset_index(drop=True)
    os.chdir(cwd)
    return dfuH

def overBmiS(cwd):
    os.chdir('../../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['bmi'] > 24.9 ) & (df2['smoker']=='no')])
    dfuH = dfuH.reset_index(drop=True)
    os.chdir(cwd)
    return dfuH

def allsmokerS(cwd):
    os.chdir('../../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['smoker'] == 'yes')])
    dfuH = dfuH.reset_index(drop=True)
    os.chdir(cwd)
    return dfuH

def obeseS(cwd):
    os.chdir('../../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .assign(Over_BMI= np.where(df1['bmi'] > 24.9 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['bmi'] > 40.0 ) & (df2['smoker']=='no')])
    dfuH = dfuH.reset_index(drop=True)
    os.chdir(cwd)
    return dfuH

def RawDirS():
    cwd=os.getcwd()
    os.chdir('../../..')
    cwdm=os.getcwd()
    dir = os.chdir("Data/Raw")
    return dir

def RawDirS():
    cwd=os.getcwd()
    os.chdir('../../..')
    cwdm=os.getcwd()
    dir = os.chdir("Data/Raw")
    return dir
#Omar functions

def load_and_process3(cwd):
    os.chdir('../..')
    os.chdir("Data/Raw")
    df1 = (
          pd.read_csv('medical_expenses.csv')
          .dropna(subset=['charges'])
        .rename(columns={'region':'area'})
        .replace({'southwest': 'SW', 'southeast': 'SE', 'northeast': 'NE', 'northwest': 'NW'})
          .round({"bmi":2,"charges":2})
          .sort_values('bmi',ascending=True)
          .reset_index(drop=True)
    )
    os.chdir(cwd)
    return df1

def percentage_young_smokers(df):
    smoker=(df['smoker'] == "yes")
    elderly =df['age'] >= 51
    df[elderly & smoker]
    
    young = df['age']<=27
    df[smoker & young]
    
    index = df[smoker].index
    number_smokers = len(index)
    
    index = df[young].index
    number_young = len(index)
    
    index = df[smoker & young].index
    number_young_smokers = len(index)
    
    percentage = ((number_young_smokers)/(number_young))*100
    print("the percentage of young smokers: {}%".format(percentage))
    return


def percentage_elderly_smokers(df):
    smoker=(df['smoker'] == "yes")
    elderly =df['age'] >= 51
    df[elderly & smoker]
    
    young = df['age']<=27
    df[smoker & young]
    
    index = df[smoker].index
    number_smokers = len(index)
    
    index = df[elderly].index
    number_elderly = len(index)
    
    index = df[smoker & elderly].index
    number_elderly_smokers = len(index)
    
    percentage = ((number_elderly_smokers)/(number_elderly))*100
    print("the percentage of elderly smokers: {}%".format(percentage))
    return

def charges_mean(df):
    average= df["charges"].mean()
    print("the average charges are: {}".format(average))
    return

def boxplot(df):
    x= sns.boxplot(x='area',y='charges',data= df, hue='smoker')
    return x

def lmplot(df):
    x=sns.lmplot(x='age', y='charges', hue='smoker', data=df, markers=['o', '^'], scatter_kws={'s': 100, 'linewidth': 0.5, 'edgecolor': 'w'})
    return x


def lmplot_2(df):
    sns.set_context('poster', font_scale=1.4)
    x= sns.lmplot(x='age', y='charges', data=df, col='area', hue='smoker',
          height=8, aspect=0.6)
    return x

def countplit(df):
    x=sns.countplot(y="area", data=df, palette='Paired', order=df['area'].value_counts().index[:5],hue='smoker')
    return x