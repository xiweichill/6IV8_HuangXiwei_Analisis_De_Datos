import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean, cityblock, chebyshev

# Diccionario de puntos
puntos = {
    'Punto A': (2, 3),
    'Punto B': (5, 4),
    'Punto C': (1, 1),
    'Punto D': (6, 7),
    'Punto E': (3, 5),
    'Punto F': (8, 2),
    'Punto G': (4, 6),
    'Punto H': (2, 1)
}

# Convertimos los puntos a un DataFrame
df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['X', 'Y']
print("Coordenadas de los puntos:")
print(df_puntos)

def calcular_distancias(df):
    # Inicializamos dataframes para cada métrica
    metrics = {
        'Euclidiana': pd.DataFrame(index=df.index, columns=df.index),
        'Manhattan': pd.DataFrame(index=df.index, columns=df.index),
        'Chebyshev': pd.DataFrame(index=df.index, columns=df.index)
    }
    
    # Calculamos las distancias (usando doble bucle)
    for i in df.index:
        for j in df.index:
            if i == j:
                metrics['Euclidiana'].loc[i, j] = 0
                metrics['Manhattan'].loc[i, j] = 0
                metrics['Chebyshev'].loc[i, j] = 0
            else:
                metrics['Euclidiana'].loc[i, j] = euclidean(df.loc[i], df.loc[j])
                metrics['Manhattan'].loc[i, j] = cityblock(df.loc[i], df.loc[j])
                metrics['Chebyshev'].loc[i, j] = chebyshev(df.loc[i], df.loc[j])
    
    # Convertimos a tipo numérico
    for key in metrics:
        metrics[key] = metrics[key].astype(float)
    
    return metrics

# Calculamos las matrices de distancia
distance_matrices = calcular_distancias(df_puntos)

# Para cada métrica, encontramos el par de puntos con la distancia máxima y la mínima (excluyendo la diagonal)
results = {}
for metric, matrix in distance_matrices.items():
    max_val = matrix.values.max()
    min_val = matrix[matrix > 0].values.min()  # la menor distancia positiva
    max_pair = matrix.stack().idxmax()           # par con mayor distancia
    min_pair = matrix[matrix > 0].stack().idxmin() # par con menor distancia
    results[metric] = {
        'max_val': max_val,
        'max_pair': max_pair,
        'min_val': min_val,
        'min_pair': min_pair,
        'matrix': matrix
    }
    print(f"\nDistancias {metric}:")
    print(matrix)
    print(f"Distancia máxima: {max_val} entre {max_pair[0]} y {max_pair[1]}")
    print(f"Distancia mínima: {min_val} entre {min_pair[0]} y {min_pair[1]}")


