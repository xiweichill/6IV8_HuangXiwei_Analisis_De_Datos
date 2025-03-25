import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#leer las dos xlsx
dataset_datos_completos = pd.read_csv('ElementosBasicosEstadistica/proyecto1.csv')
dataset_datos_catalogos = pd.read_csv('ElementosBasicosEstadistica/Catalogo_sucursal.csv')


df_unido = pd.merge(dataset_datos_completos, dataset_datos_catalogos, on='id_sucursal', how='inner')

#1.- Ventas totales del comercio
total_venta = sum(df_unido['ventas_tot'])
print(f'total de ventas {total_venta}')
#2.- Gentes con adeudos y sin adeudos en por centaje
filter_con_adeudos = list(filter(lambda persona : persona == 'Con adeudo', df_unido['B_adeudo']))
filter_sin_adeudos = list(filter(lambda persona : persona == 'Sin adeudo', df_unido['B_adeudo']))

con_adeudos_porcentaje = len(filter_con_adeudos) *100 / (len(df_unido.iloc[:]))
sin_adeudos_porcentaje = len(filter_sin_adeudos) * 100 / len(df_unido.iloc[:])
print(f'Porcentaje de la gente con adeudos {con_adeudos_porcentaje}% \nPorcenta de la gente sin adeudos {sin_adeudos_porcentaje}%')

#3.-Grafica donde se pueda observar las ventas totales respecto del tiempo, en una grafica de barras 
plt.figure(figsize=(10,6))
plt.bar(df_unido['B_mes'],df_unido['ventas_tot'],color = 'red')
plt.xlabel('B_mes')
plt.ylabel('Ventas totales')
plt.title('Ventas totales por B_mes')
plt.show()

#4.-Grafica donde se pueda visualizar la desviación estándar de los pagos realizados del comercio respecto del tiempo
# Calcula la desviación estándar agrupando por 'B_mes', profe aqui no se que hizo, pero encontre que tiene que unir las doscolumnas para sacar su desviacion estandar de valores por usuario en cada fecha
std_by_mes = df_unido.groupby('B_mes')['pagos_tot'].std().sort_index()

# Grafica usando el método de plot de Pandas
plt.figure(figsize=(10,6))
std_by_mes.plot.bar(color='skyblue')
plt.xlabel('Mes (B_mes)')
plt.ylabel('Desviación estándar de pagos')
plt.title('Desviación estándar de pagos por mes')
plt.show()

#5.-Cuanto es la deuda total de los clientes
total_deudos = sum(df_unido['adeudo_actual'])
print(f'el total de deudos es {total_deudos}')

# 6.-Cuanto es el porcentaje de utilidad del comercio a partir de el total de las ventas respecto del adeudo 