import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
#Lectira del dataset
movies = pd.read_csv(r'C:\Users\largo\Documents\JDC\2021-2\DATA SIENCE\ProyectoDataSciencie\imbd\peliculas.csv', encoding='utf-8')

#separamos los datos
num =(movies.dtypes == float) | (movies.dtypes == int)
obj = (movies.dtypes == object)

#Columnas numerias
num_cols = [c for c in num.index if num[c]]
movies_nums = movies[num_cols]

#Culmnas de texto
obj_cols = [c for c in obj.index if obj[c]]

#Histograma de la columna de duraccion
movies_nums['duration'].hist()
plt.figure()

#Histograma de la columna de calidad segun IMDB
movies_nums['imdb_score'].hist()
plt.figure()

#Histograma de la columna de presupuestos de las peliculas con error del presupuesto
movies_nums['budget'].hist()
plt.figure()

#Leectura del segundo DataFrame
financials = pd.read_csv(r'C:\Users\largo\Documents\JDC\2021-2\DATA SIENCE\ProyectoDataSciencie\imbd\thenumbers.csv', encoding='utf-8')

#Realizamos un merge
financials = financials[['movie_title', 'production_budget', 'worldwide_gross']]
movies_nums = pd.concat([movies_nums,movies['movie_title']], axis=1)
movies_v2 = pd.merge(financials, movies_nums, on='movie_title', how='left')

#Datos faltantes y limpiar perfectamente la variable objetivo

available = ((movies_v2 != 0) & (movies_v2.notnull()))
available.all(axis=1).value_counts()

mask = available['worldwide_gross']
movies_v2 = movies_v2[mask]

#Eliminamos las columnas duplicadas 
movies_v2 = movies_v2.drop('movie_title', axis=1)
movies_v2 = movies_v2.drop('duration', axis=1)

#Completar los datos faltantes
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

values = imputer.fit_transform(movies_v2)
print(values)

#DataFrame final
X = pd.DataFrame(values)
X.columns = movies_v2.columns
X.index = movies_v2.index

X.to_csv(r'C:\Users\largo\Documents\JDC\2021-2\DATA SIENCE\ProyectoDataSciencie\imbd\X.csv', index=False)
"""


plt.show()
