import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('housing.csv')

#mostrar las primeras 5 filas
print(df.head())

#mostrar las ultimas 5 filas
print(df.tail())

#mostrar una fila en espefico
print(df.iloc[7-10])

#mostrar la columna ocean_proximity
print(df["ocean_proximity"])

#mediadecuarto la media de la colimna total_rooms
mediadecuarto = df['total_rooms'].mean()
print('la media de total room es ', mediadecuarto)

#mediana
medianacuarto = df['median_house_value'].median()
print('la mediana de la columna valor mediana de la casa ', medianacuarto)

#la suma de popular
salariototal = df['population'].sum()
print('El salario total es de ', salariototal)

#para poder filtrar 
vamoshacerunfiltro = df[df['ocean_proximity'] == 'ISLAND']
print(vamoshacerunfiltro)

#vamos a hacer una grafico de dispersion
plt.scatter(df['ocean_proximity'][:10],df['median_house_value'][:10])
#nombramos los ejes
plt.xlabel('Proximidad')
plt.ylabel('Precio')

plt.title('Grafico de Dispersion de Proximidad al oceano vs Precio')
plt.show()