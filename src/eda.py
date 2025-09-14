import pandas as pd
def eda_preeliminar (df):
  '''
  Aqui se explica la funcion para que las personas sepan que se está realizando. 
  
  
  '''
  display(df.sample(5))
  print("--------")
  print(df.shape)
  print("---------")
  print("INFO")
  display(df.info())
  print("---------")
  print("Nulos")
  print(df.isnull().sum()/df.shape[0]*100)
  print("---------")
  print("Duplicados")
  print(df.duplicated().sum())
  print("------------")
  print('ESTADISTICOS NUMERICOS')
  display(df.describe().T)
  print('-------------')
  print("Frecuencia")
  categoric_columns = df.select_dtypes(include='O').columns
  for col in categoric_columns:
    print(f"Las categorias de las columna {col} son las siguientes:")
    print(df[col].value_counts())
    print("-----------------------------------------------------------")
