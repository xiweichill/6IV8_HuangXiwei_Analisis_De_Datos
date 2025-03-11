
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("housing.csv")

columna_median_house = dataset["median_house_value"]
#print(columna_median_house)
#probando como sacar rango
rango = columna_median_house.max() - columna_median_house.min()
#print(rango)
#numero 283421, es un rango que yo pense establecerlo, si no pues es que no entendi xd
dataframe = pd.DataFrame([columna_median_house.mean(),columna_median_house.median(),columna_median_house.mode(),283421, columna_median_house.var(), columna_median_house.std()], index = ['Media','Mediana','Moda','Rango','Varianza','Desviacion estandar'])

print(dataframe)

# Graficar histogramas en subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Histograma para median_house_value con línea de la media
axes[0].hist(columna_median_house, bins=30, alpha=0.7, color='skyblue', label='Median House Value')
axes[0].axvline(columna_median_house.mean(), color='red', linestyle='dashed', linewidth=1, label='Media')
axes[0].set_xlabel('Median House Value')
axes[0].set_ylabel('Frecuencia')
axes[0].set_title('Histograma de Median House Value')
axes[0].legend()

# Histograma para total_bedrooms
axes[1].hist(dataset["total_bedrooms"], bins=30, alpha=0.7, color='lightgreen', label='Total Bedrooms')
axes[1].set_xlabel('Total Bedrooms')
axes[1].set_ylabel('Frecuencia')
axes[1].set_title('Histograma de Total Bedrooms')
axes[1].legend()

# Histograma para population
axes[2].hist(dataset["population"], bins=30, alpha=0.7, color='lightcoral', label='Population')
axes[2].set_xlabel('Population')
axes[2].set_ylabel('Frecuencia')
axes[2].set_title('Histograma de Population')
axes[2].legend()

plt.tight_layout()
plt.show()




