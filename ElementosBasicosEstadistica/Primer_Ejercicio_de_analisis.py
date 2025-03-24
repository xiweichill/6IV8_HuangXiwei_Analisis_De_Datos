import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#leer las dos xlsx
dataset_datos_completos = pd.read_csv('ElementosBasicosEstadistica/proyecto1.csv')
dataset_datos_catalogos = pd.read_csv('ElementosBasicosEstadistica/Catalogo_sucursal.csv')


df_unido = pd.merge(dataset_datos_completos, dataset_datos_catalogos, on='id_sucursal', how='inner')

#1.- Ventas totales del comercio
total_venta = sum(df_unido['ventas_tot'])
print(total_venta)
#2.- Gentes con adeudos y sin adeudos en por centaje
filter_con_adeudos = list(filter(lambda persona : persona == 'Con adeudo', df_unido['B_adeudo']))
filter_sin_adeudos = list(filter(lambda persona : persona == 'Sin adeudo', df_unido['B_adeudo']))
print((len(df_unido.iloc[:])))
con_adeudos_porcentaje = len(filter_con_adeudos) *100 / (len(df_unido.iloc[:]))
sin_adeudos = len(filter_sin_adeudos)
print(con_adeudos_porcentaje)

#3