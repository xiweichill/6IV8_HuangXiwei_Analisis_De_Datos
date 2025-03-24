import numpy as np
import matplotlib.pyplot as plt

#vamos a crear una semilla ramdom para reproductibilidad
np.random.seed(0)

#vamos a buscar los parametros para una distribución
#media
media = 0

#desviaciones estandar
sigma1 = 1
sigma2 = 2
sigma3 = 3

#el numero de muestras para el analisis
n_muestras = 1000

#vamos a generar los datos de las distribuciones normales
data1 = np.random.normal(media, sigma1, n_muestras)
data2 = np.random.normal(media, sigma2, n_muestras)
data3 = np.random.normal(media, sigma3, n_muestras)

#vamos a comfigurar la grafica
plt.figure(figsize=(10, 6))

#vamos a cargar las frecuencias a partir de una grafica de histograma

plt.hist(data1, bins= 30, color='blue', density=True, label='Desviacion Estandar 1', alpha=0.5)

plt.hist(data2, bins= 30, color='red', density=True, label='Desviacion Estandar 2', alpha=0.5)

plt.hist(data3, bins= 30, color='green', density=True, label='Desviacion Estandar 3', alpha=0.5)

#a graficar owo
plt.title('comparacion de distribuciones Normales con una semilla en ramdom')
plt.xlabel('valor')
plt.ylabel('Densidad')
plt.axhline(0, color = 'black', linewidth= 0.5, ls='--')
plt.axvline(0, color = 'black', linewidth= 0.5, ls='--')
plt.legend()
plt.grid()

plt.show()