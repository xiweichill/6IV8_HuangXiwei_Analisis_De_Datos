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

# Graficamos cada métrica en un subplot
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for ax, (metric, data) in zip(axes, results.items()):
    # Graficamos los puntos
    ax.scatter(df_puntos['X'], df_puntos['Y'], color='blue')
    for label, row in df_puntos.iterrows():
        ax.text(row['X'] + 0.1, row['Y'] + 0.1, label)
    
    # Resaltamos el par de puntos con la distancia máxima (línea roja sólida)
    p1, p2 = data['max_pair']
    x_max = [df_puntos.loc[p1, 'X'], df_puntos.loc[p2, 'X']]
    y_max = [df_puntos.loc[p1, 'Y'], df_puntos.loc[p2, 'Y']]
    ax.plot(x_max, y_max, color='red', linestyle='-', linewidth=2, label='Máxima distancia')
    
    # Resaltamos el par de puntos con la distancia mínima (línea verde discontinua)
    p1_min, p2_min = data['min_pair']
    x_min = [df_puntos.loc[p1_min, 'X'], df_puntos.loc[p2_min, 'X']]
    y_min = [df_puntos.loc[p1_min, 'Y'], df_puntos.loc[p1_min, 'Y']]  # <-- Atención: corregir si es necesario
    # Corrigiendo: se debe usar df_puntos.loc[p2_min, 'Y'] para el segundo punto
    y_min = [df_puntos.loc[p1_min, 'Y'], df_puntos.loc[p2_min, 'Y']]
    ax.plot(x_min, y_min, color='green', linestyle='--', linewidth=2, label='Mínima distancia')
    
    ax.set_title(f"Distancia {metric}")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.show()
