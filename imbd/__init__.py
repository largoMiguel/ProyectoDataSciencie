import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Lectira del dataset
movies = pd.read_csv(r'C:\Users\largo\Documents\JDC\2021-2\DATA SIENCE\ProyectoDataSciencie\imbd\peliculas.csv')

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
plt.legend()
plt.figure()
plt.show()

#Histograma de la columna de calidad segun IMDB
movies_nums['imdb_score'].hist()
plt.legend()
plt.figure()
plt.show()

#Histograma de la columna de presupuestos de las peliculas
movies_nums['budget'].hist()
plt.legend()
plt.figure()
plt.show()

