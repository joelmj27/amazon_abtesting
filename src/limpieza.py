import pandas as pd 
def espacios(df):
  "explicar"
  for col in df.select_dtypes(include='O').columns:
    df[col] = df[col].str.replace(' ','_')
    
def comas(df):
  "Explicar"
  for col in df.select_dtypes(include='O').columns:
    df[col] = df[col].str.replace(',','.')
    try:
      df[col] = df[col].astype('float64')
    except:
      pass
    
def minus(df):
  "explicar"
  for col in df.select_dtypes(include='O').columns:
    df[col] = df[col].str.lower()