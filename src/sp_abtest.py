import pandas as pd
import scipy.stats as stats
def exploracion_df_abtest(df, col_control):
  for categ in df[col_control].unique():
    df_filtrado = df[df[col_control]== categ]
    print(f"Los principales estadisticos de la columna {categ.upper()} son :")
    display(df_filtrado.describe(include='O').T)
    display(df_filtrado.describe().T)
    
    
    
def normalidad(df, lista_metricas):
  for test in lista_metricas:
    statistic, pvalue = stats.shapiro(df[test])
    if pvalue>0.05:
      print(f'Para la columna {test.upper()} si siguen una distribución normal')
    else:
      print(f'Para la columna {test.upper()} no siguen una distribución normal')
      

def homocedasticidad(df, col_control, lista_metricas):
  df_grupos = []
  for metrica in lista_metricas:
    for valor in df[col_control].unique():
      df_grupos.append(df[df[col_control]==valor][metrica])
    statistc, pvalue = stats.levene(*df_grupos)#se le pone un args
    if pvalue>0.05:
      print(f'Para la columna {metrica.upper()} las varianzas son homogenes entre grupos, si que hay homogenesticidad')
    else:
      print(f'Para la columna {metrica.upper()} las varianzas no son homogenes entre grupos, no hay homogenesticidad')
      

def mannwhitneyu(df,col_control,lista_metricas):
  for metrica in lista_metricas:
    valores_control=df[col_control].unique()
    control = df[df[col_control]== valores_control[0]][metrica]
    test = df[df[col_control]== valores_control[1]][metrica]
    statistic, pvalue = stats.mannwhitneyu(control,test)
    if pvalue>0.05:
      print(f'Para la metrica {metrica.upper()}, las medianas son iguales, es decir no hay diferencias significativas entre grupos')
    else:
      print(f'Para la metrica {metrica.upper()}, las medianas no son iguales')